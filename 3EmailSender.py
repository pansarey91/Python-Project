import smtplib

print("Welcome to Email Sender")
print("\n Login to your Gmail account")
your_email_address=input("\n Enter your email address: ")
your_password=input("\n Enter your password: ")

print("\n Logged in successfully")


to=input("Enter the recipient's email address: ")
content=input("Enter the content: ")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(your_email_address, your_password)
    server.sendmail(your_email_address, to, content)
    server.close()

sendEmail(to, content)