import Tkinter
import random

computer_guess = random.randint(1,10)
def check():
    #get the value from txt_guess
    user_guess = int(txt_guess.get())

    #determine higher or lower or correct
    if user_guess < computer_guess:
        msg = 'Higher!'
    elif user_guess > computer_guess:
        msg = 'Lower!'
    elif user_guess == computer_guess:
        msg = 'Correct!'
    else:
        msg = 'Something went wrong...'
        
    #Show the result
    lbl_result['text'] = msg
    #clear txt_guess
    txt_guess.delete(0,5)
    
    
#use enter button
def enter(x):
        #get the value from txt_guess
    user_guess = int(txt_guess.get())

    #determine higher or lower or correct
    if user_guess < computer_guess:
        msg = 'Higher!'
    elif user_guess > computer_guess:
        msg = 'Lower!'
    elif user_guess == computer_guess:
        msg = 'Correct!'
    else:
        msg = 'Something went wrong...'
        
    #Show the result
    lbl_result['text'] = msg
    #clear txt_guess
    txt_guess.delete(0,5)
    
 
    
        
def reset():
    #Declare the global variable
    global computer_guess
    #get a random number
    computer_guess = random.randint(1,10)
    #change the lbl_result txt
    lbl_result['text'] = 'Game reset. Guess again!'
    



#create rood window
root = Tkinter.Tk()
 

#change root window background color
root.configure(bg='white')

#change title
root.title('Guess the number!')

#change the window size
root.geometry('500x250')

#create widgets
lbl_title = Tkinter.Label(root, text='Welcome to the Guessing Game!', bg='white')
lbl_title.pack()

lbl_result = Tkinter.Label(root, text='Good Luck!',bg='white')
lbl_result.pack()

btn_check = Tkinter.Button(root, text = 'Check', fg='blue',bg='white', command=check)
btn_check.pack(side='left')

btn_reset = Tkinter.Button(root, text = 'Reset', fg='red', command=reset)
btn_reset.pack(side='right')

txt_guess = Tkinter.Entry(root, width=3)
txt_guess.pack()


#use enter button
root.bind('<Return>', enter)   
    



#start the main Events Loop
root.mainloop()
root.destroy()