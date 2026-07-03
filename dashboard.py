import tkinter as tk
from tkinter import ttk
import pandas as pd
from calorie_tracker import CalorieTracker


class Dashboard:

    def __init__(self, username):

        self.username = username
        self.goal = 2000

        self.root = tk.Tk()
        self.root.title("Smart Health & Calorie Tracker")
        self.root.geometry("950x750")
        self.root.configure(bg="#F4F7FA")
        self.root.resizable(False, False)

        # ================= HEADER ================= #
        header = tk.Frame(self.root, bg="#4F8EF7", height=70)
        header.pack(fill="x")

        tk.Label(
            header,
            text="🍎 Smart Calories Tracker",
            bg="#4F8EF7",
            fg="white",
            font=("Segoe UI", 18, "bold")
        ).pack(side="left", padx=10, pady=15)

        tk.Label(
            header,
            text=f"Welcome, {username}",
            bg="#4F8EF7",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(side="right", padx=10)

        # ================= TITLE ================= #
        tk.Label(
            self.root,
            text="Today's Health Summary",
            bg="#F4F7FA",
            fg="#2E3A59",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=8)

        # ================= SUMMARY CARDS ================= #
        card_frame = tk.Frame(self.root, bg="#F4F7FA")
        card_frame.pack(pady=5)

        def create_card(parent, title, color):
            frame = tk.Frame(parent, bg="white", width=180, height=90, bd=1, relief="solid")
            frame.pack_propagate(False)

            tk.Label(
                frame,
                text=title,
                bg="white",
                fg="gray",
                font=("Segoe UI", 10, "bold")
            ).pack(pady=(10, 0))

            label = tk.Label(
                frame,
                text="0",
                bg="white",
                fg=color,
                font=("Segoe UI", 14, "bold")
            )
            label.pack()

            return frame, label

        row1 = tk.Frame(card_frame, bg="#F4F7FA")
        row1.pack()

        self.cal_card, self.cal_value = create_card(row1, "Calories", "#4F8EF7")
        self.cal_card.pack(side="left", padx=10)

        self.water_card, self.water_value = create_card(row1, "Water", "#00A8E8")
        self.water_card.pack(side="left", padx=10)

        row2 = tk.Frame(card_frame, bg="#F4F7FA")
        row2.pack(pady=10)

        self.ex_card, self.ex_value = create_card(row2, "Exercise", "#FF6B6B")
        self.ex_card.pack(side="left", padx=10)

        self.net_card, self.net_value = create_card(row2, "Net", "#2ECC71")
        self.net_card.pack(side="left", padx=10)

        # ================= PROGRESS BAR ================= #
        tk.Label(
            self.root,
            text="Daily Goal Progress",
            bg="#F4F7FA",
            font=("Segoe UI", 11, "bold")
        ).pack(pady=(10, 5))

        self.progress_bar = ttk.Progressbar(
            self.root,
            length=420,
            mode="determinate"
        )
        self.progress_bar.pack()

        self.progress = tk.Label(
            self.root,
            text="0%",
            bg="#F4F7FA",
            font=("Segoe UI", 10)
        )
        self.progress.pack(pady=5)

        # ================= BUTTON FRAME ================= #
        center_frame = tk.Frame(self.root, bg="#F4F7FA")
        center_frame.pack(fill="both",expand=True)

# BUTTON FRAME INSIDE CENTER
        button_frame = tk.Frame(center_frame, bg="#F4F7FA", width=600)
        button_frame.pack(pady=8)
        button_frame.pack_propagate(False)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        

        btn_style = {
            "width": 18,
            "height": 2,
            "font": ("Segoe UI", 11, "bold"),
            "relief": "flat",
            "bg": "#4F8EF7",
            "fg": "white",
            "activebackground": "#357AE8",
            "cursor": "hand2"
        }
        
        tk.Button(button_frame, text="🍽 Food", command=self.open_food_tracker, **btn_style).grid(row=0, column=0, padx=15, pady=5, sticky="n")
        tk.Button(button_frame, text="💧 Water", command=self.open_water_tracker, **btn_style).grid(row=0, column=1, padx=15, pady=5, sticky="n")

        tk.Button(button_frame, text="🏃 Exercise", command=self.open_exercise_tracker, **btn_style).grid(row=1, column=0, padx=15, pady=5, sticky="n")
        tk.Button(button_frame, text="📏 BMI", command=self.open_bmi, **btn_style).grid(row=1, column=1, padx=15, pady=5, sticky="n")

        tk.Button(button_frame, text="📊 Reports", command=self.open_reports, **btn_style).grid(row=2, column=0, padx=15, pady=5, sticky="n")
        tk.Button(button_frame, text="📈 Graphs", command=self.open_graphs, **btn_style).grid(row=2, column=1, padx=15, pady=5, sticky="n")

        tk.Button(
            button_frame,
            text="🚪 Logout",
            command=self.root.destroy,
            bg="#E74C3C",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2"
        ).grid(row=3, column=0, columnspan=2, padx=10, pady=(15,5),sticky="n")


        # ================= START LOOP ================= #
        self.update_dashboard()
        self.root.mainloop()

    # ================= OPEN MODULES ================= #
    def open_food_tracker(self):
        CalorieTracker(self.username)

    def open_water_tracker(self):
        from water import WaterTracker
        WaterTracker(self.username)

    def open_exercise_tracker(self):
        from exercise import ExerciseTracker
        ExerciseTracker(self.username)

    def open_reports(self):
        from reports import Reports
        Reports(self.username)

    def open_bmi(self):
        from bmi import BMI
        BMI(self.username)

    def open_graphs(self):
        from graphs import Graphs
        Graphs(self.username)

    # ================= LIVE UPDATE ================= #
    def update_dashboard(self):

        try:
            df = pd.read_csv("data/history.csv")
            df["Username"] = df["Username"].astype(str).str.strip()
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date

            today = pd.to_datetime("today").date()

            today_data = df[
                (df["Username"] == self.username) &
                (df["Date"] == today)
            ]

            if not today_data.empty:
                calories = today_data["Calories"].sum()
                water = today_data["Water"].sum()
                exercise = today_data["Exercise"].sum()
            else:
                calories = water = exercise = 0

            net = calories - exercise
            percent = min((calories / self.goal) * 100 if calories else 0, 100)

            # update cards
            self.cal_value.config(text=f"{int(calories)} kcal")
            self.water_value.config(text=f"{int(water)} ml")
            self.ex_value.config(text=f"{int(exercise)} kcal")
            self.net_value.config(text=f"{int(net)} kcal")

            self.progress_bar["value"] = percent
            self.progress.config(text=f"{int(percent)}% of daily goal")

        except Exception as e:
            print("Error:", e)

        self.root.after(2000, self.update_dashboard)