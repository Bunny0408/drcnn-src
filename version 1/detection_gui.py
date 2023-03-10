import main1
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import subprocess
import tkcalendar
from tkcalendar import DateEntry
import pymysql.cursors
import datetime



# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='dr_cnn',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


# Global variable to store the selected file path and result
selected_file_path = ""
result = ""


# Create a Tkinter window
window = tk.Tk()
window.geometry("800x800")
window.title("DR Detection Page")


# ------------------------------------Single Iamge Result-----------------------------------
def single_img():
    global selected_file_path
    global result


    if selected_file_path == "":
        text = "Please select an image file first."
        label = tk.Label(window, text=text)  
        label.pack()
        return

    

    report = main1.single_predict(selected_file_path)
    
    if report == 0:
        
        text = "Final Result is : No DR"
        result = "No DR"
        label = tk.Label(window, text=text, bg="green", fg="white")  
        label.pack() 

    elif report == 1:
        
        text = "Final Result is : Mild DR"
        result = "Mild DR"
        label = tk.Label(window, text=text, bg="green", fg="white")  
        label.pack()

    elif report == 2:   
        
        text = "Final Result is : Moderate DR"
        result = "Moderate DR"
        label = tk.Label(window, text=text, bg="red", fg="white")  
        label.pack()

    elif report == 3:
        
        text = "Final Result is : Severe DR"
        result = "Severe DR"
        label = tk.Label(window, text=text, bg="red", fg="white")  
        label.pack()

    else:
        
        text = "Final Result is : Proliferative DR"
        result = "Proliferative DR"
        label = tk.Label(window, text=text, bg="red", fg="white")  
        label.pack()


# ---------------------------------Accuracy and Confusion Matrix -------------------------------
# To call predict_all function in main and display cm and accuracy
def accuracu_cm():



    all = main1.predict_all()

    # Create a label to display the report
    label = tk.Label(window, text=all, justify="left")
    label.pack(padx=5, pady=10)



# ------------------------------------Open Iamge-----------------------------------
# Create a function to open an image file
def open_image():

    global selected_file_path

    # Get the file path from the user
    file_path = filedialog.askopenfilename(title="Open Image File",
                                           filetypes=(("PNG files", "*.png"),
                                                      ("JPEG files", "*.jpg"),
                                                      ("All files", "*.*")))
    selected_file_path = file_path
    
    # Display the selected image
    # image = Image.open(selected_file_path)
    # image = image.resize((100, 100))
    # photo = ImageTk.PhotoImage(image)
    # label_image.config(image=photo)
    # label_image.image = photo

    text = "Image Selected"
    label = tk.Label(window, text=text)  
    label.pack(padx=5, pady=10) 
    

    label = tk.Label(window, text=selected_file_path)  
    label.pack(padx=5, pady=10)
    

    # single_img(file_path)
    return selected_file_path

# ------------------------------------Sql Query-----------------------------------  

def query_for_db(pname, gender, age, date, result):
    with connection.cursor() as cursor:
        # Insert input text and result into the database
        sql = "INSERT INTO records (pname, gender, age, date, result) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (pname, gender, age, date, result))
        connection.commit()

# ------------------------------------for result button-----------------------------------
def both_functions():
    global result
    single_img()
    pname_val = pname.get("1.0", "end-1c")
    gender_val = gender.get()
    age_val = age_str.get("1.0", "end-1c")
    date_val = date_string
    query_for_db(pname_val, gender_val, age_val, date_val, result)
    
# ------------------------------------Open main_gui.py in a new process-----------------------------------
def open_main_gui():
    subprocess.Popen(['python', 'main_gui.py'])  # Open main_gui.py in a new process






button1 = tk.Button(window, text="Back", padx=10, pady=5, command=open_main_gui)
button1.pack(side=tk.RIGHT, padx=5, pady=10, anchor=tk.NE) 



# Heading
heading = tk.Label(window, text="Detection of Diabetic Retinopathy", font=("Arial", 16), anchor = "center")
heading.pack(pady=10)



# ------------------------Patient name
label = tk.Label(window, text="Patient Name: ", anchor="center")
label.pack()
pname = tk.Text(window, height=1, width=15)
pname.pack(padx=5, pady=10)

# ------------------------Gender Radio button
# Create a Label widget
label = tk.Label(window, text="Select Gender:", anchor="center")
label.pack(padx=5, pady=10)
# Create a StringVar to store the selected option
gender = tk.StringVar()
# Create a dropdown widget
dropdown = ttk.Combobox(window, textvariable=gender, values=["Select an option","Female", "Male", "other"])
dropdown.pack(padx=5, pady=10)
# Set a default value for the dropdown
dropdown.current(0)



# ------------------------Age
label = tk.Label(window, text="Age: ", anchor="center")
label.pack(padx=5, pady=10)
age_str = tk.Text(window, height=1, width=5)
age_str.pack(padx=5, pady=10)

# age = age_str.get("1.0", "end-1c") 


# ------------------------create a label for the date picker widget
date_label = tk.Label(window, text='Select a date: (DD/MM/YYYY)')
date_label.pack(pady=10)

# create a date picker widget
date_entry = DateEntry(window, width=12, background='darkblue',
                       foreground='white', borderwidth=2,
                       date_pattern='dd/mm/yyyy')

# set the current date as the default value for the date picker
today = datetime.date.today()
date_entry.set_date(today)

# set the format of the displayed date in the widget
date_entry.config(date_pattern='dd/mm/yyyy')

date_entry.pack(pady=10)

selected_date = date_entry.get_date()

date_string = selected_date.strftime('%d/%m/%Y')



# -----------------------Create a button to open an image file
button_open_image = tk.Button(window, text="Open Image", command=open_image)
button_open_image.pack(padx=5, pady=10)

# Create a label to display the loaded image


label = tk.Label(window, text=selected_file_path)  
label.pack(padx=5, pady=10)




# Create a button widget for singleimage
button = tk.Button(window, text="Results", command=both_functions)
button.pack(padx=5, pady=10)

# # Create a button widget for accuracy and Matrix
# button = tk.Button(window, text="Accuracy and confusion Matrix", command=accuracu_cm)
# button.pack()

# Run the Tkinter event loop
window.mainloop()

