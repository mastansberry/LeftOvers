import change
import tkinter
#from change import changer
a=2
b='nope'
global c
c = 5

def testing():
    print (a)
    print (b)
    print (c)
    
    changer()
    print (a)
    print (b)
    print (change.test.c)
    
    
#testing()

root=tkinter.Tk()
root.mainloop()
root.quit()