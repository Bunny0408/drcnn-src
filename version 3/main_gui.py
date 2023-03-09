import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Main page")

# Heading
heading = tk.Label(root, text="Welcome to DR Detection", font=("Arial", 16))
heading.pack(pady=10)

# Buttons
def open_detection_gui():
    subprocess.Popen(['python', 'detection_gui.py'])  # Open detection_gui.py in a new process

button1 = tk.Button(root, text="DR Detection", padx=10, pady=5, command=open_detection_gui)
button1.pack(side=tk.LEFT, padx=5, pady=10)

button2 = tk.Button(root, text="Past Records", padx=10, pady=5)
button2.pack(side=tk.RIGHT, padx=5, pady=10)

def open_login_gui():
    subprocess.Popen(['python', 'login_gui.py'])  # Open login_gui.py in a new process

button3 = tk.Button(root, text="Back to login", padx=10, pady=5, command= open_login_gui)
button3.pack(side=tk.RIGHT, padx=5, pady=10, anchor=tk.NE)

root.mainloop()
