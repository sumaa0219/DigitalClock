import requests
import tkinter as tk

font = "游ゴシック"

def Temp(master,size,basecolor):
    global temp
    temp = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    temp.pack()

def Hum(master,size,basecolor):
    global hum
    hum = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    hum.pack()

class reload:
    def setup(self):
        None
    def min(self):      
        temp["text"]="気温:"+str(requests.get("https://sssumaa.net/api/status?element=tempreture&type=R").text) + "℃"
        hum["text"]="湿度:"+str(requests.get("https://sssumaa.net/api/status?element=humidity&type=R").text)+ "%"
    def second(self):
        None
    def milisecond(self):
        None