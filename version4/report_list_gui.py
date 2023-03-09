import mysql.connector
import tkinter as tk
import pymysql.cursors

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
window.geometry("800x800")
window.title("DRCNN")

# Heading
heading = tk.Label(window, text="Past History of patients", font=("Arial", 16), anchor="center")
heading.grid(row=0, column=0, columnspan=4, pady=10)

cursor = connection.cursor()

sql = "SELECT * FROM records"
cursor.execute(sql)

# fetch all the rows from the result set
rows = cursor.fetchall()

# display the data in the tkinter window
for i in range(len(rows)):
    for j, column_name in enumerate(rows[i]):
        label = tk.Label(window, text=rows[i][column_name], relief=tk.RIDGE, width=20)
        label.grid(row=i+1, column=j)

# close the cursor and database connection
cursor.close()
connection.close()

window.mainloop()
