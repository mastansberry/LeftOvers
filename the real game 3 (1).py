# -*- coding: utf-8 -*-
#Samuel Miserez 1/12/2017
from Tkinter import *
import Tkinter 
import random
from PIL import Image, ImageTk
import os.path
import time
#Create Window

root = Tk()
#Loads in every image
one = ImageTk.PhotoImage(file="George Washington.gif")
two = ImageTk.PhotoImage(file="John Adams.gif")
three = ImageTk.PhotoImage(file="Thomas Jefferson.gif")
four = ImageTk.PhotoImage(file="James Madison.gif")
five = ImageTk.PhotoImage(file="James Monroe.gif")
six = ImageTk.PhotoImage(file="John Quincy Adams.gif")
seven = ImageTk.PhotoImage(file="Andrew Jackson.gif")
eight = ImageTk.PhotoImage(file="Martin Van Buren.gif")
nine = ImageTk.PhotoImage(file="William Henry Harris.gif")
ten = ImageTk.PhotoImage(file="John Tyler.gif")
eleven = ImageTk.PhotoImage(file="James K Polk.gif")
twelve = ImageTk.PhotoImage(file="Zachary Taylor.gif")
thirteen = ImageTk.PhotoImage(file="Millard Fillmore.gif")
fourteen = ImageTk.PhotoImage(file="Franklin Pierce.gif")
fifteen = ImageTk.PhotoImage(file="James Buchanan.gif")
sixteen=ImageTk.PhotoImage(file="abe.gif")
seventeen = ImageTk.PhotoImage(file="Andrew Johnson.gif")
eighteen = ImageTk.PhotoImage(file="Ulysses S Grant.gif")
nineteen = ImageTk.PhotoImage(file="Rutherford B Hayes.gif")
twenty = ImageTk.PhotoImage(file="James A Garfield.gif")
twentyone = ImageTk.PhotoImage(file="Chester Arthur.gif")
twentytwo = ImageTk.PhotoImage(file="Grover Cleveland.gif")
twentythree = ImageTk.PhotoImage(file="Benjamin Harrison.gif")
twentyfour = ImageTk.PhotoImage(file="Grover Cleveland.gif")
twentyfive = ImageTk.PhotoImage(file="William McKinley.gif")
twentysix = ImageTk.PhotoImage(file="Theodore Roosevelt.gif")
twentyseven = ImageTk.PhotoImage(file="William Howard Taft.gif")
twentyeight = ImageTk.PhotoImage(file="Woodrow Wilson.gif")
twentynine = ImageTk.PhotoImage(file="Warren G Hardin.gif")
thirty = ImageTk.PhotoImage(file="Calvin Coolidge.gif")
thirtyone = ImageTk.PhotoImage(file="Herbert Hoover.gif")
thirtytwo = ImageTk.PhotoImage(file="Franklin D. Roosevelt.gif")
thirtythree = ImageTk.PhotoImage(file="Harry Truman.gif")
thirtyfour = ImageTk.PhotoImage(file="Dwight D Eisenhower.gif")
thirtyfive = ImageTk.PhotoImage(file="John F Kennedy.gif")
thirtysix = ImageTk.PhotoImage(file="Lyndon B Johnson.gif")
thirtyseven = ImageTk.PhotoImage(file="Richard Nixon.gif")
thirtyeight = ImageTk.PhotoImage(file="Gerald Ford.gif")
thirtynine = ImageTk.PhotoImage(file="Jimmy Carter.gif")
forty = ImageTk.PhotoImage(file="Ronald Reagan.gif")
fortyone = ImageTk.PhotoImage(file="George H Bush.gif")
fortytwo = ImageTk.PhotoImage(file="Bill Clinton.gif")
fortythree = ImageTk.PhotoImage(file="George W Bush.gif")
fortyfour = ImageTk.PhotoImage(file="Barry.gif")
fortyfive = ImageTk.PhotoImage(file="donald trump.gif")
#presidents are put into a list and then a random one is being selected under the name of pres

