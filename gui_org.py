# Gui code 2
import main1
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Create a Tkinter window
window = tk.Tk()
window.geometry("400x500")
window.title("DRCNN Image")

# Create a function to open an image file
def open_image():
    # Get the file path from the user
    file_path = filedialog.askopenfilename(title="Open Image File",
                                           filetypes=(("PNG files", "*.png"),
                                                      ("JPEG files", "*.jpg"),
                                                      ("All files", "*.*")))
    # Load the image file using Pillow
    image = str(file_path)
    # # Convert the image to Tkinter-compatible format
    # image_tk = ImageTk.PhotoImage(image)
    # Display the image in the GUI

    report = main1.single_predict(image)
    
    if report == 0:
        # print('Final Result is : No DR')
        text = "Final Result is : No DR"
        label = tk.Label(window, text=text)  
        label.pack() 
    elif report == 1:
        # print('Final Result is : Mild DR')
        text = "Final Result is : Mild DR"
        label = tk.Label(window, text=text)  
        label.pack()
    elif report == 2:
        # print('Final Result is : Moderate DR')
        text = "Final Result is : Moderate DR"
        label = tk.Label(window, text=text)  
        label.pack()
    elif report == 3:
        # print('Final Result is : Severe DR')
        text = "Final Result is : Severe DR"
        label = tk.Label(window, text=text)  
        label.pack()
    else:
        # print('Final Result is : Proliferative DR')
        text = "Final Result is : Proliferative DR"
        label = tk.Label(window, text=text)  
        label.pack()
    

    # label_image.config(image=image_tk)
    # label_image.image = image_tk





# Create three text boxes for user input
    # label_input = tk.Label(window, text="Input values:")
    # label_input.pack()

# label_textbox1 = tk.Label(window, text="Doctor Name")
# label_textbox1.pack()
# textbox1 = tk.Entry(window)
# textbox1.pack()

# label_textbox2 = tk.Label(window, text="Patient Name")
# label_textbox2.pack()
# textbox2 = tk.Entry(window)
# textbox2.pack()

# label_textbox3 = tk.Label(window, text="Age")
# label_textbox3.pack()
# textbox3 = tk.Entry(window)
# textbox3.pack()


# radio_var = tk.StringVar()
# radio_var.set("Option 1")

# radio_button1 = tk.Radiobutton(window, text="Female", variable=radio_var, value="F")
# radio_button1.pack()

# radio_button2 = tk.Radiobutton(window, text="Male", variable=radio_var, value="M")
# radio_button2.pack()

# Create a button to open an image file
button_open_image = tk.Button(window, text="Open Image", command=open_image)
button_open_image.pack()



# # Create a label to display the loaded image
# label_image = tk.Label(window)
# label_image.pack()

# Create a submit button to submit user inputs
# def submit():
#     textbox1_value = textbox1.get()
#     textbox2_value = textbox2.get()
#     textbox3_value = textbox3.get()
#     radio_value = radio_var.get()
#     print(f"Doctor Name {textbox1_value}\nPatient Name {textbox2_value}\nAge {textbox3_value}\nRadio button value: {radio_value}")

# button_submit = tk.Button(window, text="Submit", command=submit)
# button_submit.pack()

# Run the Tkinter event loop
window.mainloop()