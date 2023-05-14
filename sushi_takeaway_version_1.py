""" This programme lets user choose types of food, type in user's name, and order 
food. Past orders can be seen in History GUI. If unsatisfactory, users can 
cancel order. Information GUI tells users how to use programme. Details GUI 
shows more details about the food when user clicks on image of one food.
"""

# Import all needed libraries for the programme
from tkinter import *
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
        sushi_menu_list = [] # total is menu_list, and sushi_menu_list would be menu_list[i]
        
        # common format for regular and large texts
        # large texts are found in headings and buttons
        normal_font = ("Helvetica 12")
        small_heading_font = ("Helvetica 14 bold")
        large_font = ("Helvetica 17 bold")
        
        # color palette that is friendly to colour-blind people
        bg_btn_color = "#7CA1CC"
        bg_color = "#A8B6CC"
        error_font_color = "#F05039"
        font_color = "#141414"
        
        # set up GUI frame and non-button widgets
        self.takeaway_frame = Frame(padx = 10, pady = 10, bg=bg_color)
        self.takeaway_frame.grid()
        
        self.top_buttons_frame = Frame(self.takeaway_frame, bg=bg_color)
        self.top_buttons_frame.grid(row=0, pady=10)
        
        # add History and Information button widgets
        self.history_button = Button(self.top_buttons_frame, text="History", fg=font_color, bg=bg_btn_color, font=large_font, width="12", command=self.open_history)
        self.history_button.grid(row=0, column=0, padx=5)
        
        self.information_button = Button(self.top_buttons_frame, text="Information", fg=font_color, bg=bg_btn_color, font=large_font, width="12", command=self.open_information)
        self.information_button.grid(row=0, column=1, padx=5)        
        
        self.takeaway_heading = Label(self.takeaway_frame, text="Welcome to Sushi Takeaway", font=large_font, fg=font_color, bg=bg_color, justify="center")
        self.takeaway_heading.grid(row=1)
        
        # self.takeaway_description scrapped because same function but better in Information
        
        # provide instructions for users how to open Details GUI
        self.takeaway_instruction = Label(self.takeaway_frame, text="Please click on images of each food for more details.", bg=bg_color, fg=font_color, font=normal_font)
        self.takeaway_instruction.grid(row=2)
        
        self.sushi_heading = Label(self.takeaway_frame, text="Sushi", bg=bg_color, fg=font_color, font=small_heading_font)
        self.sushi_heading.grid(row=3, pady=10)
        
        self.sushi_menu_frame = Frame(self.takeaway_frame, bg=bg_color)
        self.sushi_menu_frame.grid(row=4, padx=5, pady=5)
        
        
        # foodds
        
        
        
        # Create frame for user's name input indentification purpose 
        self.name_frame = Frame(self.takeaway_frame, bg=bg_color)
        self.name_frame.grid(row=3)
            
        self.name_label = Label(self.name_frame, text="Name: ", bg=bg_color, fg=font_color, font=normal_font)
        self.name_label.grid(row=0, column=0, pady=5)
        
        self.name_textbox = Entry(self.name_frame, font=font_color, bg="white")
        self.name_textbox.grid(row=0, column=1, pady=5)
        
        # This widget stays in name_frame as it is related
        self.name_instructions_text = "This is for identificaton purposes only. You can type either your first name or your initials."
        self.name_instructions_label = Label(self.name_frame, text=self.name_instructions_text, fg=font_color, bg=bg_color, font=normal_font, wraplength="400")
        self.name_instructions_label.grid(row=1, column=0, columnspan=2, pady=5)
        
        self.bottom_buttons_frame = Frame(self.takeaway_frame, bg=bg_color)
        self.bottom_buttons_frame.grid(row=4, pady=10)
        
        self.order_button = Button(self.bottom_buttons_frame, text="Order", font=large_font, bg=bg_btn_color, fg=font_color, width="12", command=self.order)
        self.order_button.grid(row=0, column=0, padx=5)
        
        self.cancel_order_button = Button(self.bottom_buttons_frame, text="Cancel order", font=large_font, bg=bg_btn_color, fg=font_color, width="12", command=self.cancel_order)
        self.cancel_order_button.grid(row=0, column=1, padx=5)

    def open_history(self):
        pass
    
    def open_information(self):
        pass
    
    def order(self):
        pass
    
    def cancel_order(self):
        pass
    
# main routine
if __name__ == "__main__":
    # set up main GUI as root with title and size/geometry and run programme    
    root = Tk()
    root.title("Sushi Takeaway")
    # root.geometry? !!!
    root.resizable(0, 0)
    Takeaway()
    root.mainloop()