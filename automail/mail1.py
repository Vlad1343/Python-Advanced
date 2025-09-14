
# import smtplib    #Library for sending emails using SMTP
# import getpass    #Library for securely handling password prompts.

# sender_email = input("Enter your email address: ")
# password = getpass.getpass("Enter your password: ")   #App Password
# receiver_email = input("Enter recipient email address: ")

# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login(sender_email, password)
# smtpObj.sendmail(sender_email,
#                  receiver_email,
#                  'Subject: Test Email\n\nThis is a test email sent from Python.')




# import imapclient  #Library that makes working with IMAP easier(reading emails).
# import pyzmail     #Library for parsing email messages.

# imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
# imapObj.select_folder('INBOX', readonly=True)
# UIDs = imapObj.search(['SINCE 05-Jul-2014'])
# UIDs
# rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
# message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
# message.get_subject()
# message.get_addresses('from')
# message.get_addresses('to')
# message.get_addresses('cc')
# message.get_addresses('bcc')
# message.text_part != None
# message.text_part.get_payload().decode(message.text_part.charset)
# message.html_part != None
# message.html_part.get_payload().decode(message.html_part.charset)
# imapObj.logout()

# You can only get ID's
# imapObj.search(['ON 05-Jul-2015'])
# imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN'])
# imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com'])
# imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com'])


# Get actual content
# import pprint
# rawMessages = imapObj.fetch(UIDs, ['BODY[]']) 
# pprint.pprint(rawMessages)



# import imapclient
# import pyzmail
# import pprint

## Get a list of folders
# pprint.pprint(imapObj.list_folders())
# # Connect to Gmail IMAP server
# imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# imap_obj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')

# # Select the INBOX in read-only mode
# imap_obj.select_folder('INBOX', readonly=True)

# # Search for messages since a specific date
# uids = imap_obj.search(['SINCE 05-Jul-2014'])
# print("Found UIDs:", uids)

# # Fetch the latest message
# if uids:
#     latest_uid = uids[-1]
#     raw_messages = imap_obj.fetch([latest_uid], ['BODY[]', 'FLAGS'])
#     message = pyzmail.PyzMessage.factory(raw_messages[latest_uid]['BODY[]'])

#     # Display message details
#     print("Subject:", message.get_subject())
#     print("From:", message.get_addresses('from'))
#     print("To:", message.get_addresses('to'))
#     print("CC:", message.get_addresses('cc'))
#     print("BCC:", message.get_addresses('bcc'))

#     # Print message body (text and HTML parts)
#     if message.text_part:
#         print("Text Part:")
#         print(message.text_part.get_payload().decode(message.text_part.charset))

#     if message.html_part:
#         print("HTML Part:")
#         print(message.html_part.get_payload().decode(message.html_part.charset))

# # Logout
# imap_obj.logout()