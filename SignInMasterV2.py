from List import StudentInfo
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
from threading import Thread

number=StudentInfo.keys()
name=StudentInfo.values()
StudentPresentWP=[]
StudentPresentBR=[]
loopcity=True
CheckInTime=('Checked in at: {:%H:%M:%S %Y-%b-%d}'.format(datetime.datetime.now()))
cspMorning = ("{:%H:%M:%S}".format(datetime.time(8,30,00)))
cspAfternoon = ("{:%H:%M:%S}".format(datetime.time(13,15,00)))
StaffList=('mstansberry@ocknights.org','matt_stansberry@hotmail.com')
def Login():
    global loopcity
    global StudentPresentWP
    global StudentPresentBR
    while loopcity == True:
        StudentID = int(raw_input("what is your ID number: "))
        if StudentID in number:
            print StudentInfo.get(StudentID)
            #studentandtime=
            if StudentID < 1130:
                if StudentID > 1130 and  StudentID < 1140:
                    StudentPresentBR.append((StudentInfo.get(StudentID),CheckInTime))
            else:
                StudentPresentWP.append((StudentInfo.get(StudentID),CheckInTime))    
                
            print StudentPresentWP
            print StudentPresentBR
        else:
            print "Not in our system, check with Admin"     
        if StudentID == 9999:
            loopcity= False
            print loopcity
            
'''            
def func2():
    global StudentPresent
    global cspMorning1
    global cspMorning2
    while True:
        Time=("{:%H:%M:%S}".format(datetime.datetime.now()))
        #print Time 
        time.sleep(1)
        if Time ==cspAfternoon:
            print "Sending Present List"
            fromaddr = 'notificationupdate12344321@gmail.com'
            toaddrs = StaffList
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Students who are Present morning"
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
            time.sleep(1)
            StudentPresent=[]
        if Time ==cspAfternoon:
            print "Sending Present List"
            fromaddr = 'notificationupdate12344321@gmail.com'
            toaddrs = StaffList
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Students who are Present afternoon"
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
            time.sleep(1)
            StudentPresent=[]

if __name__ == '__main__':
        Thread(target = func2).start()








'''









def Mail():

    fromaddr = 'notificationupdate12344321@gmail.com'
    toaddrs = 'matt_stansberry@hotmail.com'
    
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