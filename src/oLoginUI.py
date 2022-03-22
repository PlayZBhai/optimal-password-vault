from tkinter import *
from src.backend import create_password, encrypt, createOptimalInstance
import sqlite3
import threading
import time

class oLoginUI:
    def __init__(self, master):

        self.master = master
        self.master.title("Login Optimal")
        self.master.geometry("736x458")
        self.master.resizable(width=False, height=False)
        self.master.configure(background="#fff")

        self.Label1 = Label(self.master, text="Optimal Password Holder", font=("Helvetica", 36), background="#fff")
        self.Label1.place(x=100, y=46)

        self.label2 = Label(self.master, text="Enter Login Password", font=("Helvetica", 24), background="#fff")
        self.label2.place(x=200, y=137)

        self.textboxImg = PhotoImage(file="src/res/tb1.png")
        self.label3 = Label(self.master, image=self.textboxImg, bg="#fff")
        self.label3.place(x=79, y=181)

        self.textbox = Entry(self.master, font=("Helvetica", 14), show="*", width=49, justify=CENTER, bg="#c4c4c4", relief=FLAT, fg='#000')
        self.textbox.place(x=100, y=185)

        def showPass(self):
            if self.textbox.get() == "":
                self.textbox.config(show="*")
            else:
                self.textbox.config(show="")

        self.showIcon = PhotoImage(file="src/res/eye.png")
        self.showBtn = Button(self.master, image=self.showIcon, bg="#c4c4c4", width=20, height=20, relief=FLAT, cursor="hand2", activebackground="#c4c4c4", activeforeground="#000", command=lambda: showPass(self))
        self.showBtn.place(x=675, y=185)

        #adding main butttons
        self.btn1Image = PhotoImage(file="src/res/btn1.png")
        self.btn2Image = PhotoImage(file="src/res/btn2.png")
        self.btn1Image_hover = PhotoImage(file="src/res/btn1_hover.png")
        self.btn2Image_hover = PhotoImage(file="src/res/btn2_hover.png")

        self.createBtn = Button(self.master, image=self.btn1Image, bg="#fff", relief=FLAT, cursor="hand2", activebackground="#fff", activeforeground="#fff", borderwidth=0)
        self.loginBtn = Button(self.master, image=self.btn2Image, bg="#fff", relief=FLAT, cursor="hand2", activebackground="#fff", activeforeground="#fff", borderwidth=0)
        self.createBtn.place(x=79, y=235)
        self.loginBtn.place(x=379, y=235)

        self.createBtn.bind("<Enter>", lambda event: self.createBtn.config(image=self.btn1Image_hover))
        self.createBtn.bind("<Leave>", lambda event: self.createBtn.config(image=self.btn1Image))
        self.loginBtn.bind("<Enter>", lambda event: self.loginBtn.config(image=self.btn2Image_hover))
        self.loginBtn.bind("<Leave>", lambda event: self.loginBtn.config(image=self.btn2Image))


        self.settingIcon = PhotoImage(file="src/res/settings.png")
        self.settingBtn = Button(self.master, image=self.settingIcon, bg="#fff", relief=FLAT, cursor="hand2", activebackground="#fff", activeforeground="#fff", borderwidth=0)
        self.settingBtn.place(x=650, y=416)

        self.settingBtn.bind("<Enter>", lambda event: self.settingBtn.config(bg="#c4c4c4"))
        self.settingBtn.bind("<Leave>", lambda event: self.settingBtn.config(bg="#fff"))

        #db intialization
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS passwords (passwords TEXT)")
        c.execute("SELECT * FROM passwords")
        if c.fetchone() is not None:
            self.createBtn.config(state=DISABLED)


        c.execute("SELECT * FROM passwords")

        if c.fetchone() is None:
            self.loginBtn.config(state=DISABLED)
        conn.close()
        #end db intialization
        
        
        

        self.createBtn.config(command=lambda: create_password(self.master, self.textbox.get()))
        self.loginBtn.config(command=lambda: createOptimalInstance(self.master, self.textbox.get()))     