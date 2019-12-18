import time
import sched
import datetime
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from smtplib import SMTP
import smtplib
localtime = ('{:%H:%M:%S}'.format(datetime.datetime.now()))
samhere = False
attendence = []
samcount = 0
jacobcount=0
manuelcount = 0
n = 2017
seconds = (0, 60, 1)
abelcount = 0
def rollcall():
    code = raw_input("Enter your rolecall number.  ")
    if code == '1234':
        global samcount
        print 'hello Sam'
        samhere = 'Sam is present'
        samcount += 1
    
        if samcount > 1:
            print 'this student has already been accounted for'
            samhere = 'already accounted for'
        if samhere == 'Sam is present':
            attendence.append(samhere)
        
    if code == '42069':
        global jacobcount
        print 'hello jacob'
        jacobhere = 'Jacob is present'
        jacobcount += 1
        if jacobcount > 1:
            print 'this student has already been accounted for'
        if jacobhere == 'Jacob is present':
            attendence.append(jacobhere)
    if code == '1266':
        global abelcount
        print 'hello abel'
        abelhere = 'Abel is present'
        abelcount += 1
        if abelcount > 1:
            print 'this student has already been accounted for'
        if abelhere == 'Jacob is present':
            attendence.append(abelhere)
    if code == '1111':
        global manuelcount
        print 'hello jacob'
        manuelhere = 'Manny is present'
        manuelcount += 1
        if jacobcount > 1:
            print 'this student has already been accounted for'
        if manuelhere == 'Manny is present':
            attendence.append(manuelhere)
               
    print attendence
  

emailstart = ('{:%H:%M:%S}'.format(datetime.time(14, 42,00)))

def rollloop():
    global localtime
    global emailstart
    while localtime != emailstart:
        localtime = ('{:%H:%M:%S}'.format(datetime.datetime.now()))
        if localtime == emailstart:
            email()
        else:
            rollcall()
def email():
    if localtime == emailstart: #and localtime < emailend:
        fromaddr = " pythonemailstest@gmail.com"
        toaddr = "sdmiserez@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Security Notification"
        body = str(attendence)
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("pythonemailstest@gmail.com", "pythonemail99")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        rollloop()
rollloop()