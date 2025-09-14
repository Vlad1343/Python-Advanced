import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('vladshutkevych@gmail.com', 'llsu mtpl yhno pxkw')  # Replace with your App Password
smtpObj.sendmail('vladshutkevych@gmail.com',
                 'vladshut476@gmail.com',
                 'Subject: Test Email\n\nThis is a test email sent from Python.')
smtpObj.quit()