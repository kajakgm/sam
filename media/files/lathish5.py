from tkinter import*
from tkinter import PhotoImage
import random
import smtplib
otp=str(random.randint(000000,999999))
print(otp)
sender_address="lathishwaran522@gmail.com"
sender_pwd="kyjv hipf xuxi xyer"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_address,sender_pwd)
msg=f'''subject:regarding to otp..\n
Your otp is:{otp}'''
#server.sendmail(sender_address,)
b=Tk()
def x():
    pass
def sendotp_fun(ot):
    server.sendmail(sender_address,ot,msg)
def f():
    reg=Tk()
    eml=Label(reg,text="enter email")
    eml.place(x=10,y=100)
    email_ent=Entry(reg)
    email_ent.place(x=80,y=100)
    send_otp=Button(reg,text='send otp',command=lambda:sendotp_fun(email_ent.get()))
    send_otp.place(x=340,y=100)
b.geometry('400x600')
####photo images######
ph=PhotoImage(file='C:/Users/admin-pc/Pictures/Capture.png')
imgl=Label(b,image=ph)
imgl.image=ph
imgl.pack()
########
l=Label(b,text="username")
l.place(x=100,y=50)
e=Entry()
e.place(x=170,y=50)
l=Label(b,text="password")  
l.place(x=100,y=100)
e1=Entry()
e1.place(x=170,y=100)
b11=Button(b,text="login",command=x)
b11.place(x=100,y=200)
b1=Button(b,text="register",command=f)
b1.place(x=200,y=200)   

