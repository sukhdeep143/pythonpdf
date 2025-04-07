import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from calendar import monthrange

def calculate_age(birth_date):
    today = datetime.now()
    delta = today - birth_date

    # Calculate years, months, and days
    age_in_years = today.year - birth_date.year
    age_in_months = today.month - birth_date.month
    age_in_days = today.day - birth_date.day

    # Adjust for negative months or days
    if age_in_days < 0:
        age_in_months -= 1
        previous_month = (today.month - 1) if today.month > 1 else 12
        previous_year = today.year if today.month > 1 else today.year - 1
        days_in_previous_month = monthrange(previous_year, previous_month)[1]
        age_in_days += days_in_previous_month

    if age_in_months < 0:
        age_in_years -= 1
        age_in_months += 12

    # Calculate total minutes and seconds
    age_in_minutes = delta.total_seconds() // 60
    age_in_seconds = delta.total_seconds()

    return age_in_years, age_in_months, age_in_days, int(age_in_minutes), int(age_in_seconds)

def show_age():
    dob_input = dob_entry.get()
    try:
        birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days, minutes, seconds = calculate_age(birth_date)
        result = (
            f"You are {years} years, {months} months, {days} days, "
            f"{minutes} minutes, and {seconds} seconds old."
        )
        messagebox.showinfo("Age Calculator Result", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD format.")

# Create the GUI
root = tk.Tk()
root.title("Age Calculator")

# Input label and entry
tk.Label(root, text="Enter your date of birth (YYYY-MM-DD):").pack(pady=10)
dob_entry = tk.Entry(root, width=20)
dob_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Age", command=show_age)
calculate_button.pack(pady=20)

# Run the application
root.mainloop()