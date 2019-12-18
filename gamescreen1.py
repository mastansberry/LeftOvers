import Tkinter
import random
    

    
def game1():
    #destroy the main window and open new one
    top.destroy()

    #Literally copy and past your game code here and tab it all in.  Make sure 
    #you add import random at the top

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
        txt_guess.delete(0,100)
    
    
    
    #create root window
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

def game2():
    top.destroy()
    def passingbutton():
        pass
        
    a = Tkinter.Tk()
    label = Tkinter.Label(a, text= 'Oh  waddup')
    label.pack()
    btn = Tkinter.Button(text = "Done", command =passingbutton )
    btn.pack(side='left')
    a.mainloop()
def game3():
    pass  
top = Tkinter.Tk()
top.wm_title("Game Center")
A = Tkinter.Button(top, text = "Game 1 Name Here", command = game1, width = 50, height= 10)
B = Tkinter.Button(top, text = "Game 2 Name Here", command = game2, width = 50, height = 10)
C = Tkinter.Button(top, text = "Game 3 Name Here", command = game2, width = 50, height = 10)
A.pack()
B.pack()
C.pack()

top.mainloop()
