import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry("800x800")
root.title("Login Page")

# Heading
heading = tk.Label(root, text="Login", font=("Arial", 16))
heading.pack(pady=10)

# Username input
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password input
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login button
def open_main_gui():
    subprocess.Popen(['python', 'main_gui.py'])  # Open main_gui.py in a new process
    

login_button = tk.Button(root, text="Login", padx=10, pady=5, command=open_main_gui)
login_button.pack(pady=10)

root.mainloop()
