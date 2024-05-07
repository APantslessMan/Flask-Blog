import smtplib

######
#           SMTP Connection info
######

SENDER = "email@gmail.com"
PASSWORD = "gmail auth password"
RECIPIENT = ['you@email.com']


class SendContact:
    def __init__(self, email, body, name):
        self.sender = SENDER
        self.password = PASSWORD
        self.recipients = RECIPIENT
        self.subject = f"You got a contact request from {name}!"
        self.body = (f"{name}, has sent you a contact request\n"
                     f"They would like to know: \n{body}"
                     f"\n\n You can get back to them at {email}")
        self.sent = 0
        self.smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def send_mail(self):
        email = 'Subject: {}\n\n{}'.format(self.subject, self.body)
        self.smtpserver.ehlo()
        self.smtpserver.login(self.sender, self.password)
        self.smtpserver.sendmail(self.sender, self.recipients, email)
        # Close the connection
        self.smtpserver.close()
