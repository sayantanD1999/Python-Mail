import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
sender_email = input("Enter your email id ")
sender_email_pswd = input("Enter your password ")

server.login(sender_email,sender_email_pswd)

receiver_email = input("Enter receiver's mail id ")
mssg = input("Enter the message : ")
server.sendmail(sender_email,receiver_email,mssg)
server.quit()
