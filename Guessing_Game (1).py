import Tkinter
import random

number = random.randint(1,20)
counter = 0
def submit():
    guess = int(entry.get())
    verify(guess)
def verify(guess):
    ver = Tkinter.Tk()
    ver.focus_force()
    def retry():
        ver.destroy()
    def quit():
        ver.destroy()
        root.destroy()
    if guess == number:
        ver.wm_title('You Win!')
        acceptbutton = Tkinter.Button(ver, text = 'Quit', width = 50, height = 2, command = quit)
        done = Tkinter.Label(ver, text = 'You Got It!', width = 100) 
        def enter(event):
            quit()
        ver.bind('<Return>', enter)
    else:
        ver.wm_title('Try Again')
        acceptbutton = Tkinter.Button(ver, text = 'Retry', width = 50, height = 2, command = retry)
        if guess < number:
            done = Tkinter.Label(ver, text = "You're too low!", width = 100)
        if guess > number:
            done = Tkinter.Label(ver, text = "You're too high!", width = 100)
        def enter(event):
            retry()
        ver.bind('<Return>', enter)
    done.pack()
    acceptbutton.pack()
    ver.mainloop()
        
root = Tkinter.Tk()
root.wm_title('Guessing Game')

instructions = Tkinter.Label(root, text = 'I am thinking of a number between 1 and 20. Guess!', width = 100)
entry = Tkinter.Entry(root, width = 50)
button = Tkinter.Button(root, text = 'Enter', width = 50, height = 2, command = submit)
instructions.pack()
entry.pack()
button.pack()
def enter(event):
    submit()
root.bind('<Return>', enter)
root.mainloop()