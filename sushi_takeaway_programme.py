""" This programme lets user choose types of food, type in user's name, and order
food. Past orders can be seen in History GUI. If unsatisfactory, users can
cancel order. Information GUI tells users how to use programme. Details GUI
shows more details about the food when user clicks on image of one food.
"""
# version 1 testing: Takeaway GUI
# This GUI is the main GUI of the programme.
# Information GUI and History GUI can be accessed from this GUI

# Import all needed libraries for the programme
import os
os.system('cmd /c "pip install Pillow"')
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import tkinter.scrolledtext as st
from datetime import date, datetime
import re


class Takeaway:
    """ This GUI displays all information about the Sushi Takeaway
    """
    
    def __init__(self):
        """Initialising variables and setting up Takeaway GUI
        """ 
        
        # init_vars dictionary stores common formats of the programme
        self.init_vars = {
        # large fonts are found in headings,  medium fonts are found in buttons
        # and error messages, the rest are normal fonts
                          "normal_font" : "Helvetica 12", 
                          "medium_font" : "Helvetica 14 bold",
                          "large_font" : "Helvetica 17 bold",
                          
        
        # background, button and error components use colour-blind friendly 
        # color palette
                         "btn_bg_color" : "#7CA1CC",
                         "error_bg_color" : "#EEBAB4",
                         "bg_color" : "#A8B6CC",
                         "error_font_color" : "#F05039",
                         "font_color" : "#141414",
        
        # height and weight variables for almost all buttons' size in programme
                         "btn_width" : "16",
                         "btn_height" : "0"}
        
        # set up main GUI frame
        self.takeaway_frame = Frame(padx = 10, bg=self.init_vars["bg_color"])
        self.takeaway_frame.grid()
        
        # builing Takeaway GUI with widgets
        # a separate frame to contain history and information buttons
        self.top_buttons_frame = Frame(self.takeaway_frame, bg=self.init_vars["bg_color"])
        self.top_buttons_frame.grid(row=0, pady=5)
        
        # add History and Information button widgets into top button frame
        # to seprate from rest of GUI programme
        self.history_button = Button(self.top_buttons_frame, text="History", fg=self.init_vars["font_color"], bg=self.init_vars["btn_bg_color"], font=self.init_vars["medium_font"], width=self.init_vars["btn_width"], height=self.init_vars["btn_height"], command=self.open_history)
        self.history_button.grid(row=0, column=0, padx=10)
        
        self.information_button = Button(self.top_buttons_frame, text="Information", fg=self.init_vars["font_color"], bg=self.init_vars["btn_bg_color"], font=self.init_vars["medium_font"], width=self.init_vars["btn_width"], height=self.init_vars["btn_height"], command=self.open_information)
        self.information_button.grid(row=0, column=1, padx=10)        
        
        # heading and instructions for introducing users to the GUI and how to use it
        self.takeaway_heading = Label(self.takeaway_frame, text="Welcome to Sushi Takeaway", font=self.init_vars["large_font"], fg=self.init_vars["font_color"], bg=self.init_vars["bg_color"], justify="center")
        self.takeaway_heading.grid(row=1)
        
        self.takeaway_instruction = Label(self.takeaway_frame, text="Come and see our wares!   The maximum amount per food is 100.", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
        self.takeaway_instruction.grid(row=2)
        
        # A frame to hold all food items like a menu
        self.menu_frame = Frame(self.takeaway_frame, bg=self.init_vars["bg_color"])
        self.menu_frame.grid(row=3, padx=5)        
        
        try: 
            # check if sushi_takeaway_menu.txt file is available in sushi_takeaway folder
            with open("sushi_takeaway_menu.txt", "r") as menu_file:
                self.raw_menu_file = menu_file.read().split("\n")
        
        except FileNotFoundError: 
            # in case user deletes or misplaces sushi_takeaway_menu.txt file
            # an error text label appears showing problem with solution            
            self.menu_txt_error_msg = Label(self.menu_frame, text="Error: cannot find sushi_takeaway_menu.txt file.\n\nPlease re-install this programme.\n\nSushi Takeaway store information can be accessed by clicking 'Information' button at top right of programme. We are sorry for the inconvenience.", font=self.init_vars["large_font"], bg=self.init_vars["bg_color"], fg=self.init_vars["error_font_color"], wraplength="670")
            self.menu_txt_error_msg.grid(row=0, column=0)
            
            # error message is in menu frame so that if there is any issue, user 
            # can go to Information GUI for access of aTkeaway store's phone 
            # number and store location
        
        else:
            # if menu.txt file is available
            
            # commnents are directly removed word by word, in case the text file is # edited incorrectly by takeaway manager or user, and may cause 
            # programme to work incorrectly
            
            menu_txt_comment_1 = '# Follow this format: food name, food image name, price, "ingredients", "food and allergy alerts". Do NOT touch these two hashtag # lines. Max 8 food items.'
            
            menu_txt_comment_2 = '# Please put comma , between every part and put ingredients and food alerts in quotation " " symbols with NO comma. If unsure, call programmer.'
            
            try:
                # check in case comments in menu.txt file don't match
                self.raw_menu_file.remove(menu_txt_comment_1)
                self.raw_menu_file.remove(menu_txt_comment_2)
                
            except ValueError:
                # in case comment lines are altered and may cause programme 
                # unable to run
                # error message shows up with problem encountered and solution
                self.menu_txt_error_msg = Label(self.menu_frame, text="Error in menu text file.\n\nPlease contact us to solve the problem. Sushi takeaway store information can be accessed by clicking 'Information' button at top right of programme.\n\nWe are sorry for the inconvenience.", font=self.init_vars["large_font"], bg=self.init_vars["bg_color"], fg=self.init_vars["error_font_color"], justify="center", wraplength="670")
                self.menu_txt_error_msg.grid(row=0)            
                
            else:   
                # create food1 profile as a list for the 1st food item
                # with food name, price, image name and ingredients as items of list
                self.food1 = self.raw_menu_file[0].split(", ")
                # set up food1 name
                self.food1_name = self.food1[0]
                
                # set up image path of food 1 for later implementing in widgets
                # strip function for image name in case there are white spaces around string
                self.food1_image_path = "images/" + self.food1[1].strip()
                self.food1_image = ImageTk.PhotoImage(Image.open(self.food1_image_path).resize((90, 90)))
                
                # foods 2-8 are implemented same way as food 1
                self.food2 = self.raw_menu_file[1].split(", ")
                self.food2_name = self.food2[0]
                
                self.food2_image_path = "images/" + self.food2[1].strip()
                self.food2_image = ImageTk.PhotoImage(Image.open(self.food2_image_path).resize((90, 90)))        
                
                self.food3 = self.raw_menu_file[2].split(", ")
                self.food3_name = self.food3[0]
                
                self.food3_image_path = "images/" + self.food3[1].strip()
                self.food3_image = ImageTk.PhotoImage(Image.open(self.food3_image_path).resize((90, 90)))
                
                self.food4 = self.raw_menu_file[3].split(", ")
                self.food4_name = self.food4[0]
                
                self.food4_image_path = "images/" + self.food4[1].strip()
                self.food4_image = ImageTk.PhotoImage(Image.open(self.food4_image_path).resize((90, 90)))
                
                self.food5 = self.raw_menu_file[4].split(", ")
                self.food5_name = self.food5[0]
                
                self.food5_image_path = "images/" + self.food5[1].strip()
                self.food5_image = ImageTk.PhotoImage(Image.open(self.food5_image_path).resize((90, 90)))     
                
                self.food6 = self.raw_menu_file[5].split(", ")
                self.food6_name = self.food6[0]
                
                self.food6_image_path = "images/" + self.food6[1].strip()
                self.food6_image = ImageTk.PhotoImage(Image.open(self.food6_image_path).resize((90, 90))) 
                
                self.food7 = self.raw_menu_file[6].split(", ")
                self.food7_name = self.food7[0]
                
                self.food7_image_path = "images/" + self.food7[1].strip()
                self.food7_image = ImageTk.PhotoImage(Image.open(self.food7_image_path).resize((90, 90))) 
                
                self.food8 = self.raw_menu_file[7].split(", ")
                self.food8_name = self.food8[0]
                
                self.food8_image_path = "images/" + self.food8[1].strip()
                self.food8_image = ImageTk.PhotoImage(Image.open(self.food8_image_path).resize((90, 90)))
                
                # create list containing 8 foods' names for later use in a function
                self.food_name_list =  [self.food1_name, self.food2_name, self.food3_name, self.food4_name, self.food5_name, self.food6_name, self.food7_name, self.food8_name]      
                
                # Contains one food dish and its name, image and price
                # LabelFrame used for displaying food name and put its details in 
                # a box so users have easier time processing output of GUI
                self.food1_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food1[0].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food1_frame.grid(row=0, column=0, sticky="E"+"W")
                # this sticky tells that this labelframe has maximum area in its 
                # grid in menu_frame
                
                # image path of food1 is put in Label widget to display image
                self.food1_image_label = Label(self.food1_frame, image=self.food1_image, bg=self.init_vars["bg_color"], width="100")
                self.food1_image_label.grid(row=0, column=0, columnspan=2)
                
                # price of food1 is shown with label "price: "
                self.food1_price_label = Label(self.food1_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food1_price_label.grid(row=1, column=0)        
                
                self.food1_price = Label(self.food1_frame, text=self.food1[2].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food1_price.grid(row=1, column=1)
                
                # food quantity is shown in sipnbox, with both textbox and buttons
                # features for user to change food quantity to order
                self.food1_quantity_label = Label(self.food1_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food1_quantity_label.grid(row=2, column=0)
                
                # default food quantity is set to '0'
                self.food1_quantity = StringVar(value=0)
                # max food quantity is 100 because sushi takeaway is equipped to # cater for mostly individuals and small groups up to 10 people
                
                # wrap is True so bulk-buyers can go to maximum amount in one 
                # click on down button, or they can type in "100" in textbox
                self.food1_quantity_spinbox = Spinbox(self.food1_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food1_quantity, justify="center", width=4, wrap=True)
                self.food1_quantity_spinbox.grid(row=2, column=1)
                
                # foods 2-8 are replica of food 1, but with unique foods and details from sushi_takeaway_menu.txt file
                # and labelledframe rows and columns are unique in menu frame grid
                self.food2_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food2[0].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food2_frame.grid(row=0, column=1, sticky="E"+"W")
                
                self.food2_image_label = Label(self.food2_frame, image=self.food2_image, bg=self.init_vars["bg_color"], width="100", anchor="center")
                self.food2_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food2_price_label = Label(self.food2_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food2_price_label.grid(row=1, column=0)        
                
                self.food2_price = Label(self.food2_frame, text=self.food2[2].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food2_price.grid(row=1, column=1)
                
                self.food2_quantity_label = Label(self.food2_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food2_quantity_label.grid(row=2, column=0)
                
                self.food2_quantity = StringVar(value=0)
                self.food2_quantity_spinbox = Spinbox(self.food2_frame, from_=0, to=100, increment="1",format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food2_quantity, justify="center", width=4, wrap=True)
                self.food2_quantity_spinbox.grid(row=2, column=1)        
                
                self.food3_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food3[0].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food3_frame.grid(row=0, column=2, sticky="E"+"W")
                
                self.food3_image_label = Label(self.food3_frame, image=self.food3_image, bg=self.init_vars["bg_color"], width="100", anchor="center")
                self.food3_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food3_price_label = Label(self.food3_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food3_price_label.grid(row=1, column=0)        
                
                self.food3_price = Label(self.food3_frame, text=self.food3[2 ].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food3_price.grid(row=1, column=1)
                
                self.food3_quantity_label = Label(self.food3_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food3_quantity_label.grid(row=2, column=0)
                
                self.food3_quantity = StringVar(value=0)
                self.food3_quantity_spinbox = Spinbox(self.food3_frame, from_=0, to=100, increment="1",format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food3_quantity, justify="center", width=4, wrap=True)
                self.food3_quantity_spinbox.grid(row=2, column=1)          
                
                self.food4_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food4[0 ].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food4_frame.grid(row=0, column=3, sticky="E"+"W") 
                
                self.food4_image_label = Label(self.food4_frame, image=self.food4_image, bg=self.init_vars["bg_color"], width="100", anchor="center")
                self.food4_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food4_price_label = Label(self.food4_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food4_price_label.grid(row=1, column=0)        
                
                self.food4_price = Label(self.food4_frame, text=self.food4[2 ].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food4_price.grid(row=1, column=1)
                
                self.food4_quantity_label = Label(self.food4_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food4_quantity_label.grid(row=2, column=0)
                
                self.food4_quantity = StringVar(value=0)
                self.food4_quantity_spinbox = Spinbox(self.food4_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food4_quantity, justify="center", width=4, wrap=True)
                self.food4_quantity_spinbox.grid(row=2, column=1)          
                
                self.food5_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food5[0 ].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food5_frame.grid(row=1, column=0, sticky="E"+"W")
                
                self.food5_image_label = Label(self.food5_frame, image=self.food5_image, bg=self.init_vars["bg_color"], width="100", anchor="center")
                self.food5_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food5_price_label = Label(self.food5_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food5_price_label.grid(row=1, column=0)        
                
                self.food5_price = Label(self.food5_frame, text=self.food5[2 ].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food5_price.grid(row=1, column=1)
                
                self.food5_quantity_label = Label(self.food5_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food5_quantity_label.grid(row=2, column=0)
                
                self.food5_quantity = StringVar(value=0)
                self.food5_quantity_spinbox = Spinbox(self.food5_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food5_quantity, justify="center", width=4, wrap=True)
                self.food5_quantity_spinbox.grid(row=2, column=1)          
                
                self.food6_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food6[0 ].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food6_frame.grid(row=1, column=1, sticky="E"+"W") 
                
                self.food6_image_label = Label(self.food6_frame, image=self.food6_image, bg=self.init_vars["bg_color"], width="100", anchor="center")
                self.food6_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food6_price_label = Label(self.food6_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food6_price_label.grid(row=1, column=0)        
                
                self.food6_price = Label(self.food6_frame, text=self.food6[2].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food6_price.grid(row=1, column=1)
                
                self.food6_quantity_label = Label(self.food6_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food6_quantity_label.grid(row=2, column=0)
                
                self.food6_quantity = StringVar(value=0)
                self.food6_quantity_spinbox = Spinbox(self.food6_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food6_quantity, justify="center", width=4, wrap=True)
                self.food6_quantity_spinbox.grid(row=2, column=1)          
                
                self.food7_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food7[0 ].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food7_frame.grid(row=1, column=2, sticky="E"+"W") 
                
                self.food7_image_label = Label(self.food7_frame, image=self.food7_image, bg=self.init_vars["bg_color"], width="100", anchor="center")
                self.food7_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food7_price_label = Label(self.food7_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food7_price_label.grid(row=1, column=0)        
                
                self.food7_price = Label(self.food7_frame, text=self.food7[2 ].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food7_price.grid(row=1, column=1)
                
                self.food7_quantity_label = Label(self.food7_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food7_quantity_label.grid(row=2, column=0)
                
                self.food7_quantity = StringVar(value=0)
                self.food7_quantity_spinbox = Spinbox(self.food7_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food7_quantity, justify="center", width=4, wrap=True)
                self.food7_quantity_spinbox.grid(row=2, column=1)          
                
                self.food8_frame = LabelFrame(self.menu_frame, bg=self.init_vars["bg_color"], text=self.food8[0 ].strip().capitalize(), font=self.init_vars["normal_font"], fg=self.init_vars["font_color"], labelanchor="n")
                self.food8_frame.grid(row=1, column=3, sticky="E"+"W")         
                
                self.food8_image_label = Label(self.food8_frame, image=self.food8_image, bg=self.init_vars["bg_color"], width="100", anchor="center")
                self.food8_image_label.grid(row=0, column=0, columnspan=2)
                
                self.food8_price_label = Label(self.food8_frame, text="Price:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food8_price_label.grid(row=1, column=0)        
                
                self.food8_price = Label(self.food8_frame, text=self.food8[2 ].strip(), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food8_price.grid(row=1, column=1)
                
                self.food8_quantity_label = Label(self.food8_frame, text="Amount:", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.food8_quantity_label.grid(row=2, column=0)
                
                self.food8_quantity = StringVar(value=0)
                self.food8_quantity_spinbox = Spinbox(self.food8_frame, from_=0, to=100, increment="1", format="%3.0f", fg=self.init_vars["font_color"], font=self.init_vars["normal_font"], textvariable=self.food8_quantity, justify="center", width=4, wrap=True)
                self.food8_quantity_spinbox.grid(row=2, column=1)          
                
                # button to check food quantity and show total price
                self.calculate_total_btn = Button(self.menu_frame, text="Show total price: ", bg=self.init_vars["btn_bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["medium_font"], width=self.init_vars["btn_width"], height=self.init_vars["btn_height"], command=self.show_total_price)
                self.calculate_total_btn.grid(row=3, column=0, columnspan=2, sticky="E", pady=5, padx=10)
                
                # price is shown with medium font to stand out, and rounded to 
                # 2 decimal places like real life prices
                self.total_price_label = Label(self.menu_frame, text="$0.00", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["medium_font"], justify="center")
                self.total_price_label.grid(row=3, column=2, sticky="E"+"W")
                
                # Create frame for user's name input for indentification purposes
                self.name_frame = LabelFrame(self.takeaway_frame, bg=self.init_vars["bg_color"], text="Identification purposes only", font=self.init_vars["medium_font"], fg=self.init_vars["font_color"])
                self.name_frame.grid(row=4, padx=5)
                
                # texttbox for users to put their names, and label "name: " for
                # user's recognition of where to input
                self.name_label = Label(self.name_frame, text="Name: ", bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["normal_font"])
                self.name_label.grid(row=0, column=0, pady=5)
                
                # user_name variable used to store input
                self.user_name = StringVar()
                self.name_textbox = Entry(self.name_frame, font=self.init_vars["font_color"], bg="white", fg=self.init_vars["font_color"], textvariable=self.user_name)
                self.name_textbox.grid(row=0, column=1, pady=5)
                
                # variable for instructions of name component of GUI
                self.name_instructions_text = "This is for identificaton purposes only. You can type either your first name or your initials."
                
                # This label widget stays in name_frame since it instructs users
                # how to enter name. Also shows error message in problem encounters
                self.name_instructions_label = Label(self.name_frame, text=self.name_instructions_text, fg=self.init_vars["font_color"], bg=self.init_vars["bg_color"], font=self.init_vars["normal_font"], wraplength="400")
                self.name_instructions_label.grid(row=1, column=0, columnspan=2, pady=5)
                
                # this label widget displays error message when problems unrelated to food quantity or user's name is encountered
                # eg. when total_price is $0 because user hasn't increased any 
                # food quantity
                self.error_order_label = Label(self.takeaway_frame, fg=self.init_vars["error_font_color"], bg=self.init_vars["bg_color"], font=self.init_vars["medium_font"], wraplength="400")
                self.error_order_label.grid(row=5)
                
                # add 'Order', 'Cancel Order' and 'Quit' button widgets into bottom 
                # button frame to seprate from rest of GUI programme
                self.bottom_buttons_frame = Frame(self.takeaway_frame, bg=self.init_vars["bg_color"])
                self.bottom_buttons_frame.grid(row=6, pady=10)
                
                # button to check all food quantities and user's name,then store 
                # order into history.txt file
                self.order_button = Button(self.bottom_buttons_frame, text="Order", font=self.init_vars["medium_font"], bg=self.init_vars["btn_bg_color"], fg=self.init_vars["font_color"], width=self.init_vars["btn_width"], height=self.init_vars["btn_height"], command=self.order)
                self.order_button.grid(row=0, column=0, padx=5)
                
                # button to reset all widgets and variables that are changeable to 
                # default values
                self.cancel_order_button = Button(self.bottom_buttons_frame, text="Cancel order", font=self.init_vars["medium_font"], bg=self.init_vars["btn_bg_color"], fg=self.init_vars["font_color"], width=self.init_vars["btn_width"], height=self.init_vars["btn_height"], command=self.cancel_order)
                self.cancel_order_button.grid(row=0, column=1, padx=5)
                
                # button to close Sushi Takeaway programme and all GUIs of it
                self.exit_takeaway_button = Button(self.takeaway_frame, text="Exit Programme", font=self.init_vars["medium_font"], bg=self.init_vars["btn_bg_color"], fg=self.init_vars["font_color"], width = "26", height=self.init_vars["btn_height"], command=quit)
                self.exit_takeaway_button.grid(row=7, padx=5)
                
    # opens History GUI with main GUI as parent parameter
    def open_history(self):
        History(self)
    
    # opens Information GUI with main GUI as parent parameter
    def open_information(self):
        Information(self)
    
    def show_total_price(self):
        # check whether quantity of all 8 foods are valid, with two returned
        # variables to report on any issues found
        quantity_error_check, error_feedback = self.check_food_quantity()
        
        # create global total price for calculations with this function and display
        # with 'order' function
        self.total_price = 0
        
        if quantity_error_check is True:
            # when there is a problem with food quantity
            self.total_price_label.config(text=error_feedback, bg=self.init_vars["error_bg_color"], fg=self.init_vars["error_font_color"], font=self.init_vars["normal_font"], wraplength="200")
            
            # return boolean value as check of food quantity validity when ordering
            return True
            
        else:
            # when there is no problem with food quantities
            # find price of each food item
            food1_price = int(self.food1_quantity.get()) * float(self.food1[2])
            food2_price = int(self.food2_quantity.get()) * float(self.food2[2])
            food3_price = int(self.food3_quantity.get()) * float(self.food3[2])
            food4_price = int(self.food4_quantity.get()) * float(self.food4[2])
            food5_price = int(self.food5_quantity.get()) * float(self.food5[2])
            food6_price = int(self.food6_quantity.get()) * float(self.food6[2])
            food7_price = int(self.food7_quantity.get()) * float(self.food7[2])
            food8_price = int(self.food8_quantity.get()) * float(self.food8[2])
            
            # find total price of order
            self.total_price = food1_price + food2_price + food3_price + food4_price + food5_price + food6_price + food7_price + food8_price
            
            # show total price on designated label
            self.total_price_label.config(text="${:.2f}".format(self.total_price), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["medium_font"])
    
            # return boolean value as check of food quantity validity when 
            # user presses 'order' button
            return False
        
        
    def check_food_quantity(self):
        # in case of user typing food quantity in textbox of spinbox, this functions 
        # checks whether the food quantity value is valid
        
        # this boolean variable tells whether food quantity has error
        quantity_has_error = False
        # this variable stores a problem found while checking food quantities
        problem_result = ""
        
        # this variable stores all food quantities for later finding which food 
        # has quantity > 1, meaning user orders that food item
        self.foods_quantities_list = []
        
        # only whole numbers 0-100 is accepted:
        # food quantity is stripped to remove spaces around number due to
        # default values surrounded by spaces
        
        # this variable stores the food quantity that is currently checked - to reduce 
        # complexity of error searching
        num_checking = self.food1_quantity.get().strip()
        # First food quantity checked is from food1
        if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
            # if quantity is not a number
            # variable shows there is an issue
            quantity_has_error = True
            # use find_error function to return fault
            problem_result = self.find_error(num_checking, "[0-9]")
            # highlight spinbox with issue red
            self.food1_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
            
        else:
            # if 1st food's quantity has no error
            # 1st food spinbox's background color is reset to white
            self.food1_quantity_spinbox.config(bg="#FFFFFF")
            # quantity addedd to quantities list
            self.foods_quantities_list.append(num_checking)
            
            # food quantities 2-8 works same as food 1
            
            # food 2 is being checked
            num_checking = self.food2_quantity.get().strip()
            if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                quantity_has_error = True
                problem_result = self.find_error(num_checking, "[0-9]")
                self.food2_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
                
            else:
                # if 2nd food's quantity has no error
                self.food2_quantity_spinbox.config(bg="#FFFFFF")
                self.foods_quantities_list.append(num_checking)
                
                # food 3 is being checked
                num_checking = self.food3_quantity.get().strip()
                if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                    quantity_has_error = True
                    problem_result = self.find_error(num_checking, "[0-9]")
                    self.food3_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
                    
                else:
                    # if 3rd food's quantity has no error
                    self.food3_quantity_spinbox.config(bg="#FFFFFF")
                    self.foods_quantities_list.append(num_checking)
                    
                    # food 4 is being checked
                    num_checking = self.food4_quantity.get().strip()
                    if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                        quantity_has_error = True
                        problem_result = self.find_error(num_checking, "[0-9]")
                        self.food4_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
                    
                    else:
                    # if 4th food's quantity has no error
                        self.food4_quantity_spinbox.config(bg="#FFFFFF")
                        self.foods_quantities_list.append(num_checking)
                        
                        # food 5 is being checked
                        num_checking = self.food5_quantity.get().strip()
                        if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                            quantity_has_error = True
                            problem_result = self.find_error(num_checking, "[0-9]")
                            self.food5_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
                    
                        else:
                            # if 5th food's quantity has no error
                            self.food5_quantity_spinbox.config(bg="#FFFFFF")
                            self.foods_quantities_list.append(num_checking)
                            
                            # food 6 is being checked
                            num_checking = self.food6_quantity.get().strip()
                            if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                                quantity_has_error = True
                                problem_result = self.find_error(num_checking, "[0-9]")
                                self.food6_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
                    
                            else:
                                # if 6th food's quantity has no error
                                self.food6_quantity_spinbox.config(bg="#FFFFFF")
                                self.foods_quantities_list.append(num_checking)
                                
                                # # food 7 is being checked
                                num_checking = self.food7_quantity.get().strip()
                                if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                                    quantity_has_error = True
                                    problem_result = self.find_error(num_checking, "[0-9]")
                                    self.food7_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
                    
                                else:
                                    # if 7th food's quantity has no error
                                    self.food7_quantity_spinbox.config(bg="#FFFFFF")
                                    self.foods_quantities_list.append(num_checking)
                                    
                                    # food 8 is being checked
                                    num_checking = self.food8_quantity.get().strip()
                                    if not num_checking.isdigit() or not 0 <= int(num_checking) <= 100:
                                        quantity_has_error = True
                                        problem_result = self.find_error(num_checking, "[0-9]")
                                        self.food8_quantity_spinbox.config(bg=self.init_vars["error_bg_color"])
                        
                                    else:
                                        # if 8th food's quantity has no error
                                        self.food8_quantity_spinbox.config(bg="#FFFFFF")
                                        self.foods_quantities_list.append(num_checking)
                                        # reset this variable to show there's no
                                        # issue with food quantities
                                        quantity_has_error = False
         
        # set feedback string with problem encountered and reuturn to 
        # original function for feedback display
        error_feedback = f"{problem_result} Only whole numbers from 1-100 accepted."
        return quantity_has_error, error_feedback
        
    def find_error(self, error_string, valid_char):
        # function that finds error of food quantity in case it contains non-numbers
        # loop searches per character of quantity to match digits 0-9, and returns
        # error found in problem string variable
        problem = ""
        for char in error_string.strip():
            if re.match (valid_char, char):
                continue
            
            else:
                problem = f"Sorry, no {char} is allowed."
            break
        
        # returns problem to previous function for error display
        return problem
                
    
    def order(self):
        # in case user doesn't press the 'show price' button before 'order' button, 
        # automatically check foods' quantities validity and show order's price 
        check_quantity_error = self.show_total_price()
        
        # check validity of user's name
        check_name_error = self.check_user_name()
        
        if check_quantity_error is False and check_name_error is False and self.total_price != 0:
            # if no error is found in user's input name, programme continues
            
            # create a string containing order's information and store in history
            # .txt file to simulate an order
            order_string_to_add = self.create_order_string()
            
            try:
                # check if sushi_takeaway_history.txt file is available in sushi_takeaway folder with 'try'
                with open("sushi_takeaway_history.txt", "r") as history_file:
                    history_file.read()  
                    
            except: 
                # in the case history.txt file is deleted or misplaced in different 
                # folder by mistake
                # error message is shown on top of menu frame, name frame and
                # order button to inform that users cannot order foods anymore
                self.error_order_label.config(text="Error encountered: cannot find sushi_takeaway_history.txt file. Please re-install the programme.\n\nSushi Takeaway store information can be accessed by clicking 'Information' button at top right of programme. We are sorry for the inconvenience.", bg=self.init_vars["error_bg_color"], wraplength="670")
                self.error_order_label.grid(row=3, rowspan=4, sticky='N' + 'S')
                # widget widget is put in rowspan from menu frame to order buttons 
                # widget is lifted to be on top of frames and buttons widgets.
                self.error_order_label.lift()
            
            else:
                # order string is added to file if history.txt can be accessed
                with open("sushi_takeaway_history.txt", "a") as history_file:
                    history_file.write(order_string_to_add)
                self.error_order_label.config(text="Order successful", bg=self.init_vars["bg_color"])                
                
        elif check_quantity_error is False and check_name_error is False and self.total_price == 0:
            # if all variables are valid but all foods quantities are still 0
            self.error_order_label.config(text="You haven't chosen any food yet! Please add some foods before ordering", bg=self.init_vars["error_bg_color"])
                    
    def check_user_name(self):
        # set up a boolean variable for later recognition of user's name error
        name_has_error = False
        
        # check's user's input name for validity
        if self.user_name.get() == "":
            # if user didn't input name
            self.name_instructions_label.config(text="Please fill in your name", bg=self.init_vars["error_bg_color"], fg=self.init_vars["error_font_color"], font=self.init_vars["medium_font"])
            self.name_textbox.config(bg=self.init_vars["error_bg_color"])
            name_has_error = True
            
        else:
            # check whether name that user puts in has error by putting in find_error function
            name_problem_result = self.find_error(self.user_name.get(), "[A-Za-z. ]")
            if name_problem_result != "" :
                # there is a problem with user's input name
                # erro message is shown where instructions for name was, and textbox
                # is highlighted red
                self.name_instructions_label.config(text=name_problem_result, bg=self.init_vars["error_bg_color"], fg=self.init_vars["error_font_color"], font=self.init_vars["medium_font"]) 
                self.name_textbox.config(bg=self.init_vars["error_bg_color"])
                # this variable shows that name inputted has error
                name_has_error = True
                
            else:
                # there is no problem so name instructions are returned to normal
                self.name_instructions_label.config(text=self.name_instructions_text, fg=self.init_vars["font_color"], bg=self.init_vars["bg_color"], font=self.init_vars["normal_font"], wraplength="400")
                self.name_textbox.config(bg="#FFFFFF")
                # this variable shows that there is no issue with name inputted
                name_has_error = False 
        
        # return boolean value as check of input name validity when ordering
        return name_has_error
    
    # retrieves date and creates DD_MM_YYYY string
    def get_date_time(self):
        # get order's date
        today = date.today()
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")
        
        # get order's time
        now = datetime.now()
        time = now.strftime("%H:%M:%S")    
        
        # function gives date and time of order in one string
        return f"{day}/{month}/{year} {time}"
    
    def create_order_string(self):
        # variable order_string is created and added with order's information 
        # before being written on history.txt file
        
        # string's order is user name, date and time of order, quantities of 
        # foods ordered, and total price
        order_string = ""
        
        # add user's name in order_string
        order_string += f"{self.user_name.get()}, "
        
        # call function to get date and time at order and add to order_string variable
        current_date_time = self.get_date_time()
        order_string += f"{current_date_time}, "
        
        # create a string variable to store foods' ordered and quantities
        foods_ordered_string = ""
        
        # this variable helps loop determine foods' names with quantities more than 0
        # when checking a list of all food quantities
        # food index starts at 0 to mimick list order numerics
        food_ordered_index = 0
        for food_quantity in self.foods_quantities_list:
            if food_quantity == "0":
                # ignore foods with quantity = 0 since they are not ordered
                # index increase 1 unit to represent which food in food list is 
                # being checked
                food_ordered_index += 1
                continue
            else:
                # add food name and quantity into foods_ordered_string variable
                foods_ordered_string += f"{self.food_name_list[food_ordered_index]} = {food_quantity}; "
                # index is added 1 to know which order of food quantity is being checked
                food_ordered_index += 1
        
        # add foods ordered string to order_string variable
        order_string += f"[{foods_ordered_string}], "
        
        # add total price to order_string variable
        order_string += f"${str(format(self.total_price, '.2f'))}\n"        
        
        # reurn order_string to be added to history.txt file
        return order_string
    
    def cancel_order(self):
        # reset foods' quantities to 0 and color of spinboxes to white of all 8 foods
        # reset food1's
        self.food1_quantity.set("0")
        self.food1_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        # reset food2's
        self.food2_quantity.set("0")
        self.food2_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        # reset food3's
        self.food3_quantity.set("0")
        self.food3_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        # reset food4's
        self.food4_quantity.set("0")
        self.food4_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        # reset food5's
        self.food5_quantity.set("0")
        self.food5_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        # reset food6's
        self.food6_quantity.set("0")
        self.food6_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        # reset food7's
        self.food7_quantity.set("0")
        self.food7_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")
        # reset food8's
        self.food8_quantity.set("0")
        self.food8_quantity_spinbox.config(bg="#FFFFFF", format="%3.0f")  
        
        # reset total price of order shown and label widget displaying the variable/error
        self.total_price = 0
        self.total_price_label.config(text="${:.2f}".format(self.total_price), bg=self.init_vars["bg_color"], fg=self.init_vars["font_color"], font=self.init_vars["medium_font"])
        
        # reset instructions label in name frame to default instructions 
        # (in case label contained error message)
        self.name_instructions_label.config(text=self.name_instructions_text, fg=self.init_vars["font_color"], bg=self.init_vars["bg_color"], font=self.init_vars["normal_font"], wraplength="400")
        # reset name textbox to blank and white background
        self.name_textbox.config(bg="#FFFFFF") # default textbox background to white
        self.user_name.set("")
        
        # reset error message label that may occur during order process
        self.error_order_label.config(fg=self.init_vars["error_font_color"], text="", bg=self.init_vars["bg_color"], font=self.init_vars["medium_font"], wraplength="400")
    
    # Terminate all GUIs of programme
    def quit(self):
        self.destroy()
    
class Information:
    """ This is the main GUI window that takes food orders from users. Two 
    buttons and images give access to three other GUIs
    """
    
    def __init__(self, partner):
        """Initialising variables and setting up Information GUI
        """ 
        # set up Information dialogue box
        self.info_box = Toplevel()
        self.info_box.title("Sushi Takeaway Information")
        
        # disable information button in Takeaway GUI when Information GUI is open
        partner.information_button.config(state=DISABLED)
        
        # If users press cross button at top right, closes Information GUI and 
        # enables information button in Takeaway GUI
        self.info_box.protocol("WM_DELETE_WINDOW", partial(self.dismiss_info_gui, partner))
        
        # set up Information GUI frame   
        self.info_frame = Frame(self.info_box, padx = 10, pady = 10, bg=partner.init_vars["bg_color"])
        self.info_frame.grid()        
        
        try: 
            # check if sushi_takeaway_information.txt file is available in sushi_takeaway folder
            with open("sushi_takeaway_information.txt", "r") as info_file:
                self.info_file = info_file.read()
        
        except FileNotFoundError: 
            # in case user deletes or misplaces sushi_takeaway_information.txt file
            # a red text label appears showing problem with solution            
            self.info_txt_error_msg = Label(self.info_frame, text="Error: cannot find sushi_takeaway_information.txt file.\n\nPlease re-install this programme.\n\nWe are sorry for the inconvenience.", font=partner.init_vars["large_font"], bg=partner.init_vars["bg_color"], fg=partner.init_vars["error_font_color"], wraplength="700")
            self.info_txt_error_msg.grid(row=0, column=0)        
        
        else:
            # if information.txt file is available
            # information GUI is set up using Tkinter widgets
            self.info_heading = Label(self.info_frame, text="Information about Sushi Takeaway", font=partner.init_vars["large_font"], fg=partner.init_vars["font_color"], bg=partner.init_vars["bg_color"])
            self.info_heading.grid(row=0, padx=5, pady=5)
            
            # label displaying the restaurant's slogan
            self.info_slogan = Label(self.info_frame, text="Come and see our wares!", font=partner.init_vars["medium_font"], fg=partner.init_vars["font_color"], bg=partner.init_vars["bg_color"])
            self.info_slogan.grid(row=1, pady=5)
            
            # displays all texts from information.txt file
            self.info_label = Label(self.info_frame, text=self.info_file, bg=partner.init_vars["bg_color"], fg=partner.init_vars["font_color"], font=partner.init_vars["normal_font"], wraplength="400", justify="left")
            self.info_label.grid(row=2)
            
        finally:
            # no matter if information text is available or not, user can close Information 
            # window with "Close window" button and then close programme, or continue ordering 
            self.close_info = Button(self.info_frame, text="Close window", bg=partner.init_vars["btn_bg_color"], fg=partner.init_vars["font_color"], font=partner.init_vars["medium_font"], command=quit, width=partner.init_vars["btn_width"], height=partner.init_vars["btn_height"])
            self.close_info.grid(row=3, padx=10, pady=10)
            
    # Terminate Information GUI
    def dismiss_info_gui(self, partner):
        partner.information_button.config(state=NORMAL)
        self.info_box.destroy()    

class History:
    """ This is the main GUI window that takes food orders from users. Two 
    buttons and images give access to three other GUIs
    """
    
    def __init__(self, partner):
        """Initialising variables and setting up Takeaway GUI
        """ 
        # set up History dialogue box
        self.history_box = Toplevel()
        self.history_box.title("Sushi Takeaway History")
        
        # disable history button in Takeaway GUI when History GUI is open
        partner.history_button.config(state=DISABLED)
        
        # If users press cross button at top right, closes History GUI and 
        # enables history button in Takeaway GUI
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.dismiss_history_gui, partner))
        
        # set up History GUI frame        
        self.history_frame = Frame(self.history_box, padx = 10, pady = 10, bg=partner.init_vars["bg_color"])
        self.history_frame.grid()        
        
        try: 
            # check if sushi_takeaway_history.txt file is available in sushi_takeaway folder
            with open("sushi_takeaway_history.txt", "r") as history_file:
                self.raw_history_file = history_file.read().split("\n")
        
        except FileNotFoundError: 
            # in case user deletes or misplaces history.txt file
            # a red text label appears showing problem with solution            
            self.history_txt_error_msg = Label(self.history_frame, text="Error: cannot find sushi_takeaway_history.txt file.\n\nPlease re-install this programme.\n\nSushi Takeaway store information can be accessed by clicking 'Information' button at top right of programme. We are sorry for the inconvenience.", font=partner.init_vars["large_font"], bg=partner.init_vars["bg_color"], fg=partner.init_vars["error_font_color"], wraplength="700")
            self.history_txt_error_msg.grid(row=0, column=0)        
        
        else:
            # if history.txt file is available
            # commnent in file is directly removed word by word, in case the text 
            # file is edited incorrectly by takeaway manager or user, and may 
            # cause programme to work incorrectly
            
            history_txt_file_comment = "# string's order is: user name, data and time of order, [quantities of foods ordered], total price"
            # this comment is a note for the restaurant to read users' orders
            
            try:
                # check in case comment in history.txt file doesn't match
                self.raw_history_file.remove(history_txt_file_comment)
            
            except ValueError:
                # in case sushi manager incorrectly edits sushi_takeaway_menu.txt file
                # by altering comment lines
                # error message shows up with problem user encounters and solution
                self.history_txt_error_msg = Label(self.history_frame, text="Error in history text file.\n\nPlease contact us to solve the problem. Sushi takeaway store information can be accessed by closing this window and clicking 'Information' button at top right of programme.\n\nWe are sorry for the inconvenience.", font=partner.init_vars["large_font"], bg=partner.init_vars["bg_color"], fg=partner.init_vars["error_font_color"], justify="center", wraplength="670")
                self.menu_txt_error_msg.grid(row=0)   
            
            else:
                # blank line at bottom of history.txt file is removed
                self.raw_history_file.pop(-1)
                
                # History GUI is set up using Tkinter widgets
                # label for heading of GUI
                self.history_heading = Label(self.history_frame, text="Past Orders on Sushi Takeaway", font=partner.init_vars["large_font"], fg=partner.init_vars["font_color"], bg=partner.init_vars["bg_color"])
                self.history_heading.grid(row=0, padx=5, pady=5)
                
                # instructions stating how to use scrolled text widget
                self.history_instructions = Label(self.history_frame, text="Below displays all past orders made from your device. Scroll down for more", font=partner.init_vars["medium_font"], fg=partner.init_vars["font_color"], bg=partner.init_vars["bg_color"], wraplength="400")
                self.history_instructions.grid(row=1, pady=5) 
                
                # set up scrolled text widget to display all past orders
                self.display_past_orders = st.ScrolledText(self.history_frame, width=40, height=5, font=partner.init_vars["normal_font"], wrap=WORD, fg=partner.init_vars["font_color"])
                self.display_past_orders.grid(row=3)

                # history of past orders are reversed to show latest orders at the top
                # in reverse-chronological order
                self.raw_history_file.reverse()
                print(self.raw_history_file)
                
                # put all past orders in a string for display
                self.display_string = ""
                for item in self.raw_history_file:
                    self.display_string += f"{item.strip()}\n"
                    # item is stripped to remove any trailing white spaces
                
                if self.display_string == "\n":
                    # if there is no past order, an error string is displayed
                    self.display_past_orders.insert(INSERT, "You have not ordered any foods... Please return once you have made at least one order. Thank you.")
                    self.display_past_orders.configure(state ='disabled', bg=partner.init_vars["error_bg_color"]) 
                    
                else:
                    # If there are past orders to be displayed
                    #  Add text into Scrolledtext and make it read only
                    self.display_past_orders.insert(INSERT, self.display_string)
                    self.display_past_orders.configure(state ='disabled', bg="#FFFFFF")
                    # resets ScrolledText background to white in case there was a previous issue
            
        finally:
            # a button to close programme is present whether there is an error or 
            # not, so users can access restaurant information and contact them
            self.close_history = Button(self.history_frame, text="Close window", bg=partner.init_vars["btn_bg_color"], fg=partner.init_vars["font_color"], font=partner.init_vars["medium_font"], command=quit, width=partner.init_vars["btn_width"], height=partner.init_vars["btn_height"])
            self.close_history.grid(row=4, padx=10, pady=10)
    
    # Terminate all GUIs
    def dismiss_history_gui(self, partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    # set up Takeaway GUI as root with title and geometry set, then run programme    
    root = Tk()
    root.title("Sushi Takeaway")
    root.geometry("670x730") 
    root.resizable(0, 0)
    Takeaway()
    root.mainloop()