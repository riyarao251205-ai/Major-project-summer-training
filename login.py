import tkinter as tk
from tkinter import messagebox
import csv
import os


class Login:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Smart Calories Tracker")
        self.root.geometry("700x500")
        self.root.configure(bg="#F4F7FA")
        self.root.resizable(False, False)

        # ================= CARD ================= #

        card = tk.Frame(
            self.root,
            bg="white",
            padx=40,
            pady=30,
            relief="solid",
            bd=1
        )

        card.place(relx=0.5, rely=0.5, anchor="center")

        # ================= TITLE ================= #

        tk.Label(
            card,
            text="🍎 Smart Calories Tracker",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg="#2E3A59"
        ).pack()

        tk.Label(
            card,
            text="Track • Analyze • Stay Healthy",
            font=("Segoe UI", 10),
            bg="white",
            fg="gray"
        ).pack(pady=(0, 25))

        # ================= USERNAME ================= #

        tk.Label(
            card,
            text="👤 Username",
            bg="white",
            fg="#333333",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w")

        self.username = tk.Entry(
            card,
            width=32,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1
        )

        self.username.pack(ipady=6, pady=(5, 15))

        # ================= PASSWORD ================= #

        tk.Label(
            card,
            text="🔒 Password",
            bg="white",
            fg="#333333",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w")

        self.password = tk.Entry(
            card,
            width=32,
            show="*",
            font=("Segoe UI", 11),
            relief="solid",
            bd=1
        )

        self.password.pack(ipady=6, pady=(5, 25))

        # ================= BUTTONS ================= #

        login_btn = tk.Button(
            card,
            text="Login",
            command=self.login,
            bg="#4F8EF7",
            fg="white",
            activebackground="#357AE8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            font=("Segoe UI", 11, "bold")
        )

        login_btn.pack(pady=5)

        register_btn = tk.Button(
            card,
            text="Register",
            command=self.register,
            bg="#4CAF50",
            fg="white",
            activebackground="#3F9142",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            font=("Segoe UI", 11, "bold")
        )

        register_btn.pack(pady=10)

        # ================= FOOTER ================= #

        tk.Label(
            card,
            text="Developed using Python & Tkinter",
            bg="white",
            fg="gray",
            font=("Segoe UI", 9)
        ).pack(pady=(20, 0))

    # ======================================================

    def register(self):

        user = self.username.get().strip()
        pwd = self.password.get().strip()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "Fill all fields")
            return

        if not os.path.exists("data"):
            os.makedirs("data")

        file_exists = os.path.exists("data/users.csv")

        with open("data/users.csv", "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Username", "Password"])

            writer.writerow([user, pwd])

        messagebox.showinfo("Success", "Registration Successful")

    # ======================================================

    def login(self):

        user = self.username.get().strip()
        pwd = self.password.get().strip()

        if not os.path.exists("data/users.csv"):
            messagebox.showerror("Error", "No users registered.")
            return

        with open("data/users.csv", "r") as file:

            reader = csv.reader(file)

            next(reader, None)

            for row in reader:

                if row[0] == user and row[1] == pwd:

                    messagebox.showinfo("Success", "Login Successful")

                    self.root.destroy()

                    from dashboard import Dashboard

                    Dashboard(user)

                    return

        messagebox.showerror("Error", "Invalid Username or Password")

    # ======================================================

    def run(self):
        self.root.mainloop()