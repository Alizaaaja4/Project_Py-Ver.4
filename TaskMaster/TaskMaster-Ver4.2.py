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

labelfr = LabelFrame(root, text = "result", padx=20, pady=20)
labelfr.place(x = 60, y=380)

nama = Label(root, text ="Firts Name")
nama2 = Label(root, text="Last Name")
email = Label(root, text="Email")
username = Label(root, text="Username")
password = Label(root, text="Password")

e1 = Entry(root, width=40)
e2 = Entry(root, width=40)
e3 = Entry(root, width=40)
e4 = Entry(root, width=40)
e5= Entry(root, width=40, show="*")

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

def cetak():
    class user:
        def __init__(self,nama,nama2,email,username,password):
            self.nama = nama
            self.nama2 =nama2
            self.email = email
            self.username = username
            self.password = password
        
        def hasil(self):
            lbl = Label(labelfr, text="Firts Name ="+self.nama+"\nLast Name ="+self.nama2+"\nEmail ="+self.email+"\nUsername ="+self.username+"\nPassword ="+self.password).grid()

    ditampilkan= user(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    ditampilkan.hasil()

btn = Button(root, text ="Submit", command=cetak).place(x=120 , y=300)

root.mainloop()
