from tkinter import *
import json
import tkinter.messagebox
import src.main.funcs as funcs
import time
import os



class Optimal:
    def __init__(self, master):

        try:
            with open('default.txt', 'r') as f:
                self.default = f.read()
        except:
            with open('default.txt', 'w') as f:
                f.write('dark')
            with open('default.txt', 'r') as f:
                self.default = f.read()
                time.sleep(2)

        if self.default == 'light':
            with open("src/themes/light.json", "r") as f:
                self.data = json.load(f)
                self.navbar_background = self.data['navbar_background']
                self.navbar_foreground = self.data['navbar_title']
                self.navbar_links   = self.data['navbar_links']
                self.bg_color = self.data["background_color"]
                self.navbar_links_hover = self.data['navbar_links_hover']
                self.addImg = self.data['addImg']
                self.addImg_hover = self.data['addImg_hover']
        elif self.default == 'dark':
            with open("src/themes/dark.json", "r") as f:
                self.data = json.load(f)
                self.navbar_background = self.data['navbar_background']
                self.navbar_foreground = self.data['navbar_title']
                self.navbar_links   = self.data['navbar_links']
                self.bg_color = self.data["background_color"]
                self.navbar_links_hover = self.data['navbar_links_hover']
                self.addImg = self.data['addImg']
                self.addImg_hover = self.data['addImg_hover']
        else:
            with open(f"src/themes/{self.default}.json", "r") as f:
                self.data = json.load(f)
                self.navbar_background = self.data['navbar_background']
                self.navbar_foreground = self.data['navbar_title']
                self.navbar_links   = self.data['navbar_links']
                self.bg_color = self.data["background_color"]
                self.navbar_links_hover = self.data['navbar_links_hover']
                self.addImg = self.data['addImg']
                self.addImg_hover = self.data['addImg_hover']

        self.master = master
        self.master.title("Optimal Password Holder")
        self.master.geometry("1300x600")
        self.master.configure(background="#fff")

        self.navbar = Frame(self.master, bg=f"{self.navbar_background}", height=60, padx=10, pady=10)
        self.navbar.pack(fill=X)

        self.title = Label(self.navbar, text="Optimal Password Holder", bg=f"{self.navbar_background}", fg=f"{self.navbar_foreground}", font=("Helvetica", 25))
        self.title.pack(side=LEFT, padx=10)

        if self.default == 'light':
            self.border = Frame(self.master, bg="#c4c4c4", height=2, width=1300)
            self.border.pack(fill=X)
        elif self.default == 'dark':
            self.border = Frame(self.master, bg="#00ffff", height=2, width=1300)
            self.border.pack(fill=X)
        else:
            with open(f"src/themes/{self.default}.json", "r") as f:
                self.data = json.load(f)
                self.border = Frame(self.master, bg=f"{self.data['border']}", height=2, width=1300)
                self.border.pack(fill=X)

        self.body = Frame(self.master, bg=f"{self.bg_color}", padx=10, pady=10)
        self.body.pack(fill=BOTH, expand=True)

        self.link_theme = Label(self.navbar, text="Theme", bg=f"{self.navbar_background}", fg=f"{self.navbar_links}", font=("Helvetica", 15))
        self.link_theme.pack(side=RIGHT, padx=10)

        def on_hover_link_theme(event):
            self.link_theme.config(cursor="hand2", fg=f"{self.navbar_links_hover}")


        def off_hover_link_theme(event):
            self.link_theme.config(cursor="arrow", fg=f"{self.navbar_links}")
        
        self.link_theme.bind("<Enter>", on_hover_link_theme)
        self.link_theme.bind("<Leave>", off_hover_link_theme)

        def on_click_link_theme(event):
            self.theme_window = Toplevel(self.master)
            self.theme_window.title("Theme")
            self.theme_window.geometry("500x400")
            self.theme_window.configure(background="#fff")
            self.theme_window.resizable(False, False)

            self.theme_window.theme_frame = Frame(self.theme_window, bg="#fff", height=100, width=300)
            self.theme_window.theme_frame.pack(fill=X)

            self.theme_window.theme_label = Label(self.theme_window.theme_frame, text="Theme", bg="#fff", font=("Helvetica", 15))
            self.theme_window.theme_label.pack(side=LEFT, padx=10)

            self.theme_window.theme_var = StringVar()
            self.theme_window.theme_var.set(self.default)

            self.theme_window.theme_dropdown = OptionMenu(self.theme_window.theme_frame, self.theme_window.theme_var, "Light", "Dark")
            self.theme_window.theme_dropdown.pack(side=RIGHT, padx=10)
            self.theme_window.theme_dropdown.config(width=20)
            self.theme_window.theme_dropdown.config(relief=FLAT)
            self.theme_window.theme_dropdown.config(font=("Helvetica", 15), bg="#fff")

            self.custom_theme = Label(self.theme_window, text="Custom Theme", bg="#fff", font=("Helvetica", 15, UNDERLINE), cursor="hand2", fg="blue")
            self.custom_theme.pack(padx=10, pady=5)

            self.custom_theme.bind("<Button-1>", funcs.custom_theme_docs)

            self.applybtn_img = PhotoImage(file="src/res/apply_btn.png")
            self.applybtn = Button(self.theme_window, text="Apply", bg="#fff", fg="#000", font=("Helvetica", 15), relief=FLAT, cursor='hand2', command=lambda: funcs.apply_theme(self.theme_window.theme_var.get()), image=self.applybtn_img, activebackground="#fff", highlightbackground="#fff", highlightthickness=0, borderwidth=0)
            self.applybtn.pack(side=BOTTOM, pady=10)

        self.link_theme.bind("<Button-1>", on_click_link_theme)

        def on_click_link_about(e):
            funcs.on_click_link_about()
        
        self.link_about = Label(self.navbar, text="About", bg=f"{self.navbar_background}", fg=f"{self.navbar_links}", font=("Helvetica", 15))
        self.link_about.pack(side=RIGHT, padx=10)
        self.link_about.bind("<Enter>", lambda event: self.link_about.config(cursor="hand2", fg=f"{self.navbar_links_hover}"))
        self.link_about.bind("<Leave>", lambda event: self.link_about.config(cursor="arrow", fg=f"{self.navbar_links}"))
        self.link_about.bind("<Button-1>", on_click_link_about)

        self.mainFrame = Frame(self.body, bg=f"{self.bg_color}", height=100, width=100)
        self.mainFrame.pack(fill=BOTH, expand=True)
        


        self.add_btn_img = PhotoImage(file=self.addImg)
        self.add_btn_img_hover = PhotoImage(file=self.addImg_hover)
        self.addBtn = Button(self.mainFrame, text="Add", bg=f"{self.bg_color}", font=("Helvetica", 15), relief=FLAT, cursor='hand2', image=self.add_btn_img, activebackground="{}".format(self.bg_color), highlightbackground="{}".format(self.bg_color), highlightthickness=0, borderwidth=0, command=funcs.add_new_entry)
        self.addBtn.pack(side=RIGHT, anchor=NE)
        self.addBtn.bind("<Enter>", lambda event: self.addBtn.config(cursor="hand2", image=self.add_btn_img_hover))
        self.addBtn.bind("<Leave>", lambda event: self.addBtn.config(cursor="arrow", image=self.add_btn_img))