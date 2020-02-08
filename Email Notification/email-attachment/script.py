import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

contacts = ['test@example.com', 'abc@example.com']

msg = EmailMessage()
msg['Subject'] = 'Test Subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
#msg.set_content('You can edit this content!')

#ATTACH IMAGES
#msg.set_content('Image attached...')
#files = ['image.png']

#ATTACH PDF
# msg.set_content('PDF attached...')
# files = ['resume.pdf']

#ADD HTML
msg.set_content('This is a plain text email')
msg.add_alternative("""\
<html>
<body>
    <h1 style="color: blue">This is an HTML Email!</h1>
</body>
</html>
""", subtype='html')


# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         #file_type = imghdr.what(f.name)
#         file_name = f.name
    
#     # msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

#     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
