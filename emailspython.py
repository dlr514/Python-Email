import smtplib, ssl

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "danielr2460100@gmail.com"
        self.password = ""

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()

if __name__ == '__main__':
    mails = input("Enter email address: ").split()
    subject = input("Enter subject: ")
    content = input("Enter content: ")

    # To take input from the user,
    n = int(input("Enter number of emails: "))
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        mail = Mail()
        mail.send(mails, subject, content)
        print(i)
        print("done")
        i = i+1  


