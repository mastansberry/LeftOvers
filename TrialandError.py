from List import StudentInfo
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def job():
    print("I'm working...")

'''StudentName=['Abel','Diego']
StudentNumbers=[1126, 1134]
Joined= zip(StudentName,StudentNumbers)'''
flag = True
CheckedInTime=('Checked in at: {:%H:%M:%S %Y-%b-%d}'.format(datetime.datetime.now()))
StudentPresent=[]
number=StudentInfo.keys()
name=StudentInfo.values()

'''jkl ={
    234:"x",
    345:"y"
}

morn= time(4, 0, 1)
after = time(5,0,2)
now = time()


today=date.today()
fg= date(today.year,4,1)
yuh = str(datetime.now())
#localtime = time.localtime(time.time())'''
Time=("{:%H:%M}".format(datetime.datetime.now()))
#Timer=int(Time)
settime = ("{:%H:%M}".format(datetime.time(9,35)))
tester="6:30"
def math():
    if "2:40" < "4:40":
        print "yes"
        
def trash():
    if Time < settime:
        print Time, settime
        print "yes"
    else:
        print Time, settime
        print "no"
def Timecheck():
    if Time > '{8:30:00}'.format(datetime()):
        print "yes"

def Login():
    StudentID = int(raw_input("what is your ID number: "))
    if StudentID in number:
      print StudentInfo.get(StudentID)  


def Try():
    StudentID = int(raw_input("what is your ID number: "))
    print StudentID
    print number
    if StudentID in number:
      print StudentInfo.get(StudentID)  




def fla():
    StudentPresent=[]
    if Time > settime:
    #print "What student are you?"
        StudentID = int(raw_input("What student are you? "))
        if StudentID in number:
            here = StudentInfo.get(StudentID)
            print here
            StudentPresent.append(here)
            print StudentPresent       
        else:
            print "Not in our system, check with Admin"
        if StudentID == 9999:
            flag = False
            print flag
def Timer():
    while flag ==  True:
            print Time
            datetime.sleep(20)
def CheckIn():
    global flag
    StudentPresent=[]
    while flag==True:
        Time=("{:%H:%M}".format(datetime.datetime.now()))
        StudentID = int(raw_input("What student are you? "))
        if StudentID in number:
            here = StudentInfo.get(StudentID)
            print here
            StudentPresent.append(here)
            print StudentPresent       
        else:
            print "Not in our system, check with Admin"
        if StudentID == 9999:
            flag= False
            print flag
   
                
def checker():
    #print '#'
    x= int(raw_input("Enter Student Number: "))
    if x == 3:
        print "madeit"
        
         
def CheckIn2():
    global flag
    global StudentPresent
    while flag==True:
        Time=("{:%H:%M:%S}".format(datetime.datetime.now()))
        StudentID = int(raw_input("What student are you? "))
        if StudentID in number:
            here = StudentInfo.get(StudentID)
            print here
            StudentPresent.append(here)
            StudentPresent.append(Time)
            print StudentPresent       
        else:
            print "Not in our system, check with Admin"
        if StudentID == 9999:
            flag= False
            print flag
            Mail()
            print 'Sending Email'

def clocking():
    while True:
        Time=("{:%H:%M}".format(datetime.datetime.now()))
        if Time == ("{:%H:%M}".format(time(9,40))):
            print 'yes'
        
        

def Mail():
    fromaddr = 'notificationupdate12344321@gmail.com'
    toaddrs = 'mstansberry@ocknights.org'
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Students who are Present"
    msg['From'] = "Mr. Stansberry" #like name
    msg['To'] = "School Staff"
    
    body = MIMEText(str(StudentPresent))
    msg.attach(body)
    
    username = 'notificationupdate12344321@gmail.com'
    password = 'notificationupdate'
    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()        
        
        
        
        