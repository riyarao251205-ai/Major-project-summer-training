# 🍎 Smart Health & Calorie Tracker

A desktop application developed using **Python** and **Tkinter** that helps users monitor their daily calorie intake, water consumption, exercise, BMI, and health progress. The application stores user data in CSV files and provides reports and graphical analysis.

---

## 📌 Project Overview

The Smart Health & Calorie Tracker is a GUI-based desktop application designed to encourage healthy lifestyle habits. Users can register, log in, record food intake, water consumption, exercise activities, calculate BMI, and monitor daily progress through an interactive dashboard.

The application uses **Tkinter** for the graphical interface and **Pandas** for data management.

---

## ✨ Features

- 🔐 User Registration & Login
- 🍽 Food Calorie Tracking
- 💧 Water Intake Tracking
- 🏃 Exercise Tracker
- 📏 BMI Calculator
- 📊 Daily Health Dashboard
- 📈 Progress Graphs
- 📄 Report Generation
- 💾 CSV-based Data Storage
- 🎨 Modern Tkinter User Interface

---

# 📂 Project Structure

```
Smart-Calorie-Tracker/
│
├── main.py
├── login.py
├── dashboard.py
├── calorie_tracker.py
├── water.py
├── exercise.py
├── bmi.py
├── reports.py
├── graphs.py
│
├── data/
│   ├── foods.csv
│   ├── users.csv
│   └── history.csv
│
├── assets/
│
├── README.md
│
└── requirements.txt
```

---

# 🛠 Technologies Used

- Python 3.x
- Tkinter
- Pandas
- Matplotlib
- CSV
- Datetime

---

# 📦 Python Libraries

Install all required libraries using:

```bash
pip install pandas matplotlib
```

Tkinter is included with Python.

---


```



Run the application

```bash
python main.py
```

---

# 📋 Modules Description

## 1. Login Module

- User Registration
- User Login
- Authentication
- Opens Dashboard after successful login

---

## 2. Dashboard

Displays

- Today's Calories
- Water Intake
- Exercise
- Net Calories
- Goal Progress
- Buttons for all modules

---

## 3. Food Tracker

Allows users to

- Select food items
- View calories
- View Protein
- View Carbohydrates
- View Fat
- Save data into history.csv

---

## 4. Water Tracker

Allows users to

- Add water intake
- Save daily water consumption
- Display today's total water intake

---

## 5. Exercise Tracker

Supports

- Walking
- Running
- Cycling

Automatically updates burned calories.

---

## 6. BMI Calculator

Calculates

BMI = Weight / Height²

Displays

- Underweight
- Normal
- Overweight
- Obese

---

## 7. Reports

Shows complete daily report including

- Calories
- Water
- Exercise
- Net Calories

---

## 8. Graphs

Displays

- Calories Trend
- Water Intake Trend
- Exercise Trend

using Matplotlib.

---

# 💾 Data Storage

The application stores data in CSV files.

### users.csv

```
Username,Password
```

Stores registered users.

---

### foods.csv

Contains

- Food Name
- Calories
- Protein
- Carbs
- Fat

---

### history.csv

Stores

- Date
- Username
- Calories
- Protein
- Carbs
- Fat
- Water
- Exercise

---

# 📊 Application Workflow

```
Start
   │
   ▼
Login/Register
   │
   ▼
Dashboard
   │
   ├── Food Tracker
   ├── Water Tracker
   ├── Exercise Tracker
   ├── BMI Calculator
   ├── Reports
   └── Graphs
   │
   ▼
history.csv Updated
   │
   ▼
Dashboard Refreshes Automatically
```

---

# 🎯 Future Improvements

- SQLite Database
- Nutrition API Integration
- User Profile
- Weekly Reports
- Monthly Reports
- AI Meal Suggestions
- Dark Mode
- Reminder Notifications
- Export Reports to PDF
- Email Reports

---

