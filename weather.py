import tkinter as tk
import requests
import re
from bs4 import BeautifulSoup

font = "游ゴシック"
def GetWea():
    url="https://weather.com/ja-JP/weather/today/l/42.36,-71.22"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def GetApi():
    wetherapikey = "80efcb09546b956c8fa14024be0cd5fa"
    lat = "42.35"
    lon = "-71.16"
    return requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon="+lon +"&exclude=dairy&appid="+wetherapikey+"&lang=ja&units=metric").json()


def temp(master,size,basecolor):
    global Temple
    Temple = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    Temple.pack()

def place(master,size,basecolor):
    global Place
    Place = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    Place.pack()

def condition(master,size,basecolor):
    global Condition
    Condition = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    Condition.pack()


def MaxTemp(master,size,basecolor):
    global maxtemp
    maxtemp = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    maxtemp.pack()

def LowTemp(master,size,basecolor):
    global lowtemp
    lowtemp = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    lowtemp.pack()

def humidity(master,size,basecolor):
    global currenthumidity
    currenthumidity = tk.Label(master=master,font=(font,size),fg="white",bg=basecolor)
    currenthumidity.pack()

class reload:
    def setup(self):
        Place["text"]=GetWea().find(class_=re.compile("CurrentConditions--location--kyTeL")).contents[0]
    def min(self):
        Temple["text"]=GetWea().find(class_=re.compile("CurrentConditions--tempValue--3a50n")).contents[0]+"C"
        Condition["text"]=GetWea().find(class_=re.compile("CurrentConditions--phraseValue--2Z18W")).contents[0]
        #maxtemp["text"]="最高:"+str(GetApi()["daily"][0]["temp"]["max"])+ "℃"
        #lowtemp["text"]="最低:"+str(GetApi()["daily"][0]["temp"]["min"])+ "℃"
        currenthumidity["text"]="湿度:"+str(GetApi()["current"]["humidity"])+ "%"
    def second(self):
        None
    def milisecond(self):
        None