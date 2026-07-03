import tkinter as tk
import pandas as pd
import os
from datetime import date


class WaterTracker:

    def __init__(self, username):

        self.username = username
        self.today = str(date.today())

        self.window = tk.Toplevel()
        self.window.title("Water Tracker")
        self.window.geometry("400x300")

        self.water_intake = 0

        tk.Label(
            self.window,
            text="💧 Water Tracker",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.label = tk.Label(
            self.window,
            text="Water Intake: 0 ml",
            font=("Arial", 14)
        )
        self.label.pack(pady=10)

        tk.Button(
            self.window,
            text="+250 ml",
            command=lambda: self.add_water(250)
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="+500 ml",
            command=lambda: self.add_water(500)
        ).pack(pady=5)

        self.load_existing_data()

    def load_existing_data(self):

        if not os.path.exists("data/history.csv"):
            return

        df = pd.read_csv("data/history.csv")

        df["Username"] = df["Username"].astype(str).str.strip()

        today_data = df[
            (df["Username"] == self.username) &
            (df["Date"] == self.today)
        ]

        if len(today_data) > 0:
            self.water_intake = today_data["Water"].sum()

        self.update_label()

    def add_water(self, amount):

        self.water_intake += amount
        self.update_label()
        self.save_water()

    def update_label(self):

        self.label.config(
            text=f"Water Intake: {self.water_intake} ml"
        )

    def save_water(self):

        df = pd.read_csv("data/history.csv")

        df["Username"] = df["Username"].astype(str).str.strip()

        # check if today's entry exists
        mask = (
            (df["Username"] == self.username) &
            (df["Date"] == self.today)
        )

        if mask.any():

            df.loc[mask, "Water"] = self.water_intake

        else:

            new_row = {
                "Date": self.today,
                "Username": self.username,
                "Calories": 0,
                "Protein": 0,
                "Carbs": 0,
                "Fat": 0,
                "Water": self.water_intake,
                "Exercise": 0
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv("data/history.csv", index=False)