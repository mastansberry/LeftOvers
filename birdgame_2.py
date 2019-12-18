from Tkinter import *
import Tkinter
import random
from PIL import Image, ImageTk
import os.path

root = Tk()

bluejay = Tkinter.PhotoImage(file="bluejay.gif")
canary = ImageTk.PhotoImage(file="canary.gif")
cardinal = ImageTk.PhotoImage(file="cardinal.gif")
chicken = ImageTk.PhotoImage(file="chicken.gif")
dove = ImageTk.PhotoImage(file="dove.gif")
eagle = ImageTk.PhotoImage(file="eagle.gif")
flamingo = ImageTk.PhotoImage(file="flamingo.gif")
mockingbird = ImageTk.PhotoImage(file="mockingbird.gif")
owl = ImageTk.PhotoImage(file="owl.gif")
pheasant = ImageTk.PhotoImage(file="pheasant.gif")
pigeon = ImageTk.PhotoImage(file="pigeon.gif")
raven = ImageTk.PhotoImage(file="raven.gif")
robin = ImageTk.PhotoImage(file="robin.gif")
sparrow = ImageTk.PhotoImage(file="sparrow.gif")
tucan = ImageTk.PhotoImage(file="tucan.gif")
birdstext = ['bluejay','canary','cardinal','chicken','dove','eagle','flamingo','mockingbird','owl','pheasant','pigeon','raven','robin','sparrow','tucan']
birdsphotos = [bluejay,canary,cardinal,chicken,dove,eagle,flamingo,mockingbird,owl,pheasant,pigeon,raven,robin,sparrow,tucan]
birdimg = random.choice(birdsphotos)
computer_guess = birdstext[(birdsphotos.index(birdimg))]
print computer_guess

def check():
    
    user_guess = str(txt_guess.get())
    
    global lbl_result
    if user_guess != computer_guess:
        msg = "Try Again!"
    elif user_guess == computer_guess:
        msg = "Correct!"
    else:
        msg = "something went wrong..."
    lbl_result["text"] = msg
def reset():
    global birdimg
    global computer_guess
    birdimg = random.choice(birds)
    computer_guess = str(presidents.index(birdimg) + 1)
    label.configure(image = birdimg)
    lbl_result["text"] = "Guess the type of bird."

label = Tkinter.Label(root, image = birdimg)
label.pack()
lbl_result = Tkinter.Label(root, text="guess the type of bird")
lbl_result.pack()

btn_reset = Tkinter.Button(root, text="Reset", fg="blue", bg="white", command=reset)
btn_reset.pack(side="right")

root.configure(bg="blue")
txt_guess = Tkinter.Entry(root, width=10)
txt_guess.pack()
btn_check = Tkinter.Button(root, text="Check", fg="orange", bg="white", command=check)
btn_check.pack(side="left")

root.mainloop()