presidents = [one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty,thirtyone,thirtytwo,thirtythree,thirtyfour,thirtyfive,thirtysix,thirtyseven,thirtyeight,thirtynine,forty,fortyone,fortytwo,fortythree,fortyfour,fortyfive]
presimg = random.choice(presidents)
#the placement of the random choice is taken out and then added one to it
computer_guess = str(presidents.index(presimg) + 1)
score = 0
#checks if the answer is correct given is correct
def check():
#Get the value from txt_guess
    user_guess = str(txt_guess.get())

#Determine higher, lower, or just right
    global lbl_result
    global score
    global lbl_score
    global computer_guess
    global presimg
    if user_guess == "murica":
        msg = "AMERICA"
    elif user_guess == "isis>america":
        text = "What the jiminy crickets did you just flaming say about me, you little bozo? I’ll have you know I graduated top of my class in the Cub Scouts, and I’ve been involved in numerous secret camping trips in Wyoming, and I have over 300 confirmed knots. I am trained in first aid and I’m the top bandager in the entire US Boy Scouts (of America). You are nothing to me but just another friendly face. I will clean your wounds for you with precision the likes of which has never been seen before on this annual trip, mark my words. You think you can get away with saying those shenanigans to me over the Internet? Think again, finkle. As we speak I am contacting my secret network of MSN friends across the USA and your IP is being traced right now so you better prepare for the seminars, man. The storm that wipes out the pathetic little thing you call your bake sale. You’re frigging done, kid. I can be anywhere, anytime, and I can tie knots in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in road safety, but I have access to the entire manual of the United States Boy Scouts (of America) and I will use it to its full extent to train your miserable butt on the facts of the continents, you little schmuck. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your silly tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goshdarned sillyhead. I will throw leaves all over you and you will dance in them. You’re friggin done, kiddo."
        text2 = ''
        
        count = 0
        for letter in text:
            text2 += letter
            if letter == ' ':
                
                count += 1
            if count >= 15:
                text2 += '\n'
                count = 0
        msg = text2
        
    elif user_guess == computer_guess:
        msg = "Correct!"
        score += 1
        
    elif user_guess != computer_guess:
        msg="u be wrong"
    else:
        msg = "Something went wrong..."
    lbl_result["text"] = msg
    txt_score["text"] = score
    presimg = random.choice(presidents)
    computer_guess = str(presidents.index(presimg)+1)
    label.configure(image = presimg)
#resets the game
def reset():
    global presimg
    global computer_guess
    global count
    time.sleep(.5)
    count = 0
    txt_score.configure(text = count)
    presimg = random.choice(presidents)
    computer_guess = str(presidents.index(presimg) + 1)
    label.configure(image = presimg)
    lbl_result["text"] = "Guess the number of the president."
    txt_guess.delete(0, 5)
    root.after(30000, reset)

label = Tkinter.Label(root, image = presimg)
label.grid(row=1, column=1)
lbl_result=Tkinter.Label(root, text="guess the number of the president", fg="white", bg="red")
lbl_result.grid(row=2, column=1)

btn_reset = Tkinter.Button(root, text="Reset", fg="red", bg="white", command=reset)
btn_reset.grid(row=3,column=2)

#Change root window background color
root.configure(bg="red")
txt_guess = Tkinter.Entry(root, width=10)
txt_guess.grid(row=3, column=1)
txt_score = Tkinter.Label(root, text = score, fg ="white", bg="red")
txt_score.grid(row=0, column = 3)
btn_check = Tkinter.Button(root, text="Check", fg="green", bg="white", command=check)
root.bind("<Return>", lambda x: check())
#root.bind("<space>", lambda x: reset())
btn_check.grid(row = 3, column = 0)

root.after(60000, reset)
#Change the title



#Change the window size
#root.bind("<Return>", check2)
root.mainloop()