#Samuel Miserez 1/12/2017
from Tkinter import *
import Tkinter 
import random
from PIL import Image, ImageTk
import os.path
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
#checks if the answer is correct given is correct
def check():
#Get the value from txt_guess
    user_guess = str(txt_guess.get())

#Determine higher, lower, or just right
    global lbl_result
    if user_guess != computer_guess:
        msg = "Try Again" 
    elif user_guess == computer_guess:
        msg = "Correct!"
    elif user_guess == "murica":
        msg = "AMERICA"
    else:
        msg = "Something went wrong..."
    lbl_result["text"] = msg
#resets the game
def reset():
    global presimg
    global computer_guess
    presimg = random.choice(presidents)
    computer_guess = str(presidents.index(presimg) + 1)
    label.configure(image = presimg)
    lbl_result["text"] = "Guess the number of the president."
    txt_guess.delete(0, 5)
    
label = Tkinter.Label(root, image = presimg)
label.pack()
lbl_result=Tkinter.Label(root, text="guess the number of the president")
lbl_result.pack()

btn_reset = Tkinter.Button(root, text="Reset", fg="red", bg="white", command=reset)
btn_reset.pack(side="right")

#Change root window background color
root.configure(bg="red")
txt_guess = Tkinter.Entry(root, width=10)
txt_guess.pack()
btn_check = Tkinter.Button(root, text="Check", fg="green", bg="white", command=check)
btn_check.pack(side="left")
#Change the title



#Change the window size
#root.bind("<Return>", check2)
root.mainloop()