import customtkinter as ctk
from tkinter import messagebox
from plyer import notification
import requests
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

class BitcoinTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("💰 Bitcoin Price Tracker")
        master.geometry("600x450")
        master.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.main_frame = ctk.CTkFrame(master, corner_radius=20)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.main_frame, text="Bitcoin Tracker", font=("Segoe UI", 22, "bold"))
        self.title_label.pack(pady=(10, 20))

        self.price_card = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.price_card.pack(pady=10, padx=10, fill="x")

        self.price_label = ctk.CTkLabel(self.price_card, text="Current Price: $0.00", font=("Segoe UI", 18))
        self.price_label.pack(pady=15)

        self.button_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.button_frame.pack(pady=10)

        self.fetch_button = ctk.CTkButton(self.button_frame, text="🔄 Get Latest Price", width=200, command=self.get_price)
        self.fetch_button.grid(row=0, column=0, padx=10, pady=10)

        self.save_button = ctk.CTkButton(self.button_frame, text="💾 Save to Database", width=200, command=self.save_price)
        self.save_button.grid(row=1, column=0, padx=10, pady=10)

        self.history_button = ctk.CTkButton(self.button_frame, text="📜 Price History", width=200, command=self.show_history)
        self.history_button.grid(row=2, column=0, padx=10, pady=10)

        self.plot_button = ctk.CTkButton(self.button_frame, text="📈 Show Chart", width=200, command=self.plot_chart)
        self.plot_button.grid(row=3, column=0, padx=10, pady=10)

        self.current_price = None
        self.setup_database()

    def setup_database(self):
        self.conn = sqlite3.connect("bitcoin_prices.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                price_usd REAL,
                timestamp TEXT)""")
        self.conn.commit()

    def get_price(self):
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
            response = requests.get(url)
            data = response.json()
            self.current_price = float(data["bitcoin"]["usd"])
            self.price_label.configure(text=f"Current Price: ${self.current_price:,.2f}")

            notification.notify(
                title="Bitcoin Price Update",
                message=f"BTC Price is now ${self.current_price:,.2f}",
                timeout=5)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch price.\n{e}")

    def save_price(self):
        if self.current_price is None:
            messagebox.showwarning("Warning", "Please fetch the price first.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO prices (price_usd, timestamp) VALUES (?, ?)",
                            (self.current_price, timestamp))
        self.conn.commit()
        messagebox.showinfo("Saved", f"Price ${self.current_price} saved at {timestamp}")

    def show_history(self):
        history_window = ctk.CTkToplevel(self.master)
        history_window.title("📜 Price History")
        history_window.geometry("420x300")

        listbox = ctk.CTkTextbox(history_window, font=("Consolas", 12))
        listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.cursor.execute("SELECT price_usd, timestamp FROM prices ORDER BY timestamp DESC")
        rows = self.cursor.fetchall()

        for price, timestamp in rows:
            listbox.insert("end", f"${price:.2f}  -  {timestamp}\n")

    def plot_chart(self):
        self.cursor.execute("SELECT price_usd, timestamp FROM prices ORDER BY timestamp")
        rows = self.cursor.fetchall()
        if not rows:
            messagebox.showinfo("No Data", "No price data available.")
            return

        prices = [row[0] for row in rows]
        timestamps = [row[1][-8:] for row in rows]

        plt.figure(figsize=(8, 5))
        plt.plot(timestamps, prices, marker='o', linestyle='-', color='green')
        plt.xticks(rotation=45)
        plt.title("Bitcoin Price Over Time")
        plt.xlabel("Time")
        plt.ylabel("Price (USD)")
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    app = ctk.CTk()
    BitcoinTrackerApp(app)
    app.mainloop()
