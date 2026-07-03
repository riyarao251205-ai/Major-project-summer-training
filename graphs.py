import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt


class Graphs:

    def __init__(self, username):

        self.username = username

        self.window = tk.Toplevel()
        self.window.title("Analytics Graphs")
        self.window.geometry("400x250")

        tk.Label(
            self.window,
            text="📈 Progress Graphs",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=15)

        tk.Button(
            self.window,
            text="📊 Calories Graph",
            width=25,
            command=self.calories_graph
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="💧 Water Graph",
            width=25,
            command=self.water_graph
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="🏃 Exercise Graph",
            width=25,
            command=self.exercise_graph
        ).pack(pady=5)

    # ================= LOAD DATA ================= #

    def load_data(self):

        df = pd.read_csv("data/history.csv")

        df["Username"] = df["Username"].astype(str).str.strip()

        # Safe date conversion
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        df = df.dropna(subset=["Date"])

        # Keep only this user
        return df[df["Username"] == self.username]

    # ================= CALORIES GRAPH ================= #

    def calories_graph(self):

        df = self.load_data()

        if df.empty:
            print("No data found")
            return

        grouped = df.groupby(df["Date"].dt.date)["Calories"].sum().sort_index()

        plt.figure()
        plt.plot(grouped.index, grouped.values, marker="o")

        plt.title("Calories Trend")
        plt.xlabel("Date")
        plt.ylabel("Calories")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # ================= WATER GRAPH ================= #

    def water_graph(self):

        df = self.load_data()

        if df.empty:
            print("No data found")
            return

        grouped = df.groupby(df["Date"].dt.date)["Water"].sum().sort_index()

        plt.figure()
        plt.plot(grouped.index, grouped.values, marker="o")

        plt.title("Water Intake Trend")
        plt.xlabel("Date")
        plt.ylabel("Water (ml)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # ================= EXERCISE GRAPH ================= #

    def exercise_graph(self):

        df = self.load_data()

        if df.empty:
            print("No data found")
            return

        grouped = df.groupby(df["Date"].dt.date)["Exercise"].sum().sort_index()

        plt.figure()
        plt.plot(grouped.index, grouped.values, marker="o")

        plt.title("Exercise Burn Trend")
        plt.xlabel("Date")
        plt.ylabel("Calories Burned")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()