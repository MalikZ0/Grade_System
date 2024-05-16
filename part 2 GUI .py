import tkinter as tk
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook

# Global dictionary to store user details
user_details = {}

def get_credits(credit_entry):
    while True:
        try:
            credit_input = credit_entry.get()
            if credit_input == "":
                return 0
            credit = int(credit_input)
            if credit < 0 or credit > 120:
                messagebox.showerror("Error", "Credits should be between 0 and 120")
                return None
            return credit
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
            return None

def calculate_outcome():
    user_id = user_id_entry.get().strip()
    if not user_id:
        messagebox.showerror("Error", "Please enter User ID")
        return
    if len(user_id) != 8:
        messagebox.showerror("Required '7' numbers starting with 'w' letter")
        return
        
    pass_credits = get_credits(pass_entry)
    defer_credits = get_credits(defer_entry)
    fail_credits = get_credits(fail_entry)

    if pass_credits is None or defer_credits is None or fail_credits is None:
        messagebox.showerror("Error", "Please enter Credits")
        return

    total_credits = pass_credits + defer_credits + fail_credits
    total_label.config(text=f": {total_credits}", font=('Arial', 12, 'bold'), fg='blue')

    if total_credits != 120:
        messagebox.showerror("Error", "Total credits should be 120")
        return

    result = ""
    if pass_credits == 120:
        result = "Progress"
        result_label.config(text=result, font=('Arial', 12, 'bold'), fg='green')
    elif pass_credits == 100:
        result = "Progress (module trailer)"
        result_label.config(text=result, font=('Arial', 12, 'bold'), fg='blue')
    elif (pass_credits == 80) or (pass_credits == 60) or (pass_credits == 40 and defer_credits >= 20) or \
            (pass_credits == 20 and defer_credits >= 40) or (pass_credits == 0 and defer_credits >= 60):
        result = "Module retriever"
        result_label.config(text=result, font=('Arial', 12, 'bold'), fg='orange')
    else:
        result = "Exclude"
        result_label.config(text=result, font=('Arial', 12, 'bold'), fg='red')

    # Storing user details
    user_details[user_id] = {"Result": result,
                              "Pass Credits": pass_credits,
                              "Defer Credits": defer_credits,
                              "Fail Credits": fail_credits}

def clear_entries():
    user_id_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    defer_entry.delete(0, tk.END)
    fail_entry.delete(0, tk.END)
    result_label.config(text="")
    total_label.config(text="")
    user_details.clear()

def save_to_excel():
    try:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Student Grades"

        ws.append(["ID", "Result", "Pass Credits", "Defer Credits", "Fail Credits"])
        for user_id, details in user_details.items():
            ws.append([user_id] + [details[key] for key in ["Result", "Pass Credits", "Defer Credits", "Fail Credits"]])

        wb.save("students_grades.xlsx")
        messagebox.showinfo("Success", "Data saved to students_grades.xlsx")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("500x450")

# Labels
user_id_label = tk.Label(root, text="User ID:", font=('Arial', 12))
cred1 = tk.Label(root, text="PASS credits:", font=('Arial', 12))
cred2 = tk.Label(root, text="DEFER credits:", font=('Arial', 12))
cred3 = tk.Label(root, text="FAIL credits:", font=('Arial', 12))
tot = tk.Label(root, text="Total:", font=('Arial', 12, 'bold'))
result = tk.Label(root, text="Result:", font=('Arial', 12, 'bold'))

# Entries
user_id_entry = tk.Entry(root)
pass_entry = tk.Entry(root)
defer_entry = tk.Entry(root)
fail_entry = tk.Entry(root)

# Total Label
total_label = tk.Label(root, text="", font=('Arial', 12, 'bold'))

# Result Label
result_label = tk.Label(root, text="", font=('Arial', 12, 'bold'))

# Buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate_outcome, bd=10)
clear_button = tk.Button(root, text="Clear", command=clear_entries, bd=10)
save_button = tk.Button(root, text="Save", command=save_to_excel, bd=10)

# Placing
user_id_label.place(x=50, y=20)
cred1.place(x=50, y=70)
cred2.place(x=50, y=120)
cred3.place(x=50, y=170)
tot.place(x=50, y=220)
result.place(x=50, y=260)
user_id_entry.place(x=200, y=20)
pass_entry.place(x=200, y=70)
defer_entry.place(x=200, y=120)
fail_entry.place(x=200, y=170)
total_label.place(x=200, y=220)
result_label.place(x=200, y=260)
calculate_button.place(x=100, y=300)
clear_button.place(x=200, y=300)
save_button.place(x=300, y=300)

root.mainloop()