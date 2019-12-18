import Tkinter

#myfile=open("second", 'w')
#myfile.close()
myfile=open('TestText.txt', 'w')
mytext= myfile.write("hey buddy 3 \n")
myfile=open('TestText.txt', 'r')
myread= myfile.read()
print myread
myfile=open('TestText.txt', 'a')
mytext= myfile.write("hey buddy you a fatty")
myfile=open('TestText.txt', 'r')
myread2= myfile.readlines()
print myread2[1]
myfile.close()
btn= 0
num=0


help="helpme"
root = Tkinter.Tk()
root.wm_title('GamePlace')

def game1():
    print "hello"
    dog=c.cget('text')
    print dog
def game2():
    rootg1 = Tkinter.Tk()
    rootg1.wm_title('Try')
    e2 = Tkinter.Entry(rootg1)
    e2.grid(row=2, column=0)
    def Fetch():
        fetchBU=e2.get()
        print fetchBU
        c2=Tkinter.Button(root,text="NO", command= game1)
        c2.grid(row=3, column=0)
    b2=Tkinter.Button(rootg1,text="addButton", command= Fetch)
    b2.grid(row=1, column=0)
    


b=Tkinter.Button(root,text="addButton", command= game2)
b.grid(row=0, column=0)

c=Tkinter.Button(root,text="NO", command= game1)
c.grid(row=1, column=0)

e1 = Tkinter.Entry(root)
e1.insert(0,myread2[1])
e1.grid(row=2, column=0)


root.mainloop()