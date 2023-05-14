""" Testing how to put image as a button"""

# import the required modules:
import os
os.system('cmd /c "pip install Pillow"')
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Load the image:
img = Image.open("images/salmon_sushi.jpg")

# Resize the image to fit the button:
resized_img = img.resize((400, 200), Image.ANTIALIAS)

# Convert the image to a tkinter PhotoImage:
img_obj = ImageTk.PhotoImage(resized_img)

# Create the button and add the image:
button = Button(root, image=img_obj)
button.pack()

root.mainloop()