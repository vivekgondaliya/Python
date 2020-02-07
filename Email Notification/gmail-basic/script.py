import pandas as pd
import smtplib

'''
    Goal:
    Send email to list of users from excel file via gmail sender account

    Gmail Settings:
    My Account -> Sign-In & Security -> Apps with account access ->  Allow less secure apps: ON

    Input:   
        - excel_fileName : Excelsheet with "Emails" header
        - gmail_user
        - gmail_password
'''

#EDIT ME
gmail_user = "your_email@gmail.com"
gmail_password = "yourPassword1234"

excel_fileName = "email-list.xlsx"
excel_file = pd.read_excel(excel_fileName)

send_from = gmail_user
send_to = excel_file["Emails"].values
subject="This is a Subject"
body = "Hey, what's up?\n\n- Python Email Service"

#email without status
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (send_from, ", ".join(send_to), subject, body)

try:
    #server = smtplib.SMTP_SSL("smtp.gmail.com:465")
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(send_from, send_to, email_text)
    server.close()

    print('Email(s) sent!')
except:
    print('Uh oh, something went wrong...')

#email with status
# msg="This is a message" 
# subject="This is a Subject"
# body="Subject: {} \n\n {}".format(subject, msg)

# try:
#     #server = smtplib.SMTP_SSL("smtp.gmail.com:465")
#     server = smtplib.SMTP("smtp.gmail.com:587")
#     server.starttls()
#     server.login(gmail_user, gmail_password)

#     for index, recipientEmail in enumerate(send_to):
#         server.sendmail(send_from, recipientEmail, body)
#         print("Email Status: %d out of %d sent" % (index+1, len(send_to)))
    
#     server.close()
# except:
#     print('Uh oh, something went wrong...')


