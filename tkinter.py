from tkinter import *
import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "fettebobb912@gmail.com"
    msg['from'] = user
    password = "gehjiczrvzvkuwse"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert("HELP", "I cant use my phone and need your help", "michael.sekol@mahoningctc.com")

window = Tk()
button = Button(window, text='Alert')
button.config(command= email_alert)#preforms alert
button.config(font=('Arial',50,'bold'))
button.config(bg='#f42a2a')
button.config(activebackground='#46c121')
button.pack()
window.mainloop()