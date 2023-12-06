import csv
import webbrowser
import tkinter.font
from tkinter import *

root = Tk()

root.geometry("300x600") #display dari ukuran tkinter
root.title("TaskMaster") #memberikan nama dari aplikasi
root.iconbitmap("icon_task.ico") #menmabah icon

changefont = tkinter.font.Font(size=20)

judul = Label(root, text = "REGISTER", font = changefont)
judul.place(x=80, y = 15)

nama = Label(root, text ="Firts Name")
nama2 = Label(root, text="Last Name")
email = Label(root, text="Email")
username = Label(root, text="Username")
password = Label(root, text="Password")

e1 = Entry(root, width=40)
e2 = Entry(root, width=40)
e3 = Entry(root, width=40)
e4 = Entry(root, width=40)
e5= Entry(root, width=40)

nama.place(x=20, y=60)
nama2.place(x=20, y=100)
email.place(x=20, y=140)
username.place(x=20, y=180)
password.place(x=20, y=220)

e1.place(x=20, y=80)
e2.place(x=20, y=120)
e3.place(x=20, y=160)
e4.place(x=20, y=200)
e5.place(x=20, y=240)

btn = Button(root, text ="Submit").place(x=120 , y=300)
root.mainloop()