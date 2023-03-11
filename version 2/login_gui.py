import tkinter as tk
from tkinter import messagebox
import subprocess

window = tk.Tk()
window.geometry("800x800")
window.title("Login Page")

# Heading
heading = tk.Label(window, text="Login", font=("Arial", 16))
heading.pack(pady=10)

# Username input
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack(pady=5)

# Password input
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

# Login button
def open_main_gui():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        window.destroy()  # Destroy the login window

        # Create and display the main window
        import main_gui
        
        main_window = tk.Tk()
        main_window.geometry("800x800")
        main_window.title("Main Page")

        # Add widgets and functionality to the main window here
        # ...

        main_window.mainloop()
    else:
        messagebox.showerror("Error", "Invalid username or password")



login_button = tk.Button(window, text="Login", padx=10, pady=5, command=open_main_gui)
login_button.pack(pady=10)

window.mainloop()