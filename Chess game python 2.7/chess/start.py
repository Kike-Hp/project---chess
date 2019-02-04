#!/usr/bin/env python

#importy
#----------------------------------------------
import Tkinter as tk
from PIL import ImageTk
#----------------------------------------------

class Start:
    
    def __init__(self):
        self.main = tk.Tk()
        self.main.geometry("350x180")
        self.main.resizable(False, False)
        self.var = tk.StringVar()
        self.var.set("black")
        self.create_menu()
    
    def check(self,event):
        nick = self.nickname_input.get()
        ip = self.ipserver_input.get()
        color = self.var.get()
        if nick == '':
            self.error_nick.config(text = "Wrong nick", fg = 'red')
            return
        else:
            self.error_nick.config(text = "ok", fg = 'green')
        for sign in nick:
            if ord(sign) > 128:
                self.error_nick.config(text = "Nick have non ASCII characters", fg = 'red')
                return
            else:
                self.error_nick.config(text = "ok", fg = 'green')
        for val in ip:
            if ord(val) > 128:
                self.error_ip.config(text = "Ip have non ASCII characters", fg = 'red')
                return
            else:
                self.error_ip.config(text = "ok", fg = 'green')
        
    def create_menu(self):
        self.nickname = tk.Label(self.main, text = "Nickname  :")
        self.nickname_input = tk.Entry(self.main)
        self.ipserver = tk.Label(self.main, text = "Ip Serwera :")
        self.ipserver_input = tk.Entry(self.main)
        self.ipserver_input.insert(tk.END, "127.0.0.1")
        self.color = tk.Label(self.main, text = "color :")
        self.color_input_w = tk.Radiobutton(self.main, text = "white", variable = self.var, value = "white", indicatoron = False, selectcolor = "#C0C0C0")
        self.color_input_b = tk.Radiobutton(self.main, text = "black", variable = self.var, value = "black", indicatoron = False, selectcolor = "#000000")
        self.error_nick = tk.Label(self.main, text = "Only ASCII characters", fg = "yellow", font = ('',8))
        self.error_ip = tk.Label(self.main, text = "Only ASCII characters", fg = "yellow", font = ('',8))
        self.start_but = tk.Button(self.main, text = 'Start')
        self.start_but.bind('<Button-1>', self.check)
        self.show_menu()
    
    def show_menu(self):
        self.nickname.place(x = 30, y = 20)
        self.nickname_input.place(x = 120, y = 20)
        self.ipserver.place(x = 30, y = 60)
        self.ipserver_input.place(x = 120, y = 60)
        self.color.place(x = 30, y = 100)
        self.color_input_w.place(x = 100, y = 100)
        self.color_input_b.place(x = 160, y = 100)
        self.start_but.place(x = 280, y = 140)
        self.error_nick.place(x = 150, y = 45, height = 15)
        self.error_ip.place(x = 150, y = 85, height = 15)
        
    def start(self):
        self.main.mainloop()
    

