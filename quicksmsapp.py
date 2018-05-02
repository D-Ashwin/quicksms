import zerosms
import tkinter
from tkinter import *

def send():
	username=username_box.get()
	password=password_box.get()
	rec_num=receiver_box.get()
	message=message_box.get("1.0",END)
	if username!='' and password !='' and rec_num!='' and message!='':
		zerosms.sms(phno=username,passwd=password,message=message,receivernum=rec_num)
	else:
		print("Error:Check Fields")

win = Tk()
win.title('Quick SMS')
win.geometry('350x420')

Label(win, text="Send Quick SMS",fg="#18a3d0",font=("Times", "24", "bold italic")).pack(side=TOP, fill=X, padx=5, pady=25)

row = Frame(win)
row2 = Frame(win)
row3 = Frame(win)
row4 = Frame(win)

username_label = Label(row, text="Username")
username_label.pack(side=LEFT)

username_box = Entry(row)
username_box.insert(0, "9685358148")
username_box.pack(side=RIGHT, expand=YES ,fill=X)

password_label = Label(row2, text="Password")
password_label.pack(side=LEFT)

password_box = Entry(row2)
password_box.insert(0, "M9629A")
password_box.pack(side=RIGHT, expand=YES ,fill=X)

receiver_label = Label(row3, text="Receiver")
receiver_label.pack(side=LEFT)

receiver_box = Entry(row3)
receiver_box.pack(side=RIGHT, expand=YES ,fill=X)

message_label = Label(row4, text="Message")
message_label.pack(side=LEFT)

message_box = Text(row4,height=4, width=30)
message_box.pack(side=RIGHT,expand=YES,fill=X)

row.pack(side=TOP, fill=X, padx=5, pady=5)
row2.pack(side=TOP, fill=X, padx=5, pady=8)
row3.pack(side=TOP, fill=X, padx=5, pady=10)
row4.pack(side=TOP, fill=X, padx=5, pady=15)

btn = Button(win, text='Send Now!',fg="green", width=20,command=send).pack(padx=5,pady=12)
btn2 = Button(win, text='Quit!', fg="red",command=win.quit ,width=20).pack(padx=5,pady=18)


mainloop()
