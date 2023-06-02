""" This programme lets user choose types of food, type in user's name, and order
food. Past orders can be seen in History GUI. If unsatisfactory, users can
cancel order. Information GUI tells users how to use programme. Details GUI
shows more details about the food when user clicks on image of one food.
"""
# version 3 testing: History GUI
# This GUI displays past orders of Sushi Takeaway on user's computer 

# Import all needed libraries for the programme
import os
os.system('cmd /c "pip install Pillow"')
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import tkinter.scrolledtext as st
from datetime import date, datetime
import re


class History:
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
        self.history_frame = Frame(padx = 10, pady = 10, bg=self.bg_color)
        self.history_frame.grid()        
        
        try: 
            # check if sushi_takeaway_history.txt file is available in sushi_takeaway folder
            with open("sushi_takeaway_history.txt", "r") as history_file:
                self.raw_history_file = history_file.read().split("\n")
        
        except FileNotFoundError: 
            # in case user deletes or misplaces history.txt file
            # a text label appears showing problem with solution            
            self.history_txt_error_msg = Label(self.history_frame, text="Error: cannot find sushi_takeaway_history.txt file.\n\nPlease re-install this programme.\n\nSushi Takeaway store information can be accessed by clicking 'Information' button at top right of programme. We are sorry for the inconvenience.", font=self.large_font, bg=self.bg_color, fg=self.error_font_color, wraplength="700")
            self.history_txt_error_msg.grid(row=0, column=0)        
        
        else:
            # if history.txt file is available
            # commnents are directly removed word by word, in case the text file is edited
            # # incorrectly by takeaway manager or user, and may cause programme to work incorrectly
            
            history_txt_file_comment = "# string's order is: user name, data and time of order, [quantities of foods ordered], total price"
            
            try:
                # check in case comment in history.txt file doesn't match
                self.raw_history_file.remove(history_txt_file_comment)
            
            except ValueError:
                # in case sushi manager incorrectly edits sushi_takeaway_menu.txt file
                # by altering comment lines
                # error message shows up with problem user encounters and solution
                self.history_txt_error_msg = Label(self.history_frame, text="Error in history text file.\n\nPlease contact us to solve the problem. Sushi takeaway store information can be accessed by closing this window and clicking 'Information' button at top right of programme.\n\nWe are sorry for the inconvenience.", font=self.large_font, bg=self.bg_color, fg=self.error_font_color, justify="center", wraplength="670")
                self.menu_txt_error_msg.grid(row=0)   
            
            else:
                # History GUI is set up using Tkinter widgets
                self.history_heading = Label(self.history_frame, text="Past Orders on Sushi Takeaway", font=self.large_font, fg=self.font_color, bg=self.bg_color)
                self.history_heading.grid(row=0, padx=5, pady=5)
                
                # instructions stating how to use scrolled text
                self.history_instructions = Label(self.history_frame, text="Below displays all past orders made from your device. Scroll down for more", font=self.small_heading_font, fg=self.font_color, bg=self.bg_color, wraplength="400")
                self.history_instructions.grid(row=1, pady=5) 
                
                # set up scrolled text widget to display all past orders
                self.display_past_orders = st.ScrolledText(self.history_frame, width=40, height=5, font=self.normal_font, wrap=WORD)
                self.display_past_orders.grid(row=3)
                
                
                #  Add text in Scrolledtext and make it read only; this method was
                # recommended by a website while creating Temp_converter project
                # website: GeeksforGeeks
                
                # history of past orders are reversed to show latest orders at the top
                # in reverse-chronological order
                self.raw_history_file.reverse()
                
                # put all past orders in a string for display
                self.display_string = ""
                for item in self.raw_history_file:
                    self.display_string += f"{item}\n"
                
                if self.display_string == "\n":
                    # if there is no past order, an error string is displayed
                    print("nothing...")
                    self.display_past_orders.insert(INSERT, "You have not made an order... Please return once you have made at least one order. Thank you.")
                    self.display_past_orders.configure(state ='disabled') 
                    
                else:
                    # If there are past orders to be displayed
                    self.display_past_orders.insert(INSERT, self.display_string)
                    self.display_past_orders.configure(state ='disabled')                
            
        finally:
            # a button to close programme is present whether there is an error or not, so users can access information 
            self.close_history = Button(self.history_frame, text="Close window", bg=self.btn_bg_color, fg=self.font_color, font=self.small_heading_font, command=quit)
            self.close_history.grid(row=4, padx=10, pady=10)
    
    # Terminate all GUIs
    def quit(self):
        self.destroy()    
    
# main routine
if __name__ == "__main__":
    # set up main GUI as root with title and size/geometry and run programme    
    root = Tk()
    root.title("Sushi Takeaway History")
    # root.geometry("670x760") 
    root.resizable(0, 0)
    History()
    root.mainloop()