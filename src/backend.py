import sqlite3
import tkinter.messagebox
import sys
import time
import hashlib
from tkinter import Tk
from src.optimal import Optimal


def encrypt(password):
    hash_obj = hashlib.md5(password.encode())
    md5_hash = hash_obj.hexdigest()
    return md5_hash 

def create_password(self, password):
    if password == "":
        tkinter.messagebox.showinfo("Error", "Please enter a password")
        return
    elif len(password)<8:
        tkinter.messagebox.showinfo("Error", "Password must be at least 8 characters long")
        return
    elif not any(char.isdigit() for char in password):
        tkinter.messagebox.showinfo("Error", "Password must contain at least one number")
        return
    elif len(password) <= 0:
        tkinter.messagebox.showinfo("Error", "Please enter a password")
        return

    ans = tkinter.messagebox.askquestion("Confirm", "Are you sure you want to create this password?\nMake sure you've to reset everything inside the app if you forget this password.")

    if(ans == "yes"):
        conn = sqlite3.connect("passwords.db")
        c = conn.cursor()
        pas = encrypt(password)
        c.execute("INSERT INTO passwords VALUES (?)", (pas,))
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo("Success", "Password created successfully. Restart to take effect.")
        sys.exit()
    else:
        return

def createOptimalInstance(loginApp, passGiven):
    # loginApp.destroy()
    # root = Tk()
    # OptimalInstance = Optimal(root)
    # root.mainloop()
    passGivenHash = str(encrypt(passGiven))
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    data = c.fetchall()


    if passGiven == "":
        tkinter.messagebox.showinfo("Error", "Please enter a password")
    elif passGivenHash == data[0][0]:
        loginApp.destroy()
        root = Tk()
        OptimalInstance = Optimal(root)
        root.mainloop()
    else: 
        tkinter.messagebox.showinfo("Error", "Incorrect password")
        return

