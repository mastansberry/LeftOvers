import tkinter
from tkinter import *

root= tkinter.Tk()



def checker():
    print ("got it")
    
updated='hello' 

v = StringVar()
tkinter.Label(root, textvariable=v).grid(row=4, column=0)

v.set("New Text!")

#guesslab=tkinter.Entry(root, textvariable=updated)
#guesslab.grid(row=1, column=0)
b = tkinter.Button(root, text="check", command=checker)
b.grid(row=3, column=0)
    
    
root.mainloop()