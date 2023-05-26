""" How to use texts files in Takeaway GUI """
# menu txt file for display - relevant implication Future Proofing
# history txt for order simulation and access by users - End-user Consideration

# version 1 testing: Takeaway GUI
# This GUI is the main GUI of the programme. From Information GUI and 
# History GUI can be accessed from this GUI

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
        
        # height and weight variables for button size
        btn_width="16"
        btn_height="0"
        
        # set up main GUI frame
        self.takeaway_frame = Frame(padx = 10, pady = 10, bg=bg_color)
        self.takeaway_frame.grid()
        
        try: 
            with open("sushi_takeaway_menu.txt", "r") as menu_file:
                self.raw_menu_file = menu_file.read().split("\n")
            
            # commnents are directly removed word by word, in case the text file is edited
            # incorrectly by takeaway manager and may cause programme to work incorrectly
            
            menu_txt_comment_1 = '# Follow this format: food name, food image name, price, "ingredients", "food and allergy alerts". Do NOT remove these two hashtag # lines. Max 8 food items.'
            
            menu_txt_comment_2 = '# Please put comma , between every part and put ingredients and food alerts in quotation " " symbols. If unsure, call programmer.'
            
            try:
                self.raw_menu_file.remove(menu_txt_comment_1)
                self.raw_menu_file.remove(menu_txt_comment_2)
                
                # create food1 profile as a list for the 1st food item
                # with food name, price, image name and ingredients as items of list
                self.food1 = self.raw_menu_file[0].split(", ")
                
                # set up image path of food 1 for later implementing in widgets
                # strip function for image name in case there are white spaces around string
                self.food1_image_path = "images/" + self.food1[1].strip()
                self.food1_image = ImageTk.PhotoImage(Image.open(self.food1_image_path).resize((90, 90)))
                
                # foods 2-8 are implemented same way as food 1
                self.food2 = self.raw_menu_file[1].split(", ")
                
                self.food2_image_path = "images/" + self.food2[1].strip()
                self.food2_image = ImageTk.PhotoImage(Image.open(self.food2_image_path).resize((90, 90)))        
                
                self.food3 = self.raw_menu_file[2].split(", ")
                
                self.food3_image_path = "images/" + self.food3[1].strip()
                self.food3_image = ImageTk.PhotoImage(Image.open(self.food3_image_path).resize((90, 90)))        
                self.food4 = self.raw_menu_file[3].split(", ")
                
                self.food4_image_path = "images/" + self.food4[1].strip()
                self.food4_image = ImageTk.PhotoImage(Image.open(self.food4_image_path).resize((90, 90)))
                
                self.food5 = self.raw_menu_file[4].split(", ")
                
                self.food5_image_path = "images/" + self.food5[1].strip()
                self.food5_image = ImageTk.PhotoImage(Image.open(self.food5_image_path).resize((90, 90)))        
                self.food6 = self.raw_menu_file[5].split(", ")
                
                self.food6_image_path = "images/" + self.food6[1].strip()
                self.food6_image = ImageTk.PhotoImage(Image.open(self.food6_image_path).resize((90, 90)))        
                self.food7 = self.raw_menu_file[6].split(", ")
                
                self.food7_image_path = "images/" + self.food7[1].strip()
                self.food7_image = ImageTk.PhotoImage(Image.open(self.food7_image_path).resize((90, 90)))        
                self.food8 = self.raw_menu_file[7].split(", ")
                
                self.food8_image_path = "images/" + self.food8[1].strip()
                self.food8_image = ImageTk.PhotoImage(Image.open(self.food8_image_path).resize((90, 90)))        
                
                # a separate frame to contain history and information buttons
                self.top_buttons_frame = Frame(self.takeaway_frame, bg=bg_color)
                self.top_buttons_frame.grid(row=0, pady=5)
                
                # add History and Information button widgets
                self.history_button = Button(self.top_buttons_frame, text="History", fg=font_color, bg=btn_bg_color, font=small_heading_font, width=btn_width, height=btn_height, command=self.open_history)
                self.history_button.grid(row=0, column=0, padx=10)
                
                self.information_button = Button(self.top_buttons_frame, text="Information", fg=font_color, bg=btn_bg_color, font=small_heading_font, width=btn_width, height=btn_height, command=self.open_information)
                self.information_button.grid(row=0, column=1, padx=10)        
                
                self.takeaway_heading = Label(self.takeaway_frame, text="Welcome to Sushi Takeaway", font=large_font, fg=font_color, bg=bg_color, justify="center")
                self.takeaway_heading.grid(row=1)
                
                # self.takeaway_description scrapped because same function but better in Information !!
                
                # provide instructions for users how to open Details GUI
                self.takeaway_instruction = Label(self.takeaway_frame, text="Come and see our wares!   The maximum amount per food is 100.", bg=bg_color, fg=font_color, font=normal_font)
                self.takeaway_instruction.grid(row=2) # may have to change this: no Details GUI !!
                
                # A frame to hold all food items like a menu
                self.menu_frame = Frame(self.takeaway_frame, bg=bg_color)
                self.menu_frame.grid(row=3, padx=5)
                
                # Contains one food dish and its general details without ingredients and food alerts
                # LabelFrame for displaying food name and put its details in visual box
                self.food1_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food1[0].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food1_frame.grid(row=0, column=0, sticky="E"+"W")
                # sticky tells that this labelframe has maximum area in its grid in menu_frame
                
                self.food1_image_label = Label(self.food1_frame, image=self.food1_image, bg=bg_color, width="100")
                self.food1_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food1_price_label = Label(self.food1_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food1_price_label.grid(row=1, column=0)        
                
                self.food1_price = Label(self.food1_frame, text=self.food1[2].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food1_price.grid(row=1, column=1)
                
                self.food1_quantity_label = Label(self.food1_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food1_quantity_label.grid(row=2, column=0)
                
                self.food1_quantity = IntVar(value=0)
                # max food quantity is 100 because sushi takeaway is equipped to cater
                # for only individuals and small groups up to 10 people
                # wrap is True so bulk-buyers can go to maximum amount in one click
                self.food1_quantity_spinbox = Spinbox(self.food1_frame, from_=0, to=100, increment="1",format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food1_quantity, justify="center", width=4, wrap=True)
                self.food1_quantity_spinbox.grid(row=2, column=1)
                
                # foods 2-8 are replica of food 1, but with unique foods and details from sushi_takeaway_menu.txt file
                self.food2_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food2[0].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food2_frame.grid(row=0, column=1, sticky="E"+"W")
                
                self.food2_image_label = Label(self.food2_frame, image=self.food2_image, bg=bg_color, width="100", anchor="center")
                self.food2_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food2_price_label = Label(self.food2_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food2_price_label.grid(row=1, column=0)        
                
                self.food2_price = Label(self.food2_frame, text=self.food2[2].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food2_price.grid(row=1, column=1)
                
                self.food2_quantity_label = Label(self.food2_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food2_quantity_label.grid(row=2, column=0)
                
                self.food2_quantity = IntVar(value=0)
                self.food2_quantity_spinbox = Spinbox(self.food2_frame, from_=0, to=100, increment="1",format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food2_quantity, justify="center", width=4, wrap=True)
                self.food2_quantity_spinbox.grid(row=2, column=1)        
                
                self.food3_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food3[0].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food3_frame.grid(row=0, column=2, sticky="E"+"W")
                
                self.food3_image_label = Label(self.food3_frame, image=self.food3_image, bg=bg_color, width="100", anchor="center")
                self.food3_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food3_price_label = Label(self.food3_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food3_price_label.grid(row=1, column=0)        
                
                self.food3_price = Label(self.food3_frame, text=self.food3[2 ].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food3_price.grid(row=1, column=1)
                
                self.food3_quantity_label = Label(self.food3_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food3_quantity_label.grid(row=2, column=0)
                
                self.food3_quantity = IntVar(value=0)
                self.food3_quantity_spinbox = Spinbox(self.food3_frame, from_=0, to=100, increment="1",format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food3_quantity, justify="center", width=4, wrap=True)
                self.food3_quantity_spinbox.grid(row=2, column=1)          
                
                self.food4_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food4[0 ].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food4_frame.grid(row=0, column=3, sticky="E"+"W") 
                
                self.food4_image_label = Label(self.food4_frame, image=self.food4_image, bg=bg_color, width="100", anchor="center")
                self.food4_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food4_price_label = Label(self.food4_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food4_price_label.grid(row=1, column=0)        
                
                self.food4_price = Label(self.food4_frame, text=self.food4[2 ].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food4_price.grid(row=1, column=1)
                
                self.food4_quantity_label = Label(self.food4_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food4_quantity_label.grid(row=2, column=0)
                
                self.food4_quantity = IntVar(value=0)
                self.food4_quantity_spinbox = Spinbox(self.food4_frame, from_=0, to=100, increment="1", format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food4_quantity, justify="center", width=4, wrap=True)
                self.food4_quantity_spinbox.grid(row=2, column=1)          
                
                self.food5_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food5[0 ].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food5_frame.grid(row=1, column=0, sticky="E"+"W")
                
                self.food5_image_label = Label(self.food5_frame, image=self.food5_image, bg=bg_color, width="100", anchor="center")
                self.food5_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food5_price_label = Label(self.food5_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food5_price_label.grid(row=1, column=0)        
                
                self.food5_price = Label(self.food5_frame, text=self.food5[2 ].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food5_price.grid(row=1, column=1)
                
                self.food5_quantity_label = Label(self.food5_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food5_quantity_label.grid(row=2, column=0)
                
                self.food5_quantity = IntVar(value=0)
                self.food5_quantity_spinbox = Spinbox(self.food5_frame, from_=0, to=100, increment="1", format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food5_quantity, justify="center", width=4, wrap=True)
                self.food5_quantity_spinbox.grid(row=2, column=1)          
                
                self.food6_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food6[0 ].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food6_frame.grid(row=1, column=1, sticky="E"+"W") 
                
                self.food6_image_label = Label(self.food6_frame, image=self.food6_image, bg=bg_color, width="100", anchor="center")
                self.food6_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food6_price_label = Label(self.food6_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food6_price_label.grid(row=1, column=0)        
                
                self.food6_price = Label(self.food6_frame, text=self.food6[2].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food6_price.grid(row=1, column=1)
                
                self.food6_quantity_label = Label(self.food6_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food6_quantity_label.grid(row=2, column=0)
                
                self.food6_quantity = IntVar(value=0)
                self.food6_quantity_spinbox = Spinbox(self.food6_frame, from_=0, to=100, increment="1", format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food6_quantity, justify="center", width=4, wrap=True)
                self.food6_quantity_spinbox.grid(row=2, column=1)          
                
                self.food7_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food7[0 ].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food7_frame.grid(row=1, column=2, sticky="E"+"W") 
                
                self.food7_image_label = Label(self.food7_frame, image=self.food7_image, bg=bg_color, width="100", anchor="center")
                self.food7_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food7_price_label = Label(self.food7_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food7_price_label.grid(row=1, column=0)        
                
                self.food7_price = Label(self.food7_frame, text=self.food7[2 ].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food7_price.grid(row=1, column=1)
                
                self.food7_quantity_label = Label(self.food7_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food7_quantity_label.grid(row=2, column=0)
                
                self.food7_quantity = IntVar(value=0)
                self.food7_quantity_spinbox = Spinbox(self.food7_frame, from_=0, to=100, increment="1", format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food7_quantity, justify="center", width=4, wrap=True)
                self.food7_quantity_spinbox.grid(row=2, column=1)          
                
                self.food8_frame = LabelFrame(self.menu_frame, bg=bg_color, text=self.food8[0 ].strip().capitalize(), font=normal_font, fg=font_color, labelanchor="n")
                self.food8_frame.grid(row=1, column=3, sticky="E"+"W")         
                
                self.food8_image_label = Label(self.food8_frame, image=self.food8_image, bg=bg_color, width="100", anchor="center")
                self.food8_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food8_price_label = Label(self.food8_frame, text="Price:", bg=bg_color, fg=font_color, font=normal_font)
                self.food8_price_label.grid(row=1, column=0)        
                
                self.food8_price = Label(self.food8_frame, text=self.food8[2 ].strip(), bg=bg_color, fg=font_color, font=normal_font)
                self.food8_price.grid(row=1, column=1)
                
                self.food8_quantity_label = Label(self.food8_frame, text="Amount:", bg=bg_color, fg=font_color, font=normal_font)
                self.food8_quantity_label.grid(row=2, column=0)
                
                self.food8_quantity = IntVar(value=0)
                self.food8_quantity_spinbox = Spinbox(self.food8_frame, from_=0, to=100, increment="1", format="%3.0f", fg=font_color, font=normal_font, textvariable=self.food8_quantity, justify="center", width=4, wrap=True)
                self.food8_quantity_spinbox.grid(row=2, column=1)          
                
                # button to check food quantity and show total price
                self.calculate_total_btn = Button(self.menu_frame, text="Show total price: ", bg=btn_bg_color, fg=font_color, font=small_heading_font, width=btn_width, height=btn_height, command=self.show_total_price)
                self.calculate_total_btn.grid(row=3, column=0, columnspan=2, sticky="E", pady=5, padx=10)
                
                self.total_price = 0
                self.total_price_str = StringVar(value="${:.2f}".format(self.total_price))
                self.total_price_label = Label(self.menu_frame, textvariable=self.total_price_str, bg=bg_color, fg=font_color, font=small_heading_font)
                self.total_price_label.grid(row=3, column=2)
                
                
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
                self.bottom_buttons_frame.grid(row=5, pady=10)
                
                self.order_button = Button(self.bottom_buttons_frame, text="Order", font=small_heading_font, bg=btn_bg_color, fg=font_color, width=btn_width, height=btn_height, command=self.order)
                self.order_button.grid(row=0, column=0, padx=5)
                
                self.cancel_order_button = Button(self.bottom_buttons_frame, text="Cancel order", font=small_heading_font, bg=btn_bg_color, fg=font_color, width=btn_width, height=btn_height, command=self.cancel_order)
                self.cancel_order_button.grid(row=0, column=1, padx=5)
                
                self.exit_takeaway_button = Button(self.bottom_buttons_frame, text="Exit Programme", font=small_heading_font, bg=btn_bg_color, fg=font_color, width = "26", height=btn_height, command=quit)
                self.exit_takeaway_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
            
            except ValueError:
                # in case sushi manager incorrectly edits sushi_takeaway_menu.txt file
                # by altering comment lines
                # error message shows up with problem user encounters and solution to solve
                self.menu_txt_error_msg = Label(self.takeaway_frame, text="Error: Error in text file.\n\nPlease contact Sushi Takeaway at [phone number]", font=large_font, bg=bg_color, fg=error_font_color, justify="center")
                self.menu_txt_error_msg.grid(row=0)
                
        # in case user deletes sushi_takeaway_menu.txt file
        # a text label appears showing problem with solution
        except FileNotFoundError: 
            self.menu_txt_error_msg = Label(self.takeaway_frame, text="Error: cannot find sushi_takeaway_menu.txt file.\n\nPlease delete and redownload this programme.", font=large_font, bg=bg_color, fg=error_font_color, wraplength="700")
            self.menu_txt_error_msg.grid(row=0, column=0)

    def open_history(self):
        pass
    
    def open_information(self):
        pass
    
    def show_total_price(self):
        print(self.food1[2], str(self.food1_quantity.get()), "\n")
        total_food1 = self.food1_quantity.get() * float(self.food1[2])
        print(total_food1, "\n")
        total_food2 = self.food2_quantity.get() + self.food3_quantity.get() + self.food4_quantity.get() + self.food5_quantity.get() + self.food6_quantity.get() + self.food7_quantity.get() + self.food8_quantity.get()
        
        self.total_price = total_food1
        
    
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
    root.geometry("670x730") 
    root.resizable(0, 0)
    Takeaway()
    root.mainloop()
