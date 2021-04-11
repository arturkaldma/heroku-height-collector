import smtplib
from email.mime.text import MIMEText

def send_email(email, height, average_height, count):
    from_email = "antonbezfamilii3@gmail.com"
    from_password = "65H529tA"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. Average of all is <strong>%s</strong> and thas is calculated out <strong>%s</strong> of users" % (height, average_height, count)
    
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)