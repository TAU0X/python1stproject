import tkinter as tk
from tkinter import messagebox
import os
file_path= os.path.abspath("skills.txt")

def load_skills(file_path):
    skills = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                skills.append(line.strip().lower())
    except FileNotFoundError:
        messagebox.showerror("Error", "Skills file not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return skills

def check_skills():
    skill = skill_entry.get().lower()
    try:
        if skill in skills:
            messagebox.showinfo("Result", f"{skill.capitalize()} is a required skill!")
        else:
            messagebox.showwarning("Result", f"{skill.capitalize()} is not listed as a required skill.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

file_path = "skills.txt"
skills = load_skills(file_path)

app = tk.Tk()
app.title("Skill Checker")

tk.Label(app, text="Enter the programming skill you are looking for:").pack(pady=5)
skill_entry = tk.Entry(app, width=30)
skill_entry.pack(pady=5)

check_button = tk.Button(app, text="Check Skill", command=check_skills)
check_button.pack(pady=10)

app.mainloop()