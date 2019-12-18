import Tkinter

root = Tkinter.Tk()
root.wm_title('FarmApplication')

#def NewField():
myfile=open('TestText.txt', 'r')
myread= myfile.read()   
    
def Field1():
    rootF1= Tkinter.Tk()
    rootF1.wm_title('Field1')
    lab=Tkinter.Label(rootF1, text=myread)
    lab.grid(row=1)
    
    
    
def Field2():
    rootF2= Tkinter.Tk()
    rootF2.wm_title('Field2')


b=Tkinter.Button(root,text="Field1", command= Field1)
b.grid(row=0, column=1, columnspan=1)

c=Tkinter.Button(root,text="Field2", command= Field2)
c.grid(row=1, column=1)



root.mainloop()