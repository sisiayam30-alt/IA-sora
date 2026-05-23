import tkinter as tk
from tkinter import ttk, messagebox
import random
import datetime

class ForexSignalBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Forex AI Signal Bot")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e2e") # Loko maizina ho an'ny interface tsara tarehy

        # --- STYLING ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#1e1e2e", foreground="#ffffff", font=("Arial", 11))
        style.configure("TCombobox", fieldbackground="#2d2d3f", background="#2d2d3f", foreground="#ffffff")

        # --- TITRE ---
        title_label = tk.Label(root, text="📊 FOREX SIGNAL ANALYZER", bg="#1e1e2e", fg="#4ef2d2", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)

        # --- SELECTION MARCHE (PAIR) ---
        ttk.Label(root, text="Safidio ny Marche (Pair):").pack(pady=5)
        self.pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF", "EUR/GBP", "EUR/JPY"]
        self.pair_box = ttk.Combobox(root, values=self.pairs, state="readonly", width=25)
        self.pair_box.set("EUR/USD") # Atomboka amin'ny EUR/USD
        self.pair_box.pack(pady=5)

        # --- SELECTION TIMEFRAME ---
        ttk.Label(root, text="Safidio ny Timeframe (Kandrina):").pack(pady=5)
        self.timeframes = ["1 minitra", "2 minitra", "3 minitra", "5 minitra"]
        self.tf_box = ttk.Combobox(root, values=self.timeframes, state="readonly", width=25)
        self.tf_box.set("1 minitra")
        self.tf_box.pack(pady=5)

        # --- BOKOTRA HANAO ANALYSE ---
        self.analyze_btn = tk.Button(root, text="START ANALYSE 🔍", bg="#ff007f", fg="white", font=("Arial", 12, "bold"), 
                                     command=self.start_analysis, width=20, height=2, bd=0, cursor="hand2")
        self.analyze_btn.pack(pady=25)

        # --- ZONE HASEHOANA NY REVOLUTION / SIGNAL ---
        self.result_frame = tk.Frame(root, bg="#2d2d3f", bd=2, relief="groove")
        self.result_frame.pack(pady=10, fill="x", padx=30)

        self.status_label = tk.Label(self.result_frame, text="Miandry analyse...", bg="#2d2d3f", fg="#a0a0a0", font=("Arial", 11, "italic"))
        self.status_label.pack(pady=10)

        self.signal_label = tk.Label(self.result_frame, text="", bg="#2d2d3f", fg="white", font=("Arial", 20, "bold"))
        self.signal_label.pack(pady=10)

        self.time_label = tk.Label(self.result_frame, text="", bg="#2d2d3f", fg="#4ef2d2", font=("Arial", 10))
        self.time_label.pack(pady=5)

    def start_analysis(self):
        """ Mampiseho simulation fa manao analyse ny bot alohan'ny hanomezana signal """
        pair = self.pair_box.get()
        tf = self.tf_box.get()
        
        self.status_label.config(text=f"Manao analyse ny {pair} ({tf})... miandrasa kely", fg="#ffcc00")
        self.signal_label.config(text="")
        self.time_label.config(text="")
        self.root.update()
        
        # Akatona kely ny fotoana (simulation analyse mandritra ny 1.5 segondra)
        self.root.after(1500, self.generate_signal)

    def generate_signal(self):
        """ Ny kajy rehetra amin'ny analyse no mifarana eto ary mamoaka BUY na SELL """
        pair = self.pair_box.get()
        
        # Eto no misy ny algorithm-nao (RSI, Moving Averages, etc.)
        # Amin'ity ohatra ity, hataontsika kisendrasendra (Simulation) nefa azo ampitandremana amin'ny API vao tena misy any aoriana
        r = random.randint(1, 3)
        
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M:%S")

        if r == 1:
            # Raha BUY ilay izy
            self.status_label.config(text=f"✅ Analyse vita ho an'ny {pair}", fg="#4ef2d2")
            self.signal_label.config(text="🟢 BUY (CALL)", fg="#00ff66")
            self.time_label.config(text=f"Fotoana: {time_str}\n⏱ Expiration: Afaka 2 minitra")
            
        elif r == 2:
            # Raha SELL ilay izy
            self.status_label.config(text=f"✅ Analyse vita ho an'ny {pair}", fg="#4ef2d2")
            self.signal_label.config(text="🔴 SELL (PUT)", fg="#ff3333")
            self.time_label.config(text=f"Fotoana: {time_str}\n⏱ Expiration: Afaka 2 minitra")
            
        else:
            # Raha tsy misy signal mazava tsara eo amin'ny tsena
            self.status_label.config(text=f"⚠️ Analyse vita ho an'ny {pair}", fg="#ffcc00")
            self.signal_label.config(text="🚫 NO SIGNAL", fg="#a0a0a0")
            self.time_label.config(text="Tsy milamina ny tsena izao. Manandrama indray.")

# Mandefa ny Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ForexSignalBot(root)
    root.mainloop()
