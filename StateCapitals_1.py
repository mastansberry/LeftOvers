from Tkinter import *
import Tkinter
import random
from PIL import Image, ImageTk
import os.path

def run():
    game=Tkinter.Tk()

    Alabama = ImageTk.PhotoImage(file="Montgomery.gif")
    Alaska = ImageTk.PhotoImage(file="Juneau.gif")
    Arizona = ImageTk.PhotoImage(file="Phoenix.gif")
    Arkansas = ImageTk.PhotoImage(file="Little Rock.gif")
    California = ImageTk.PhotoImage(file="Sacramento.gif")
    Colorado = ImageTk.PhotoImage(file="Denver.gif")
    Connecticut = ImageTk.PhotoImage(file="Hartford.gif")
    Delaware = ImageTk.PhotoImage(file="Dover.gif")
    Florida = ImageTk.PhotoImage(file="Tallahassee.gif")
    Georgia = ImageTk.PhotoImage(file="Atlanta.gif")
    Hawaii = ImageTk.PhotoImage(file="Honolulu.gif")
    Idaho = ImageTk.PhotoImage(file="Boise.gif")
    Illinois = ImageTk.PhotoImage(file="Springfield.gif")
    Indiana = ImageTk.PhotoImage(file="Indianapolis.gif")
    Iowa = ImageTk.PhotoImage(file="Des Moines.gif")
    Kansas = ImageTk.PhotoImage(file="Topeka.gif")
    Kentucky = ImageTk.PhotoImage(file="Frankfort.gif")
    Louisiana = ImageTk.PhotoImage(file="Baton Rouge.gif")
    Maine = ImageTk.PhotoImage(file="Augusta.gif")
    Maryland = ImageTk.PhotoImage(file="Annapolis.gif")
    Massachusetts = ImageTk.PhotoImage(file="Boston.gif")
    Michigan = ImageTk.PhotoImage(file="Lansing.gif")
    Minnesota = ImageTk.PhotoImage(file="St. Paul.gif")
    Mississippi = ImageTk.PhotoImage(file="Jackson.gif")
    Missouri = ImageTk.PhotoImage(file="Jefferson City.gif")
    Montana = ImageTk.PhotoImage(file="Helena.gif")
    Nebraska = ImageTk.PhotoImage(file="Lincoln.gif")
    Nevada = ImageTk.PhotoImage(file="Carson City.gif")
    NewHampshire = ImageTk.PhotoImage(file="Concord.gif")
    NewJersey = ImageTk.PhotoImage(file="Trenton.gif")
    NewMexico = ImageTk.PhotoImage(file="Santa Fe.gif")
    NewYork = ImageTk.PhotoImage(file="Albany.gif")
    NorthCarolina = ImageTk.PhotoImage(file="Raleigh.gif")
    NorthDakota = ImageTk.PhotoImage(file="Bismarck.gif")
    Ohio = ImageTk.PhotoImage(file="Columbus.gif")
    Oklahoma = ImageTk.PhotoImage(file="Oklahoma City.gif")
    Oregon = ImageTk.PhotoImage(file="Salem.gif")
    Pennsylvania = ImageTk.PhotoImage(file="Harrisburg.gif")
    RhodeIsland = ImageTk.PhotoImage(file="Providence.gif")
    SouthCarolina = ImageTk.PhotoImage(file="Columbia.gif")
    SouthDakota = ImageTk.PhotoImage(file="Pierre.gif")
    Tennessee = ImageTk.PhotoImage(file="Nashville.gif")
    Texas = ImageTk.PhotoImage(file="Austin.gif")
    Utah = ImageTk.PhotoImage(file="Salt Lake City.gif")
    Vermont = ImageTk.PhotoImage(file="Montpelier.gif")
    Virginia = ImageTk.PhotoImage(file="Richmond.gif")
    Washington = ImageTk.PhotoImage(file="Olympia.gif")
    WestVirginia = ImageTk.PhotoImage(file="Charleston.gif")
    Wisconsin = ImageTk.PhotoImage(file="Madison.gif")
    Wyoming = ImageTk.PhotoImage(file="Cheyenne.gif")
    
    state = [Alabama,Alaska,Arizona,Arkansas,California,Colorado,Connecticut,Delaware,Florida,Georgia,Hawaii,Idaho,Illinois,Indiana,Iowa,Kansas,Kentucky,Louisiana,Maine,Maryland,Massachusetts,Michigan,Minnesota,Mississippi,Missouri,Montana,Nebraska,Nevada,NewHampshire,NewJersey,NewMexico,NewYork,NorthCarolina,NorthDakota,Ohio,Oklahoma,Oregon,Pennsylvania,RhodeIsland,SouthCarolina,SouthDakota,Tennessee,Texas,Utah,Vermont,Virginia,Washington,WestVirginia,Wisconsin,Wyoming]
    stateimg = random.choice(state)
    
    computer_guess = str(state.index(stateimg)+1)
    
    
    def check():
        global lbl_result
        user_guess = str(txt_guess.get())
        if user_guess != computer_guess:
            msg = "Try Again!"
        elif user_guess == computer_guess:
            msg = "Correct!"
        lbl_result["text"] = msg
        
    def reset():
        global stateimg
        global computer_guess
        stateimg = random.choice(state)
        computer_guess = str(state.index(stateimg)+1)
        label.configure(image = stateimg)
        lbl_result["text"] = "Guess the captial of this state."
        txt_guess.delete(0, 5)
    
    label = Tkinter.Label(game, image=stateimg)
    label.pack()
    
    lbl_result=Tkinter.Label(game, text="blah")
    lbl_result.pack()
    
    txt_guess = Tkinter.Entry(game, width=10)
    txt_guess.pack()
    
    check_btn = Tkinter.Button(game, text = "Check", command=check)
    check_btn.pack()
    
    game.mainloop()
run()
