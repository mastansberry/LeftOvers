import Tkinter
import smtplib
import threading
from threading import Thread
from Tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

student = {1:'jack', 2:'dev',3:'eric',4:'matt'}
number = student.keys()
name = student.values()

top = Tkinter.Tk()
Usernames = ['jack', 'dev', 'eric', 'matt']
Passwords = ['1','2']
recipient = ['leganddarnell@gmail.com', 'moebeaudette23@gmail.com']
here = ['Here:']
here2=[]

Time =('{:%H:%M:%S}'.format(datetime.datetime.now()))
settime =('{:%H:%M:%S}'.format(datetime.time(9,43,00)))



def verify():
    
    global present
    global E1
    numget = int(E1.get())
    if numget in number:
        print numget
        ork = student.get(numget)
        print ork
        print('Logged In')
        here.append(ork)
        E2.insert(END,ork + '\n')
        print here
        
       
'''      

def Mail():
    global settime
    while True:
        Time =('{:%H:%M:%S}'.format(datetime.datetime.now()))
        if Time == settime:
            print('sending')
            fromaddr = 'leganddarnell@gmail.com'
            toaddrs = 'darnelld@bancroft-rosalie.org'
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "turnup"
            msg['From'] = "Daddy " #like name
            msg['To'] = "wackest rappers out there"
            
            body = MIMEText(str(here))
            msg.attach(body)
            
            username = 'leganddarnell@gmail.com'
            password = 'legand24' 
            server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
'''
top.title('Login to Take Attendance')
top.geometry('270x80')
E1 = Tkinter.Entry()
E2 = Tkinter.Text(top)
L1 = Label(top, text="User Name")
L1.grid(row=1)
B1 = Tkinter.Button(top, text ="Login", command = verify)
#B2 = Tkinter.Button(top, text ="Help", command = help)
B1.grid(row=2)
#B2.pack(side = BOTTOM)
E1.grid(row=3)
E2.grid(row=4, rowspan=4)
'''CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20).pack(side = TOP)'''
'''
if __name__ == '__main__':
    Thread(target = Mail).start()

'''
top.mainloop()