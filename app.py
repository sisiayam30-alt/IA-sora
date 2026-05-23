from flask import Flask, render_template, jsonify, request
import random
import datetime
import pandas as pd
import ta

app = Flask(__name__, template_folder='.')

def analyze_market_live(pair, timeframe):
    """
    Eto no maka ny data mivantana sy mikajy ny tondro ara-teknika.
    (Soloina ny API-n'ny broker-nao haka ny labozia mivantana ity any aoriana).
    """
    # Mamorona data labozia 50 kisendrasendra fotsiny aloha ho an'ny kajy
    prices = [round(random.uniform(1.0950, 1.1050), 4) for _ in range(50)]
    df = pd.DataFrame({
        'close': prices,
        'high': [p + 0.001 for p in prices],
        'low': [p - 0.001 for p in prices]
    })
    
    # Mikajy RSI sy Bollinger Bands
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    indicator_bb = ta.volatility.BollingerBands(close=df['close'], window=20, window_dev=2)
    df['bb_high'] = indicator_bb.bollinger_hband()
    df['bb_low'] = indicator_bb.bollinger_lband()
    
    last_row = df.iloc[-1]
    current_price = last_row['close']
    rsi = last_row['rsi']
    bb_high = last_row['bb_high']
    bb_low = last_row['bb_low']
    
    # Fandinihana ny Signal
    if rsi > 65 or current_price >= bb_high:
        return "SELL"
    elif rsi < 35 or current_price <= bb_low:
        return "BUY"
    else:
        return "NEUTRAL"

@app.route('/')
def index():
    # Mampiseho ilay pejy index.html
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    pair = data.get('pair')
    timeframe = data.get('timeframe')
    
    # Antsoina ilay asa manao analyse
    result = analyze_market_live(pair, timeframe)
    
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    
    return jsonify({
        "status": "success",
        "pair": pair,
        "timeframe": timeframe,
        "signal": result,
        "time": time_str
    })

if __name__ == '__main__':
    # Handeha amin'ny port 5000 ny bot-nao
    app.run(debug=True, port=5000)
