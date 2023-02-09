import smtplib
from email.message import EmailMessage
import imghdr
import os

def mail(lst):  
   receiver_email_address = lst[0]
   email_subject = lst[1]
   
   email_smtp = "smtp.gmail.com"
   sender_email_address = "jyothika8141@gmail.com"
   email_password = os.getenv('pass')

   message = EmailMessage()

   message['Subject'] = email_subject
   message['From'] = sender_email_address
   message['To'] = ",".join(receiver_email_address)
   
   message.set_content(lst[2])

   with open('image_mars', 'rb') as file:
      image_data = file.read()

   message.add_attachment(image_data, maintype='image', subtype=imghdr.what(None, image_data))


   server = smtplib.SMTP(email_smtp, '587')
   server.ehlo()

   server.starttls()
   
   
   server.login(sender_email_address, email_password)
   server.send_message(message)
   print("email sent")
   server.quit()