import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )


root = tk.Tk()
root.title("Login Form")
root.geometry("400x350")
root.configure(bg="#1E1E2E")

title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Segoe UI", 22, "bold"),
    bg="#1E1E2E",
    fg="#89B4FA"
)
title_label.pack(pady=15)

username_label = tk.Label(
    root,
    text="Username",
    font=("Segoe UI", 11, "bold"),
    bg="#1E1E2E",
    fg="#CDD6F4"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Segoe UI", 12),
    width=25,
    bg="#313244",
    fg="#FFFFFF",
    insertbackground="white"
)
username_entry.pack(pady=5)

password_label = tk.Label(
    root,
    text="Password",
    font=("Segoe UI", 11, "bold"),
    bg="#1E1E2E",
    fg="#CDD6F4"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Segoe UI", 12),
    width=25,
    show="*",
    bg="#313244",
    fg="#FFFFFF",
    insertbackground="white"
)
password_entry.pack(pady=5)

login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Segoe UI", 12, "bold"),
    bg="#A6E3A1",
    fg="#11111B",
    width=20,
    command=login
)
login_button.pack(pady=20)

root.mainloop()
