<!DOCTYPE html>
<html lang="mg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Forex Signal Live Analyzer</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { background-color: #0f111a; color: #ffffff; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { background: #161925; width: 100%; max-width: 450px; padding: 30px; border-radius: 16px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5); border: 1px solid #23283d; text-align: center; }
        h1 { font-size: 22px; color: #4ef2d2; margin-bottom: 25px; font-weight: 700; }
        .form-group { text-align: left; margin-bottom: 18px; }
        label { display: block; font-size: 14px; color: #94a3b8; margin-bottom: 8px; }
        select { width: 100%; padding: 12px; background: #202436; border: 1px solid #2d334d; color: #fff; border-radius: 8px; font-size: 15px; outline: none; }
        .btn-analyze { width: 100%; padding: 14px; background: linear-gradient(135deg, #ff007f, #7928ca); border: none; color: white; font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer; margin-top: 15px; box-shadow: 0 4px 15px rgba(255, 0, 127, 0.3); }
        .result-box { margin-top: 25px; background: #1e2235; border-radius: 12px; padding: 20px; border: 1px dashed #2d334d; min-height: 140px; display: flex; flex-direction: column; justify-content: center; align-items: center; }
        .status { font-size: 15px; color: #a0a0a0; font-style: italic; margin-bottom: 10px; }
        .signal { font-size: 28px; font-weight: 800; }
        .buy-style { color: #00ff66; text-shadow: 0 0 15px rgba(0, 255, 102, 0.4); }
        .sell-style { color: #ff3333; text-shadow: 0 0 15px rgba(255, 51, 51, 0.4); }
        .neutral-style { color: #8e9aa8; }
        .details { margin-top: 10px; font-size: 13px; color: #4ef2d2; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 FOREX AI REAL ANALYZER</h1>
        <div class="form-group">
            <label>Safidio ny Marche (Pair):</label>
            <select id="market">
                <option value="EUR/USD">EUR/USD</option>
                <option value="GBP/USD">GBP/USD</option>
                <option value="USD/JPY">USD/JPY</option>
                <option value="AUD/USD">AUD/USD</option>
            </select>
        </div>
        <div class="form-group">
            <label>Safidio ny Timeframe:</label>
            <select id="timeframe">
                <option value="1m">1 minitra</option>
                <option value="2m">2 minitra</option>
                <option value="5m">5 minitra</option>
            </select>
        </div>
        <button class="btn-analyze" onclick="runLiveAnalysis()">START ANALYSE 🔍</button>
        <div class="result-box">
            <div id="status" class="status">Miandry analyse...</div>
            <div id="signal" class="signal"></div>
            <div id="details" class="details"></div>
        </div>
    </div>

    <script>
        async function runLiveAnalysis() {
            const pair = document.getElementById("market").value;
            const timeframe = document.getElementById("timeframe").value;
            
            const statusDiv = document.getElementById("status");
            const signalDiv = document.getElementById("signal");
            const detailsDiv = document.getElementById("details");

            statusDiv.innerHTML = `Manao analyse mivantana an'i ${pair}...`;
            statusDiv.style.color = "#ffcc00";
            signalDiv.innerHTML = "";
            detailsDiv.innerHTML = "";

            try {
                // Mandefa fangatahana any amin'ny Python Backend (API)
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/center+json', 'Content-Type': 'application/json' },
                    body: JSON.stringify({ pair: pair, timeframe: timeframe })
                });
                
                const data = await response.json();
                
                statusDiv.innerHTML = `✅ Analyse vita ho an'ny ${data.pair}`;
                statusDiv.style.color = "#4ef2d2";

                if (data.signal === "BUY") {
                    signalDiv.innerHTML = "🟢 BUY (CALL)";
                    signalDiv.className = "signal buy-style";
                    detailsDiv.innerHTML = `Ora: ${data.time}<br>⏱ <b>Expiration: Afaka 2 minitra</b>`;
                } else if (data.signal === "SELL") {
                    signalDiv.innerHTML = "🔴 SELL (PUT)";
                    signalDiv.className = "signal sell-style";
                    detailsDiv.innerHTML = `Ora: ${data.time}<br>⏱ <b>Expiration: Afaka 2 minitra</b>`;
                } else {
                    signalDiv.innerHTML = "🚫 NO SIGNAL";
                    signalDiv.className = "signal neutral-style";
                    statusDiv.innerHTML = `⚠️ Tsy misy tondro mazava`;
                    statusDiv.style.color = "#ffcc00";
                    detailsDiv.innerHTML = "Milamina ny tsena. Andramo indray mialoha ny labozia manaraka.";
                }
            } catch (error) {
                statusDiv.innerHTML = "❌ Diso ny fifandraisana amin'ny server.";
                statusDiv.style.color = "#ff3333";
            }
        }
    </script>
</body>
</html>
