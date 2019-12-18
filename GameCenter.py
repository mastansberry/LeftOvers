import Tkinter
def Game1():
    top.destroy()
    a = Tkinter.Tk()
    label = Tkinter.Label(a, text= 'Oh snap its a label, waddup')
    label.pack()
    a.mainloop()
    
def Game2():
    pass
    
def Game3():
    pass
    
top = Tkinter.Tk()
top.wm_title("GameCenter")
A = Tkinter.Button(top, text = "name of game1", command = Game1, width = 50, height= 10)
B = Tkinter.Button(top, text = "name of game2", command = Game2, width = 50, height = 10)
C = Tkinter.Button(top, text = "name of game3", command = Game3, width = 50, height = 10)
A.pack()
B.pack()
C.pack()

top.mainloop()