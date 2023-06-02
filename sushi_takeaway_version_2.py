""" This programme lets user choose types of food, type in user's name, and order
food. Past orders can be seen in History GUI. If unsatisfactory, users can
cancel order. Information GUI tells users how to use programme. Details GUI
shows more details about the food when user clicks on image of one food.
"""
# version 2 testing: Information GUI
# This GUI is contains information of sushi takeaway shop

# Import all needed libraries for the programme
import os
os.system('cmd /c "pip install Pillow"')
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import tkinter.scrolledtext as st
from datetime import date, datetime
import re


class Information:
    """ This is the main GUI window that takes food orders from users. Two 
    buttons and images give access to three other GUIs
    """
    
    def __init__(self):
        """Initialising variables and setting up Takeaway GUI
        """ 
        
        # common format for regular and large texts
        # large texts are found in headings and buttons
        self.normal_font = ("Helvetica 12")
        self.small_heading_font = ("Helvetica 14 bold")
        self.large_font = ("Helvetica 17 bold")
        
        # color palette that is friendly to colour-blind people
        self.btn_bg_color = "#7CA1CC"
        self.error_bg_color = "#EEBAB4"
        self.bg_color = "#A8B6CC"
        self.error_font_color = "#F05039"
        self.font_color = "#141414"
        
        # height and weight variables for button size
        self.btn_width="16"
        self.btn_height="0"
        
        # set up main GUI frame        
        self.info_frame = Frame(padx = 10, pady = 10, bg=self.bg_color)
        self.info_frame.grid()        
        
        try: 
            # check if sushi_takeaway_information.txt file is available in sushi_takeaway folder
            with open("sushi_takeaway_information.txt", "r") as info_file:
                self.info_file = info_file.read()
        
        except FileNotFoundError: 
            # in case user deletes or misplaces sushi_takeaway_information.txt file
            # a text label appears showing problem with solution            
            self.info_txt_error_msg = Label(self.info_frame, text="Error: cannot find sushi_takeaway_information.txt file.\n\nPlease re-install this programme.\n\nWe are sorry for the inconvenience.", font=self.large_font, bg=self.bg_color, fg=self.error_font_color, wraplength="700")
            self.info_txt_error_msg.grid(row=0, column=0)        
        
        else:
            # information.txt file is available
            # information GUI is set up using Tkinter widgets
            self.info_heading = Label(self.info_frame, text="Information about Sushi Takeaway", font=self.large_font, fg=self.font_color, bg=self.bg_color)
            self.info_heading.grid(row=0, padx=5, pady=5)
            
            self.info_slogan = Label(self.info_frame, text="Come and see our wares!", font=self.small_heading_font, fg=self.font_color, bg=self.bg_color)
            self.info_slogan.grid(row=1, pady=5)
            
            self.info_label = Label(self.info_frame, text=self.info_file, bg=self.bg_color, fg=self.font_color, font=self.normal_font, wraplength="400", justify="center")
            self.info_label.grid(row=2)
            
        finally:
            # no matter if information text is available or not, user can close Information window and continue ordering 
            self.close_info = Button(self.info_frame, text="Close window", bg=self.btn_bg_color, fg=self.font_color, font=self.small_heading_font, command=quit)
            self.close_info.grid(row=3, padx=10, pady=10)
            
    # Terminate all GUIs
    def quit(self):
        self.destroy()    
    
# main routine
if __name__ == "__main__":
    # set up main GUI as root with title and size/geometry and run programme    
    root = Tk()
    root.title("Sushi Takeaway Information")
    # root.geometry("670x760") 
    root.resizable(0, 0)
    Information()
    root.mainloop()