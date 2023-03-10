import mysql.connector
import tkinter as tk
import pymysql.cursors
import subprocess

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='dr_cnn',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Create a Tkinter window
window = tk.Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
# window.geometry("1800x800")
window.title("Report List Page")

# Heading
heading = tk.Label(window, text="Past History of Patients", font=("Arial", 16), anchor="center")
heading.grid(row=0, column=0, columnspan=4, pady=10)

# ------------------------------------Open main_gui.py in a new process-----------------------------------
def open_main_gui():
    subprocess.Popen(['python', 'main_gui.py'])  # Open main_gui.py in a new process

# Create a list of column names
column_names = ['Patient ID', 'Name', 'Gender', 'Age', 'Date', 'Result']




# Add heading labels to the window
for j, column_name in enumerate(column_names):
    label = tk.Label(window, text=column_name, font=("Arial", 14, "bold"), relief=tk.RIDGE, width=20)
    label.grid(row=1, column=j, padx=5, pady=5)

button = tk.Button(window, text="Back to Main", padx=10, pady=5, command=open_main_gui)
button.grid(row=0, column=3, padx=5, pady=10, sticky="NE") 

cursor = connection.cursor()

sql = "SELECT * FROM records"
cursor.execute(sql)

# fetch all the rows from the result set
rows = cursor.fetchall()


# display the data in the tkinter window
for i in range(len(rows)):
    for j, column_name in enumerate(rows[i]):
        label = tk.Label(window, text=rows[i][column_name], relief=tk.RIDGE, width=20)
        label.grid(row=i+2, column=j) # start from row 2


# # display the data in the tkinter window
# for i in range(len(rows)):
#     for j, column_name in enumerate(rows[i]):
#         label = tk.Label(window, text=rows[i][column_name], relief=tk.RIDGE, width=20)
#         label.grid(row=i+1, column=j)

# close the cursor and database connection
cursor.close()
connection.close()

window.mainloop()
