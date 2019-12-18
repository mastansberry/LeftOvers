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
StudentPresent=[]
loopcity=True
CheckInTime=('Checked in at: {:%H:%M:%S %Y-%b-%d}'.format(datetime.datetime.now()))
cspMorning = ("{:%H:%M:%S}".format(datetime.time(8,30,00)))
cspAfternoon = ("{:%H:%M:%S}".format(datetime.time(13,15,00)))
StaffList=('mstansberry@ocknights.org','matt_stansberry@hotmail.com')
def Login():
    global loopcity
    global StudentPresent
    while loopcity == True:
        StudentID = int(raw_input("what is your ID number: "))
        if StudentID in number:
            print StudentInfo.get(StudentID)
            #studentandtime=
            StudentPresent.append((StudentInfo.get(StudentID),CheckInTime))
            print StudentPresent
        else:
            print "Not in our system, check with Admin"     
        if StudentID == 9999:
            loopcity= False
            print loopcity