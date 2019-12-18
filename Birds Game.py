from birds import birds_dict
import Tkinter
import random

def run():
#Picks random capitals from list
    state = random.choice(birds_dict.keys())
    bird = birds_dict[state]
    bird = bird.lower()
    
    game=Tkinter.Tk()
    
    text = Tkinter.Label(game)
    text.pack()
    
    text2 = Tkinter.Entry(game)
    text2.pack()
#Checks to see if guess is correct
    def check(h):
        if h == bird:
            text.configure(text = 'Correct! Press Check to continue')
        if h != bird:
            text.configure(text = 'Incorrect! Press Check to continue')
#Closes window and opens up new one           
        def restart():
            game.destroy()
            run()
        check_btn.configure(command = restart)
#Check button
    check_btn = Tkinter.Button(game, text = "Check", command = lambda: check(text2.get()))
    check_btn.pack()
    
    text.configure(text = 'Enter State Bird of {}: '.format(state))
    
    game.mainloop()
run()