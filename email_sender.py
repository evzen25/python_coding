import smtplib
import ssl
from email.message import EmailMessage


email_sender = 'happypythoncoder@gmail.com'
email_password = 'tesuafawkeyxpppj' 

email_receiver = 'evzen21@post.cz'

subject = 'Smile, it is email from sender'
body = """
If you get this email, it means I am already good in coding :)
""" 

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string()) 
