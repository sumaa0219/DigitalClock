import tkinter as tk
import datetime

font = "游ゴシック"

def GetTime():
    return datetime.datetime.now()

def Date(master,size,basecolor):
    global DateLabel
    DateLabel = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    DateLabel.pack()

def Time(master,size,basecolor):
    global TimeLabel
    TimeLabel = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    TimeLabel.pack()

def Second(master,size,basecolor):
    global SecondLabel
    SecondLabel = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    SecondLabel.pack()

class reload:
    def setup(self):
        None
    def min(self):
        DateLabel["text"]=GetTime().strftime('%m月%d日(%a)')
    def second(self):
        TimeLabel["text"]=GetTime().strftime("%H:%M")
    def milisecond(self):
        SecondLabel["text"]=GetTime().strftime("%S")