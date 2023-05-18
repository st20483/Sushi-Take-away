""" Testing how to put image as a button"""

# Import all needed libraries for the programme
import os
os.system('cmd /c "pip install Pillow"')
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import tkinter.scrolledtext as st
from datetime import date
import re


class Takeaway:
    """ This is the main GUI window that takes food orders from users. Two 
    buttons and iamges give access to three other GUIs
    """
    
    def __init__(self):
        """Initialising variables and setting up Takeaway GUI
        """
        self.food1_image = ImageTk.PhotoImage(Image.open("images/salmon_sushi.ppm").resize((10, 10)))
        
        
        
        # common format for regular and large texts
        # large texts are found in headings and buttons
        normal_font = ("Helvetica 12")
        small_heading_font = ("Helvetica 14 bold")
        large_font = ("Helvetica 17 bold")
        
        # color palette that is friendly to colour-blind people
        btn_bg_color = "#7CA1CC"
        bg_color = "#A8B6CC"
        error_font_color = "#F05039"
        font_color = "#141414"
        
        # set up GUI frame and non-button widgets
        self.takeaway_frame = Frame(padx = 10, pady = 10, bg=bg_color)
        self.takeaway_frame.grid()
        
        self.top_buttons_frame = Frame(self.takeaway_frame, bg=bg_color)
        self.top_buttons_frame.grid(row=0, pady=5)
        
        # add History and Information button widgets
        self.history_button = Button(self.top_buttons_frame, text="History", fg=font_color, bg=btn_bg_color, font=large_font, width="12", command=self.open_history)
        self.history_button.grid(row=0, column=0, padx=10)
        
        self.information_button = Button(self.top_buttons_frame, text="Information", fg=font_color, bg=btn_bg_color, font=large_font, width="12", command=self.open_information)
        self.information_button.grid(row=0, column=1, padx=10)        
        
        self.takeaway_heading = Label(self.takeaway_frame, text="Welcome to Sushi Takeaway", font=large_font, fg=font_color, bg=bg_color, justify="center")
        self.takeaway_heading.grid(row=1)
        
        # self.takeaway_description scrapped because same function but better in Information !!
        
        # provide instructions for users how to open Details GUI
        self.takeaway_instruction = Label(self.takeaway_frame, text="Please click on images of each food for more details.\nThe maximum amount per food you can order is 100.", bg=bg_color, fg=font_color, font=normal_font)
        self.takeaway_instruction.grid(row=2) # may have to change this: no Details GUI !!
        
        self.food_menu_frame = LabelFrame(self.takeaway_frame, bg=bg_color, text="Sushi", font=small_heading_font, fg=font_color)
        self.food_menu_frame.grid(row=3, padx=5, pady=5)
        
        self.food1_frame = LabelFrame(self.food_menu_frame, bg=bg_color, text="Salmon sushi", font=normal_font, fg=font_color, labelanchor="n")
        self.food1_frame.grid(row=0, column=0)
        
        self.food1_image_label = Label(self.food1_frame, image=self.food1_image, bg=bg_color)
        self.food1_image_label.grid(row=0)        
        
        self.food1_price = Label(self.food1_frame, text="$2.50", bg=bg_color, fg=font_color, font=normal_font)
        self.food1_price.grid(row=1)
        
        self.food1_quantity = IntVar(value=0)
        # max food quantity is 100 because sushi takeaway is equipped to cater
        # for only individuals and small groups up to 10 people
        # wrap is True so bulk-buyers can go to maximum amount in one click
        self.food1_quantity_spinbox = Spinbox(self.food1_frame, from_=0, to=100, increment="1", format="%.0f", fg=font_color, font=normal_font, textvariable=self.food1_quantity, justify="center", width=4, wrap=True)
        self.food1_quantity_spinbox.grid(row=2)
        
        self.food2 = LabelFrame(self.food_menu_frame, bg=bg_color)
        self.food2.grid(row=0, column=1)
        
        self.food3 = LabelFrame(self.food_menu_frame, bg=bg_color)
        self.food3.grid(row=0, column=2)
        
        self.food4 = LabelFrame(self.food_menu_frame, bg=bg_color)
        self.food4.grid(row=0, column=3)        
        
        # quantity use spinbox
        
        
        # Create frame for user's name input indentification purpose 
        self.name_frame = LabelFrame(self.takeaway_frame, bg=bg_color, text="Identification purposes only", font=small_heading_font, fg=font_color)
        self.name_frame.grid(row=4, padx=5, pady=5)
            
        self.name_label = Label(self.name_frame, text="Name: ", bg=bg_color, fg=font_color, font=normal_font)
        self.name_label.grid(row=0, column=0, pady=5)
        
        self.name_textbox = Entry(self.name_frame, font=font_color, bg="white")
        self.name_textbox.grid(row=0, column=1, pady=5)
        
        # This widget stays in name_frame as it is related
        self.name_instructions_text = "This is for identificaton purposes only. You can type either your first name or your initials."
        self.name_instructions_label = Label(self.name_frame, text=self.name_instructions_text, fg=font_color, bg=bg_color, font=normal_font, wraplength="400")
        self.name_instructions_label.grid(row=1, column=0, columnspan=2, pady=5)
        
        self.bottom_buttons_frame = Frame(self.takeaway_frame, bg=bg_color)
        self.bottom_buttons_frame.grid(row=5, pady=5)
        
        self.order_button = Button(self.bottom_buttons_frame, text="Order", font=large_font, bg=btn_bg_color, fg=font_color, width="12", command=self.order)
        self.order_button.grid(row=0, column=0, padx=10)
        
        self.cancel_order_button = Button(self.bottom_buttons_frame, text="Cancel order", font=large_font, bg=btn_bg_color, fg=font_color, width="12", command=self.cancel_order)
        self.cancel_order_button.grid(row=0, column=1, padx=10)
        
        self.exit_takeaway_button = Button(self.bottom_buttons_frame, text="Exit Programme", font=large_font, bg=btn_bg_color, fg=font_color, width = "26", command=quit)
        self.exit_takeaway_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def open_history(self):
        pass
    
    def open_information(self):
        pass
    
    def order(self):
        pass
    
    def cancel_order(self):
        pass
    
    # Terminate all GUIs
    def quit(self):
        self.destroy()    
    
# main routine
if __name__ == "__main__":
    # set up main GUI as root with title and size/geometry and run programme    
    root = Tk()
    root.title("Sushi Takeaway")
    # root.geometry? !!!
    root.resizable(0, 0)
    Takeaway()
    root.mainloop()
