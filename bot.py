from flask import Flask, render_request, jsonify, render_template
import yfinance as yf
import pandas as pd

app = Flask(__name__, template_folder=".")

def calculate_indicators(df):
    # Mikajy Moving Average (SMA 14)
    df['SMA'] = df['Close'].rolling(window=14).mean()
    
    # Mikajy RSI (14)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['GET'])
def analyze():
    # Maka ny pair avy amin'ny tranonkala
    market = render_request.args.get('market', 'EUR/USD')
    timeframe = render_request.args.get('timeframe', '1 MIN')
    
    # Diovina ny anaran'ny pair raha misy "OTC" na "Real"
    clean_market = market.replace(" (OTC)", "").replace(" (Real)", "")
    
    # Avadika ho kaody mifanaraka amin'ny yfinance
    ticker_map = {
        "EUR/USD": "EURUSD=X",
        "GBP/USD": "GBPUSD=X",
        "USD/JPY": "JPY=X",
        "AUD/USD": "AUDUSD=X",
        "USD/CHF": "CHF=X",
        "EUR/GBP": "EURGBP=X",
        "EUR/JPY": "EURJPY=X",
        "NZD/USD": "NZDUSD=X",
        "AUD/CAD": "AUDCAD=X",
        "AUD/JPY": "AUDJPY=X",
        "EUR/AUD": "EURAUD=X",
        "GBP/JPY": "GBPJPY=X",
        "GOLD": "GC=F",
        "SILVER": "SI=F",
        "CRUDE OIL": "CL=F",
        "BRENT OIL": "BZ=F",
        "APPLE": "AAPL",
        "GOOGLE": "GOOGL",
        "MICROSOFT": "MSFT",
        "AMAZON": "AMZN",
        "FACEBOOK": "META",
        "TESLA": "TSLA",
        "NETFLIX": "NFLX",
        "ALIBABA": "BABA",
        "INTEL": "INTC",
        "VISA": "V"
    }
    
    ticker = ticker_map.get(clean_market, "EURUSD=X")
    
    try:
        # Maka data farany (labozia 1 minitra miisa 40)
        data = yf.download(tickers=ticker, period="1d", interval="1m", progress=False)
        
        if data.empty or len(data) < 15:
            return jsonify({"status": "error", "message": "Tsy azo ny data avy amin'ny tsena"})
        
        # Kajy ara-teknika
        data = calculate_indicators(data)
        
        last_row = data.iloc[-1]
        current_price = float(last_row['Close'])
        rsi_value = float(last_row['RSI'])
        sma_value = float(last_row['SMA'])
        
        # Paikady (Strategy): RSI + Trend SMA
        # Raha RSI latsaky ny 30 (Oversold) sy ny vidiny ambony SMA -> BUY
        if rsi_value < 35 and current_price > sma_value:
            signal = "🟢 HIGHER (CALL)"
            action_text = "TSINDRIO BOKOTRA MAITSO"
            style = "buy-style"
        # Raha RSI ambony 70 (Overbought) sy ny vidiny ambany SMA -> SELL
        elif rsi_value > 65 and current_price < sma_value:
            signal = "🔴 LOWER (PUT)"
            action_text = "TSINDRIO BOKOTRA MENA"
            style = "sell-style"
        else:
            signal = "🚫 NO SIGNAL"
            action_text = "Milamina ny tsena. Miandrasa labozia vaovao."
            style = "nosignal-style"
            
        return jsonify({
            "status": "success",
            "market": market,
            "timeframe": timeframe,
            "signal": signal,
            "action": action_text,
            "style": style,
            "rsi": round(rsi_value, 2),
            "price": round(current_price, 5)
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
