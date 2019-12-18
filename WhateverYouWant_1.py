from capitals import capitals_dict
import Tkinter
import random

def run():
#Picks random capitals from list
    state = random.choice(capitals_dict.keys())
    capital = capitals_dict[state]
    capital = capital.lower()
    
    game=Tkinter.Tk()
    
    text = Tkinter.Label(game)
    text.pack()
    
    text2 = Tkinter.Entry(game)
    text2.pack()
#Checks to see if guess is correct
    def check(hi):
        if hi == capital:
            text.configure(text = 'Correct! Press Check to continue')
        if hi != capital:
            text.configure(text = 'Incorrect! Press Check to continue')
#Closes window and opens up new one           
        def restart():
            game.destroy()
            run()
        check_btn.configure(command = restart)
#Check button
    check_btn = Tkinter.Button(game, text = "Check", command = lambda: check(text2.get()))
    check_btn.pack()
    
    text.configure(text = 'Enter the capital of {}: '.format(state))
    
    game.mainloop()
run()