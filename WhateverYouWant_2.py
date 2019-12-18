from capitals import *
from PIL import Image, ImageTk
import Tkinter
import threading
from threading import Thread
import time
import random
game = Tkinter.Tk()
timelimit=0 
score=0
state = random.choice(capitals_dict.keys())
capital = capitals_dict[state][0]
capital = capital.lower()



text1 = Tkinter.Label(game)
text1.pack()

img = Tkinter.PhotoImage(master = game, file = capitals_dict[state][1])
imagebackup = img

label = Tkinter.Label(game, image = imagebackup)
label.pack()

text2 = Tkinter.Entry(game)
text2.pack()

def timer():
    global game
    global timelimit
    global labeltime
    labeltime = Tkinter.Label(game, text = "")
    labeltime.pack()
    while timelimit < 120:
        timelimit += 1
        labeltime.configure(text = "Time: " + str(120- timelimit))
        time.sleep(1)
    
def run():
    global game
    global text
    
#Picks random capitals from list
    if __name__=='__main__':
        Thread(target=timer).start()

    
    
    

   

        
#Checks to see if guess is correct
def check(hi):
    global score
    labelpoints = Tkinter.Label(game, text = "")
    labelpoints.pack()
    if hi == capital:
        text1.configure(text = 'Correct! Press Check to continue')
        labelpoints.configure(text = "Score: " + str(1 + score))
        time.sleep(3)
        run()
    elif hi != capital:
        text1.configure(text = 'Incorrect! Press Check to continue')
        
#Closes window and opens up new one           
def restart():
    global score
    global timelimit
    score=0
    timelimit=0
    run()
    
#Check button
check_btn = Tkinter.Button(game, text = "Check", command = lambda: check((text2.get()).lower()))
check_btn.pack()

text1.configure(text = 'Enter the capital of {}: '.format(state))
    


game.mainloop()

run()