import time
import tkinter.messagebox
from tkinter import *
import sys
import tkhtmlview
import sqlite3


def apply_theme(theme):

    #make the theme all lower case
    selected_theme = theme.lower()

    with open("default.txt", 'w') as f:
        f.write(selected_theme)       
    time.sleep(1)
    ans = tkinter.messagebox.askokcancel("Success", "Theme applied successfully. Restart to take effect.")

    if ans == TRUE:
        sys.exit()
    else:
        return

def custom_theme_docs(e):
    custom_theme_window = Toplevel()
    custom_theme_window.title("Custom Theme")
    custom_theme_window.geometry("1200x700")
    custom_theme_window.configure(background="#fff")
    custom_theme_label = tkhtmlview.HTMLLabel(custom_theme_window, html="""
    <h1>How to use custom themes?</h1>
    <p>Make your experience better by using custom themes by yourself or maybe our future market place.</p>
    <h2>How to make a custom theme?</h2>
    <p>You can make a custom theme by following these steps:</p>
    <ol>
        <li>Create a new .json file in the themes folder.</li>
        <li>Add the keys to the json file</li>
        <li>Add the values to the json file</li>
        <li>Save the file</li>
        <li>Update default.txt</li>
    <ol>
    <h3>Creating a new .json file in themes folder</h3>
    <p>If you take a dive inside the themes folder, you will see a 2 files light.json and dark.json, each are json files containing data of specific colours and images that makes GUI look specific to the theme.</p>
    <p>The light.json file contains the data for light theme and the dark.json file contains the data for dark theme.</p>
    <p>The key names are the same as the ones in the json file, but the values are the colours and images that you want to use.</p>
    <p>Take a look inside one of the json files and you will able to understand how to make a custom theme.</p>
    <p>Also take a look at template.json file, it is a template for creating a new json file.</p>
    <img src="src/res/template.png"></img>
    </p>
    <p>Now create your own theme by naming it specificly, example "my_theme.json"</p>
    <p>Update the values but make sure to keep the keys same as the ones in the json file.</p>
    <p>It should look like this:</p>
    <img src="src/res/template_custom.png"></img>
    <h3>Updating the default.txt</h3>
    <p>Now update the default.txt file to make the theme work.</p>
    <p>This step is really necessary to do it properly.</p>
    <p>Open the default.txt file and write the <strong>exactly</strong> name of the theme you just created.</p>
    <p>Example:</p>
    <p>my_theme</p>
    <p>Now restart the program and it will take effect.</p>
    """
    )


    custom_theme_label.pack(fill=BOTH, expand=YES)

def on_click_link_about():
    #create a new window
    about_window = Toplevel()
    about_window.title("About Optimal")
    about_window.geometry("600x600")
    about_window.configure(background="#fff")
    about_label = tkhtmlview.HTMLLabel(about_window, html="""
    <h1>Optimal Password Holder</h1>
    <p>Optimal is a password holder that uses your system to hold your password secured. It is not connected to any web server, so it is all in your pc saving your critical hard passwords with a good GUI to access them all. Your passwords are encrypted so if someone tries to steal the database it will be stored perfectly without, losses. Optimal can also alert when detected a security breach in your pc trough a malware</p>
    <p>Optimal is a free open-source project. You can ask for help in the discord or request a chance to contribute. As optimal is a secured password holder, code cannot be shared with anyone</p>
    <a href="https://github.com/PlayZBhai/optimal-password-vault/blob/main/README.md">Visit Github for more information</a>
    <p>© 2022 PlayZBhai</p>""")
    about_label.pack(fill=BOTH, expand=YES)
    
def add_new_entry():

    #global every variable in the function
    global titleImg
    global webImg
    global userImg
    global passImg
    global tbImg
    global textbox_label
    global textbox_label_2
    global textbox_label_3

    conn = sqlite3.connect('protected/optimal.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, title text, username text, password text, url text, notes text)")
    conn.commit()
    conn.close()

    add_window = Toplevel()
    add_window.title("Add New Entry")
    add_window.geometry("500x300")
    add_window.resizable(0,0)
    add_window.configure(background="#fff")

    titleImg = PhotoImage(file="src/entries/add_entry.png")
    webImg = PhotoImage(file="src/entries/Website.png")
    userImg = PhotoImage(file="src/entries/Username.png")
    passImg = PhotoImage(file="src/entries/Password.png")
    cancelImg = PhotoImage(file="src/entries/cancel.png")
    cancelImg_hover = PhotoImage(file="src/entries/cancel_hover.png")
    saveImg = PhotoImage(file="src/entries/save.png")
    saveImg_hover = PhotoImage(file="src/entries/save_hover.png")
    tbImg = PhotoImage(file="src/entries/tb2.png")

    #add the titleImg in the app
    title_label = Label(add_window, image=titleImg, bg="#fff")
    title_label.place(x=196, y=18)
    
    web_label = Label(add_window, image=webImg, bg="#fff")
    web_label.place(x=98, y=110)

    user_label = Label(add_window, image=userImg, bg="#fff")
    user_label.place(x=98, y=140)

    pass_label = Label(add_window, image=passImg, bg="#fff")
    pass_label.place(x=98, y=170)

    textbox_label = Label(add_window, image=tbImg, bg="#fff")
    textbox_label.place(x=193, y=110)

    textbox_label_2 = Label(add_window, image=tbImg, bg="#fff")
    textbox_label_2.place(x=193, y=140)

    textbox_label_3 = Label(add_window, image=tbImg, bg="#fff")
    textbox_label_3.place(x=193, y=170)

    #add the textbox
    web_textbox = Entry(add_window, width=24, bg="#CFE2FF", fg="#000", borderwidth=0, highlightthickness=0, relief="flat", font=("Roboto", 12), justify=CENTER)
    web_textbox.place(x=200, y=110)

    user_textbox = Entry(add_window, width=24, bg="#CFE2FF", fg="#000", borderwidth=0, highlightthickness=0, relief="flat", font=("Roboto", 12), justify=CENTER)
    user_textbox.place(x=200, y=140)

    pass_textbox = Entry(add_window, width=24, bg="#CFE2FF", fg="#000", borderwidth=0, highlightthickness=0, relief="flat",font=("Roboto", 12), justify=CENTER)
    pass_textbox.place(x=200, y=170)

    cancel_btn = Button(add_window, image=cancelImg, bg="#fff", background="#fff", borderwidth=0, highlightthickness=0, activebackground="#fff", activeforeground="#fff", command=lambda: add_window.destroy())
    cancel_btn.place(x=62, y=250)

    save_btn = Button(add_window, image=saveImg, bg="#fff", background="#fff", borderwidth=0, highlightthickness=0, activebackground="#fff", activeforeground="#fff")
    save_btn.place(x=307, y=250)

    cancel_btn.bind("<Enter>", lambda event: cancel_btn.configure(image=cancelImg_hover, cursor='hand2'))
    cancel_btn.bind("<Leave>", lambda event: cancel_btn.configure(image=cancelImg))

    save_btn.bind("<Enter>", lambda event: save_btn.configure(image=saveImg_hover, cursor='hand2'))
    save_btn.bind("<Leave>", lambda event: save_btn.configure(image=saveImg))