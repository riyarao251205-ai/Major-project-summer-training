import tkinter as tk
from tkinter import messagebox


class BMI:

    def __init__(self, username):

        self.username = username

        self.window = tk.Toplevel()
        self.window.title("BMI Calculator")
        self.window.geometry("400x300")

        tk.Label(
            self.window,
            text="📏 BMI Calculator",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        tk.Label(self.window, text="Height (meters)").pack()
        self.height_entry = tk.Entry(self.window)
        self.height_entry.pack(pady=5)

        tk.Label(self.window, text="Weight (kg)").pack()
        self.weight_entry = tk.Entry(self.window)
        self.weight_entry.pack(pady=5)

        tk.Button(
            self.window,
            text="Calculate BMI",
            command=self.calculate_bmi
        ).pack(pady=10)

        self.result = tk.Label(
            self.window,
            text="",
            font=("Arial", 14, "bold")
        )
        self.result.pack(pady=10)

    def calculate_bmi(self):

        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 24.9:
                category = "Normal"
            elif bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"

            self.result.config(
                text=f"BMI: {round(bmi,2)} ({category})"
            )

        except:
            messagebox.showerror("Error", "Enter valid numbers")