import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
StaffList=['matt_stansberry@hotmail.com','mstansberry@ocknights.org']

def Mail():

    fromaddr = 'notificationupdate12344321@gmail.com'
    toaddrs = StaffList

    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Students who are Present"
    msg['From'] = "Mr. Stansberry" #like name
    msg['To'] = ", ".join(toaddrs)
    
    body = MIMEText('test 54321')# to send list add (str(list))
    msg.attach(body)
    
    username = 'notificationupdate12344321@gmail.com'
    password = 'notificationupdate'
    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()