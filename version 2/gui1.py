import main1
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Global variable to store the selected file path
selected_file_path = ""

# Create a Tkinter window
window = tk.Tk()
window.geometry("400x400")
window.title("DRCNN Image")



def single_img():
    
    global selected_file_path

    img = str(selected_file_path)
    

    report = main1.single_predict(img)
    
    if report == 0:
        
        text = "Final Result is : No DR"
        label = tk.Label(window, text=text)  
        label.pack() 
    elif report == 1:
        
        text = "Final Result is : Mild DR"
        label = tk.Label(window, text=text)  
        label.pack()
    elif report == 2:   
        
        text = "Final Result is : Moderate DR"
        label = tk.Label(window, text=text)  
        label.pack()
    elif report == 3:
        
        text = "Final Result is : Severe DR"
        label = tk.Label(window, text=text)  
        label.pack()
    else:
        
        text = "Final Result is : Proliferative DR"
        label = tk.Label(window, text=text)  
        label.pack()
    



# Create a function to open an image file
def open_image():
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
    label.pack() 
    

    label = tk.Label(window, text=selected_file_path)  
    label.pack()
    

    # single_img(file_path)
    return selected_file_path
    



# Create a button to open an image file
button_open_image = tk.Button(window, text="Open Image", command=open_image)
button_open_image.pack()

# Create a label to display the loaded image
label_image = tk.Label(window)
label_image.pack()

label = tk.Label(window, text=selected_file_path)  
label.pack()

# Create a button widget
button = tk.Button(window, text="Results", command=single_img)
button.pack()

# Run the Tkinter event loop
window.mainloop()
