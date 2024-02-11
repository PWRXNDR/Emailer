import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from getpass import getpass

# Read the HTML content of the email
html = Template(Path('index.html').read_text())

# Prompt the user for their email details
sender_email = input("Enter your email: ")
recipient_email = input("Enter the recipient's email: ")
subject = input("Enter the subject of the email: ")
your_name = input("Enter your name: ")
passw = input('Enter your password: ')
password = getpass(passw)

# Create the email message
email = EmailMessage()
email['from'] = your_name
email['to'] = recipient_email
email['subject'] = subject

# Substitute the placeholder with the sender's name
email.set_content(html.substitute({'name': your_name}), 'html')

# Send the email
try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.send_message(email)
        print('Email sent successfully!')
except Exception as e:
    print(f"An error occurred: {e}")
