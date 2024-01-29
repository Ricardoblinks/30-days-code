#import the necessary libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#define the function to send the email
def send_email(to, sender, subject, message):
    msg = MIMEMultipart()
    msg['to'] = to
    msg['from'] = sender
    msg['subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server_host = ''
    server_port = 465
    server_user = ''
    server_password = ''

    with smtplib.SMTP_SSL(server_host, server_port) as server:
        server.login(server_user, server_password)

        server.sendmail(sender, to, msg.as_string())

# necessary variables to fill the parameter for the function

to = "richard@compumetrics.com.ng"
sender = 'youremail'
subject = "Thanks for your time"
message = 'This is a wonderful set up'

# calling the function
send_email(to, sender, subject, message)

#note please fill the server information with your details, contact me for more information @ ricardoblinks1@gmail.com
