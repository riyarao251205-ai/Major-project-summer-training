import tkinter as tk
import pandas as pd
import csv
from datetime import date


class ExerciseTracker:

    def __init__(self, username):

        self.username = username
        self.today = str(date.today())

        self.window = tk.Toplevel()
        self.window.title("Exercise Tracker")
        self.window.geometry("400x350")

        self.calories_burned = 0

        tk.Label(
            self.window,
            text="🏃 Exercise Tracker",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.label = tk.Label(
            self.window,
            text="Calories Burned: 0 kcal",
            font=("Arial", 14)
        )
        self.label.pack(pady=10)

        tk.Button(
            self.window,
            text="🚶 Walking (100 kcal)",
            command=lambda: self.add_exercise(100)
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="🏃 Running (250 kcal)",
            command=lambda: self.add_exercise(250)
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="🚴 Cycling (200 kcal)",
            command=lambda: self.add_exercise(200)
        ).pack(pady=5)

        self.load_data()

    def load_data(self):

        try:
            df = pd.read_csv("data/history.csv")

            df["Username"] = df["Username"].astype(str).str.strip()

            today_data = df[
                (df["Username"] == self.username) &
                (df["Date"] == self.today)
            ]

            if len(today_data) > 0:
                self.calories_burned = today_data["Exercise"].sum()

            self.update_label()

        except:
            pass

    def add_exercise(self, calories):

        self.calories_burned += calories
        self.update_label()
        self.save_data()

    def update_label(self):

        self.label.config(
            text=f"Calories Burned: {self.calories_burned} kcal"
        )

    def save_data(self):

        df = pd.read_csv("data/history.csv")

        df["Username"] = df["Username"].astype(str).str.strip()

        mask = (
            (df["Username"] == self.username) &
            (df["Date"] == self.today)
        )

        if mask.any():

            df.loc[mask, "Exercise"] = self.calories_burned

        else:

            new_row = {
                "Date": self.today,
                "Username": self.username,
                "Calories": 0,
                "Protein": 0,
                "Carbs": 0,
                "Fat": 0,
                "Water": 0,
                "Exercise": self.calories_burned
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv("data/history.csv", index=False)