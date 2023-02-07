import smtplib
from email.message import EmailMessage
import imghdr
import os

  
email_subject = "Email test from Python"
sender_email_address = "jyothika8141@gmail.com"
receiver_email_address = "jyothika8141@gmail.com"
email_smtp = "smtp.gmail.com"
email_password = os.getenv('pass')

message = EmailMessage()

message['Subject'] = email_subject
message['From'] = sender_email_address
message['To'] = receiver_email_address
  

with open('image_mars', 'rb') as file:
   image_data = file.read()
  

message.set_content("Email from Python with image attachment")

message.add_attachment(image_data, maintype='image', subtype=imghdr.what(None, image_data))


server = smtplib.SMTP(email_smtp, '587')
server.ehlo()

server.starttls()
  

server.login(sender_email_address, email_password)
server.send_message(message)
server.quit()