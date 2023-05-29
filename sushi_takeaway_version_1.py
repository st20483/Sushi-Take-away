""" testing for programme outputs"""
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
        self.takeaway_frame = Frame(padx = 10, pady = 10, bg=self.bg_color)
        self.takeaway_frame.grid()
        
        try: 
            # check if sushi_takeaway_menu.txt file is available in sushi_takeaway folder
            with open("sushi_takeaway_menu.txt", "r") as menu_file:
                self.raw_menu_file = menu_file.read().split("\n")
        
        except FileNotFoundError: 
            # in case user deletes sushi_takeaway_menu.txt file
            # a text label appears showing problem with solution            
            self.menu_txt_error_msg = Label(self.takeaway_frame, text="Error: cannot find sushi_takeaway_menu.txt file.\n\nPlease delete and redownload this programme.", font=self.large_font, bg=self.bg_color, fg=self.error_font_color, wraplength="700")
            self.menu_txt_error_msg.grid(row=0, column=0)        
        
        else:
            # if menu.txt file is available
            
            # commnents are directly removed word by word, in case the text file is edited
            # incorrectly by takeaway manager and may cause programme to work incorrectly
            
            menu_txt_comment_1 = '# Follow this format: food name, food image name, price, "ingredients", "food and allergy alerts". Do NOT touch these two hashtag # lines. Max 8 food items.'
            
            menu_txt_comment_2 = '# Please put comma , between every part and put ingredients and food alerts in quotation " " symbols with NO comma. If unsure, call programmer.'
            
            try:
                # check in case comments in menu.txt file
                self.raw_menu_file.remove(menu_txt_comment_1)
                self.raw_menu_file.remove(menu_txt_comment_2)
                
            except ValueError:
                # in case sushi manager incorrectly edits sushi_takeaway_menu.txt file
                # by altering comment lines
                # error message shows up with problem user encounters and solution to solve
                self.menu_txt_error_msg = Label(self.takeaway_frame, text="Error: Error in text file.\n\nPlease contact Sushi Takeaway at [phone number]", font=self.large_font, bg=self.bg_color, fg=self.error_font_color, justify="center")
                self.menu_txt_error_msg.grid(row=0)            
                
            else:   
                
                # what about: for food in len(self.raw_menu_file.split(", "):
                #                 self.raw_menu_file[0] = self.food1
                
                
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
                
                self.name_instructions_text = "This is for identificaton purposes only. You can type either your first name or your initials."
                
                # a separate frame to contain history and information buttons
                self.top_buttons_frame = Frame(self.takeaway_frame, bg=self.bg_color)
                self.top_buttons_frame.grid(row=0, pady=5)
                
                # add History and Information button widgets
                self.history_button = Button(self.top_buttons_frame, text="History", fg=self.font_color, bg=self.btn_bg_color, font=self.small_heading_font, width=self.btn_width, height=self.btn_height, command=self.open_history)
                self.history_button.grid(row=0, column=0, padx=10)
                
                self.information_button = Button(self.top_buttons_frame, text="Information", fg=self.font_color, bg=self.btn_bg_color, font=self.small_heading_font, width=self.btn_width, height=self.btn_height, command=self.open_information)
                self.information_button.grid(row=0, column=1, padx=10)        
                
                self.takeaway_heading = Label(self.takeaway_frame, text="Welcome to Sushi Takeaway", font=self.large_font, fg=self.font_color, bg=self.bg_color, justify="center")
                self.takeaway_heading.grid(row=1)
                
                # self.takeaway_description scrapped because same function but better in Information !!
                
                # provide instructions for users how to open Details GUI
                self.takeaway_instruction = Label(self.takeaway_frame, text="Come and see our wares!   The maximum amount per food is 100.", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.takeaway_instruction.grid(row=2) # may have to change this: no Details GUI !!
                
                # A frame to hold all food items like a menu
                self.menu_frame = Frame(self.takeaway_frame, bg=self.bg_color)
                self.menu_frame.grid(row=3, padx=5)
                
                # Contains one food dish and its general details without ingredients and food alerts
                # LabelFrame for displaying food name and put its details in visual box
                self.food1_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food1[0].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food1_frame.grid(row=0, column=0, sticky="E"+"W")
                # sticky tells that this labelframe has maximum area in its grid in menu_frame
                
                self.food1_image_label = Label(self.food1_frame, image=self.food1_image, bg=self.bg_color, width="100")
                self.food1_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food1_price_label = Label(self.food1_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food1_price_label.grid(row=1, column=0)        
                
                self.food1_price = Label(self.food1_frame, text=self.food1[2].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food1_price.grid(row=1, column=1)
                
                self.food1_quantity_label = Label(self.food1_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food1_quantity_label.grid(row=2, column=0)
                
                self.food1_quantity = StringVar(value=0)
                # max food quantity is 100 because sushi takeaway is equipped to cater
                # for only individuals and small groups up to 10 people
                # wrap is True so bulk-buyers can go to maximum amount in one click
                self.food1_quantity_spinbox = Spinbox(self.food1_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food1_quantity, justify="center", width=4, wrap=True)
                self.food1_quantity_spinbox.grid(row=2, column=1)
                
                # foods 2-8 are replica of food 1, but with unique foods and details from sushi_takeaway_menu.txt file
                self.food2_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food2[0].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food2_frame.grid(row=0, column=1, sticky="E"+"W")
                
                self.food2_image_label = Label(self.food2_frame, image=self.food2_image, bg=self.bg_color, width="100", anchor="center")
                self.food2_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food2_price_label = Label(self.food2_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food2_price_label.grid(row=1, column=0)        
                
                self.food2_price = Label(self.food2_frame, text=self.food2[2].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food2_price.grid(row=1, column=1)
                
                self.food2_quantity_label = Label(self.food2_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food2_quantity_label.grid(row=2, column=0)
                
                self.food2_quantity = StringVar(value=0)
                self.food2_quantity_spinbox = Spinbox(self.food2_frame, from_=0, to=100, increment="1",format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food2_quantity, justify="center", width=4, wrap=True)
                self.food2_quantity_spinbox.grid(row=2, column=1)        
                
                self.food3_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food3[0].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food3_frame.grid(row=0, column=2, sticky="E"+"W")
                
                self.food3_image_label = Label(self.food3_frame, image=self.food3_image, bg=self.bg_color, width="100", anchor="center")
                self.food3_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food3_price_label = Label(self.food3_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food3_price_label.grid(row=1, column=0)        
                
                self.food3_price = Label(self.food3_frame, text=self.food3[2 ].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food3_price.grid(row=1, column=1)
                
                self.food3_quantity_label = Label(self.food3_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food3_quantity_label.grid(row=2, column=0)
                
                self.food3_quantity = StringVar(value=0)
                self.food3_quantity_spinbox = Spinbox(self.food3_frame, from_=0, to=100, increment="1",format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food3_quantity, justify="center", width=4, wrap=True)
                self.food3_quantity_spinbox.grid(row=2, column=1)          
                
                self.food4_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food4[0 ].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food4_frame.grid(row=0, column=3, sticky="E"+"W") 
                
                self.food4_image_label = Label(self.food4_frame, image=self.food4_image, bg=self.bg_color, width="100", anchor="center")
                self.food4_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food4_price_label = Label(self.food4_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food4_price_label.grid(row=1, column=0)        
                
                self.food4_price = Label(self.food4_frame, text=self.food4[2 ].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food4_price.grid(row=1, column=1)
                
                self.food4_quantity_label = Label(self.food4_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food4_quantity_label.grid(row=2, column=0)
                
                self.food4_quantity = StringVar(value=0)
                self.food4_quantity_spinbox = Spinbox(self.food4_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food4_quantity, justify="center", width=4, wrap=True)
                self.food4_quantity_spinbox.grid(row=2, column=1)          
                
                self.food5_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food5[0 ].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food5_frame.grid(row=1, column=0, sticky="E"+"W")
                
                self.food5_image_label = Label(self.food5_frame, image=self.food5_image, bg=self.bg_color, width="100", anchor="center")
                self.food5_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food5_price_label = Label(self.food5_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food5_price_label.grid(row=1, column=0)        
                
                self.food5_price = Label(self.food5_frame, text=self.food5[2 ].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food5_price.grid(row=1, column=1)
                
                self.food5_quantity_label = Label(self.food5_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food5_quantity_label.grid(row=2, column=0)
                
                self.food5_quantity = StringVar(value=0)
                self.food5_quantity_spinbox = Spinbox(self.food5_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food5_quantity, justify="center", width=4, wrap=True)
                self.food5_quantity_spinbox.grid(row=2, column=1)          
                
                self.food6_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food6[0 ].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food6_frame.grid(row=1, column=1, sticky="E"+"W") 
                
                self.food6_image_label = Label(self.food6_frame, image=self.food6_image, bg=self.bg_color, width="100", anchor="center")
                self.food6_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food6_price_label = Label(self.food6_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food6_price_label.grid(row=1, column=0)        
                
                self.food6_price = Label(self.food6_frame, text=self.food6[2].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food6_price.grid(row=1, column=1)
                
                self.food6_quantity_label = Label(self.food6_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food6_quantity_label.grid(row=2, column=0)
                
                self.food6_quantity = StringVar(value=0)
                self.food6_quantity_spinbox = Spinbox(self.food6_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food6_quantity, justify="center", width=4, wrap=True)
                self.food6_quantity_spinbox.grid(row=2, column=1)          
                
                self.food7_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food7[0 ].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food7_frame.grid(row=1, column=2, sticky="E"+"W") 
                
                self.food7_image_label = Label(self.food7_frame, image=self.food7_image, bg=self.bg_color, width="100", anchor="center")
                self.food7_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food7_price_label = Label(self.food7_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food7_price_label.grid(row=1, column=0)        
                
                self.food7_price = Label(self.food7_frame, text=self.food7[2 ].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food7_price.grid(row=1, column=1)
                
                self.food7_quantity_label = Label(self.food7_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food7_quantity_label.grid(row=2, column=0)
                
                self.food7_quantity = StringVar(value=0)
                self.food7_quantity_spinbox = Spinbox(self.food7_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food7_quantity, justify="center", width=4, wrap=True)
                self.food7_quantity_spinbox.grid(row=2, column=1)          
                
                self.food8_frame = LabelFrame(self.menu_frame, bg=self.bg_color, text=self.food8[0 ].strip().capitalize(), font=self.normal_font, fg=self.font_color, labelanchor="n")
                self.food8_frame.grid(row=1, column=3, sticky="E"+"W")         
                
                self.food8_image_label = Label(self.food8_frame, image=self.food8_image, bg=self.bg_color, width="100", anchor="center")
                self.food8_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food8_price_label = Label(self.food8_frame, text="Price:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food8_price_label.grid(row=1, column=0)        
                
                self.food8_price = Label(self.food8_frame, text=self.food8[2 ].strip(), bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food8_price.grid(row=1, column=1)
                
                self.food8_quantity_label = Label(self.food8_frame, text="Amount:", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.food8_quantity_label.grid(row=2, column=0)
                
                self.food8_quantity = StringVar(value=0)
                self.food8_quantity_spinbox = Spinbox(self.food8_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.font_color, font=self.normal_font, textvariable=self.food8_quantity, justify="center", width=4, wrap=True)
                self.food8_quantity_spinbox.grid(row=2, column=1)          
                
                # button to check food quantity and show total price
                self.calculate_total_btn = Button(self.menu_frame, text="Show total price: ", bg=self.btn_bg_color, fg=self.font_color, font=self.small_heading_font, width=self.btn_width, height=self.btn_height, command=self.show_total_price)
                self.calculate_total_btn.grid(row=3, column=0, columnspan=2, sticky="E", pady=5, padx=10)
                
                self.total_price_label = Label(self.menu_frame, text="$0.00", bg=self.bg_color, fg=self.font_color, font=self.small_heading_font, justify="center")
                self.total_price_label.grid(row=3, column=2, sticky="E"+"W")
                
                
                # Create frame for user's name input indentification purpose 
                self.name_frame = LabelFrame(self.takeaway_frame, bg=self.bg_color, text="Identification purposes only", font=self.small_heading_font, fg=self.font_color)
                self.name_frame.grid(row=4, padx=5, pady=5)
                    
                self.name_label = Label(self.name_frame, text="Name: ", bg=self.bg_color, fg=self.font_color, font=self.normal_font)
                self.name_label.grid(row=0, column=0, pady=5)
                
                self.user_name = StringVar()
                self.name_textbox = Entry(self.name_frame, font=self.font_color, bg="white", fg=self.font_color, textvariable=self.user_name)
                self.name_textbox.grid(row=0, column=1, pady=5)
                
                # This widget stays in name_frame as it is related
                self.name_instructions_label = Label(self.name_frame, text=self.name_instructions_text, fg=self.font_color, bg=self.bg_color, font=self.normal_font, wraplength="400")
                self.name_instructions_label.grid(row=1, column=0, columnspan=2, pady=5)
                
                self.bottom_buttons_frame = Frame(self.takeaway_frame, bg=self.bg_color)
                self.bottom_buttons_frame.grid(row=5, pady=10)
                
                self.order_button = Button(self.bottom_buttons_frame, text="Order", font=self.small_heading_font, bg=self.btn_bg_color, fg=self.font_color, width=self.btn_width, height=self.btn_height, command=self.order)
                self.order_button.grid(row=0, column=0, padx=5)
                
                self.cancel_order_button = Button(self.bottom_buttons_frame, text="Cancel order", font=self.small_heading_font, bg=self.btn_bg_color, fg=self.font_color, width=self.btn_width, height=self.btn_height, command=self.cancel_order)
                self.cancel_order_button.grid(row=0, column=1, padx=5)
                
                self.exit_takeaway_button = Button(self.bottom_buttons_frame, text="Exit Programme", font=self.small_heading_font, bg=self.btn_bg_color, fg=self.font_color, width = "26", height=self.btn_height, command=quit)
                self.exit_takeaway_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
                

    def open_history(self):
        pass
    
    def open_information(self):
        pass
    
    def show_total_price(self):
        # check whether quantity of all 8 foods are valid
        food_has_error, error_feedback = self.check_food_quantity()
        total_price = 0
        
        if food_has_error != 0:
            # when there is a problem with food quantity
            self.total_price_label.config(text=error_feedback, bg=self.error_bg_color, fg=self.error_font_color, font=self.normal_font, wraplength="200")
            
        else:
            # when there is no problem
            food1_price = int(self.food1_quantity.get()) * float(self.food1[2])
            food2_price = int(self.food2_quantity.get()) * float(self.food2[2])
            food3_price = int(self.food3_quantity.get()) * float(self.food3[2])
            food4_price = int(self.food4_quantity.get()) * float(self.food4[2])
            food5_price = int(self.food5_quantity.get()) * float(self.food5[2])
            food6_price = int(self.food6_quantity.get()) * float(self.food6[2])
            food7_price = int(self.food7_quantity.get()) * float(self.food7[2])
            food8_price = int(self.food8_quantity.get()) * float(self.food8[2])

            total_price = food1_price + food2_price + food3_price + food4_price + food5_price + food6_price + food7_price + food8_price
            
            self.total_price_label.config(text="${:.2f}".format(total_price), bg=self.bg_color, fg=self.font_color, font=self.small_heading_font)
    
            
        
    def check_food_quantity(self):
        # in case of user typing food quantity in textbox of spinbox, this functions 
        # checks whether the food quantity value is valid
        # this process is lengthy because I couldn't find a better working way to approach the situation
        
        # food_has_error variable stores food item's order to later address in an error message 
        food_has_error = 0
        problem_result = ""
        
        # only whole numbers 0-100 is accepted:
        # food quantity is stripped to remove spaces in front or back of number that can
        # make the condition below return False - we want to find True
        
        # this variable stores the number that is currently checked - to reduce complexity of function
        num_checking = self.food1_quantity.get().strip()
        if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
            food_has_error = 1
            problem_result = self.find_error(num_checking, "[0-9 ]")
            self.food1_quantity_spinbox.config(bg=self.error_bg_color)
            
        else:
            # if 1st food's quantity has no error
            # 1st food spinbox's background color is reset
            self.food1_quantity_spinbox.config(bg="#FFFFFF")
            
            num_checking = self.food2_quantity.get().strip()
            if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                food_has_error = 2
                problem_result = self.find_error(num_checking, "[0-9 ]")
                self.food2_quantity_spinbox.config(bg=self.error_bg_color)
                
            else:
                # if 2nd food's quantity has no error
                self.food2_quantity_spinbox.config(bg="#FFFFFF")
                
                num_checking = self.food3_quantity.get().strip()
                if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                    food_has_error = 3
                    problem_result = self.find_error(num_checking, "[0-9 ]")
                    self.food3_quantity_spinbox.config(bg=self.error_bg_color)
                    
                else:
                    # if 3rd food's quantity has no error
                    self.food3_quantity_spinbox.config(bg="#FFFFFF")
                    
                    num_checking = self.food4_quantity.get().strip()
                    if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                        food_has_error = 4
                        problem_result = self.find_error(num_checking, "[0-9 ]")
                        self.food4_quantity_spinbox.config(bg=self.error_bg_color)
                    
                    else:
                    # if 4th food's quantity has no error
                        self.food4_quantity_spinbox.config(bg="#FFFFFF")
                        
                        num_checking = self.food5_quantity.get().strip()
                        if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                            food_has_error = 5
                            problem_result = self.find_error(num_checking, "[0-9 ]")
                            self.food5_quantity_spinbox.config(bg=self.error_bg_color)
                    
                        else:
                            # if 5th food's quantity has no error
                            self.food5_quantity_spinbox.config(bg="#FFFFFF")
                            
                            num_checking = self.food6_quantity.get().strip()
                            if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                                food_has_error = 6
                                problem_result = self.find_error(num_checking, "[0-9 ]")
                                self.food6_quantity_spinbox.config(bg=self.error_bg_color)
                    
                            else:
                                # if 6th food's quantity has no error
                                self.food6_quantity_spinbox.config(bg="#FFFFFF")
                                
                                num_checking = self.food7_quantity.get().strip()
                                if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                                    food_has_error = 7
                                    problem_result = self.find_error(num_checking, "[0-9 ]")
                                    self.food7_quantity_spinbox.config(bg=self.error_bg_color)
                    
                                else:
                                    # if 7th food's quantity has no error
                                    self.food7_quantity_spinbox.config(bg="#FFFFFF")
                                    
                                    num_checking = self.food8_quantity.get().strip()
                                    if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                                        food_has_error = 8
                                        problem_result = self.find_error(num_checking, "[0-9 ]")
                                        self.food8_quantity_spinbox.config(bg=self.error_bg_color)
                        
                                    else:
                                        # if 8th food's quantity has no error
                                        self.food8_quantity_spinbox.config(bg="#FFFFFF")
                                        
        error_feedback = f"{problem_result} Only whole numbers from 1-100 accepted."
        return food_has_error, error_feedback
        
    def find_error(self, error_string, valid_char):
        problem = ""
        for char in error_string.strip():
            if re.match (valid_char, char):
                continue
            
            else:
                problem = f"Sorry, no {char} is allowed."
            break
            
        return problem
                
    
    def order(self):
        # in case the user doesn't press the 'show price' button, pressing order button would automatically 
        # check foods' quantities validity and show the order's price 
        self.show_total_price()
        
        # check's user's input name for validity
        if self.user_name.get() == "":
            # if user didn't input name
            self.name_instructions_label.config(text="Please fill in your name", bg=self.error_bg_color, fg=self.error_font_color, font=self.small_heading_font)
            self.name_textbox.config(bg=self.error_bg_color)
        else:
            # check whether name that user puts in is valid
            name_problem_result = self.find_error(self.user_name.get(), "[A-Za-z. ]")
            if name_problem_result != "" :
                # there is a problem with user's input name
                self.name_instructions_label.config(text=name_problem_result, bg=self.error_bg_color, fg=self.error_font_color, font=self.small_heading_font) 
                self.name_textbox.config(bg=self.error_bg_color)
            else:
                # there is no problem so name instructions are returned to normal
                self.name_instructions_label.config(text=self.name_instructions_text, fg=self.font_color, bg=self.bg_color, font=self.normal_font, wraplength="400")
                self.name_textbox.config(bg="#FFFFFF")
                
                # use history.txt file by add, otherwise error
    
    def cancel_order(self):
        # reset foods' quantities and color of spinboxes
        self.food1_quantity.set("0")
        self.food1_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        self.food2_quantity.set("0")
        self.food2_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        self.food3_quantity.set("0")
        self.food3_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        self.food4_quantity.set("0")
        self.food4_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        self.food5_quantity.set("0")
        self.food5_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        self.food6_quantity.set("0")
        self.food6_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")  
        self.food7_quantity.set("0")
        self.food7_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        self.food8_quantity.set("0")
        self.food8_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")  
        
        # reset name textbox and instructions label underneath
        self.name_instructions_label.config(text=self.name_instructions_text, fg=self.font_color, bg=self.bg_color, font=self.normal_font, wraplength="400")
        self.name_textbox.config(bg="#FFFFFF")
        self.user_name.set("")
    
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
