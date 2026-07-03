import tkinter as tk
import pandas as pd


class Reports:

    def __init__(self, username):

        self.username = username

        self.window = tk.Toplevel()
        self.window.title("Reports")
        self.window.geometry("600x400")

        tk.Label(
            self.window,
            text="📊 Weekly Report",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.text = tk.Text(self.window, width=70, height=20)
        self.text.pack()

        self.load_report()

    def load_report(self):

        df = pd.read_csv("data/history.csv")

        df["Username"] = df["Username"].astype(str).str.strip()

        user_data = df[df["Username"] == self.username]

        if len(user_data) == 0:
            self.text.insert(tk.END, "No data available")
            return

        summary = user_data.groupby("Date").sum(numeric_only=True)

        self.text.insert(tk.END, str(summary))