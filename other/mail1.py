
import smtplib
import getpass

sender_email = input("Enter your email address: ")
password = getpass.getpass("Enter your password: ")   #App Password
receiver_email = input("Enter recipient email address: ")

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sender_email, password)
smtpObj.sendmail(sender_email,
                 receiver_email,
                 'Subject: Test Email\n\nThis is a test email sent from Python.')