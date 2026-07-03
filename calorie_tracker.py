import tkinter as tk
from tkinter import ttk
import pandas as pd
import csv
from datetime import datetime


class CalorieTracker:

    def __init__(self, username):

        self.username = username

        # Load food database
        self.food_data = pd.read_csv("data/foods.csv")

        # Totals
        self.total_calories = 0
        self.total_protein = 0
        self.total_carbs = 0
        self.total_fat = 0

        # Window
        self.window = tk.Toplevel()
        self.window.title("Food Tracker")
        self.window.geometry("600x500")

        # Title
        tk.Label(
            self.window,
            text="🍽 Food Tracker",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        # Dropdown
        self.food_combo = ttk.Combobox(
            self.window,
            values=self.food_data["Food"].tolist(),
            width=30
        )
        self.food_combo.pack(pady=10)

        # Button
        tk.Button(
            self.window,
            text="Add Food",
            command=self.add_food
        ).pack(pady=5)

        # Result label
        self.result = tk.Label(
            self.window,
            text="No Food Added Yet",
            font=("Arial", 14),
            justify="left"
        )
        self.result.pack(pady=20)

    def add_food(self):

        food = self.food_combo.get()

        row = self.food_data[self.food_data["Food"] == food]

        if len(row) == 0:
            self.result.config(text="❌ Invalid Food Selected")
            return

        # Get values
        cal = int(row.iloc[0]["Calories"])
        pro = float(row.iloc[0]["Protein"])
        carb = float(row.iloc[0]["Carbs"])
        fat = float(row.iloc[0]["Fat"])

        # Update totals
        self.total_calories += cal
        self.total_protein += pro
        self.total_carbs += carb
        self.total_fat += fat

        # Update UI
        self.result.config(
            text=f"""
📊 TODAY TOTALS

Calories : {self.total_calories} kcal
Protein  : {self.total_protein} g
Carbs    : {self.total_carbs} g
Fat      : {self.total_fat} g
"""
        )

        # Save to history.csv
        with open("data/history.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().date(),
                self.username,
                cal,
                pro,
                carb,
                fat,
                0,   # water (future use)
                0    # exercise (future use)
            ])