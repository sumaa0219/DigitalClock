import tkinter as tk
import requests
import calender11 as CL
import DigitalClock as DC
import weather
import room

BaseBackColor = "black"

root = tk.Tk()
root.geometry("1024x600")
menubar = tk.Menu(root)
root.configure(menu = menubar,bg=BaseBackColor)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
# ～内容
filemenu.add_command(label = "Open File...")
# セパレーター
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = lambda: root.destroy())

calender = tk.LabelFrame(root,width=420, height=360,bg=BaseBackColor,bd=0)
CL.calender(calender,25,BaseBackColor)
calender.place(x=35,y=10)

time = tk.LabelFrame(root,width=455, height=160,bg=BaseBackColor,bd=0)
DC.Time(time,180,BaseBackColor)
time.place(x=475,y=40)

date = tk.LabelFrame(root,width=330, height=70,bg=BaseBackColor,bd=0)
DC.Date(date,50,BaseBackColor)
date.place(x=665,y=235)

second= tk.LabelFrame(root,width=75, height=55,bg=BaseBackColor,bd=0)
DC.Second(second,50,BaseBackColor)
second.place(x=930,y=165)

temp= tk.LabelFrame(root,width=240, height=110,bg=BaseBackColor,bd=0)
weather.temp(temp,100,BaseBackColor)
temp.place(x=520,y=465)

place= tk.LabelFrame(root,width=440, height=40,bg=BaseBackColor,bd=0)
weather.place(place,30,BaseBackColor)
place.place(x=520,y=345)

condition= tk.LabelFrame(root,width=240, height=45,bg=BaseBackColor,bd=0)
weather.condition(condition,30,BaseBackColor)
condition.place(x=765,y=400)

maxtemp= tk.LabelFrame(root,width=155, height=35,bg=BaseBackColor,bd=0)
weather.MaxTemp(maxtemp,35,BaseBackColor)
maxtemp.place(x=790,y=465)

lowtemp= tk.LabelFrame(root,width=155, height=35,bg=BaseBackColor,bd=0)
weather.LowTemp(lowtemp,35,BaseBackColor)
lowtemp.place(x=790,y=510)

humidity= tk.LabelFrame(root,width=155, height=35,bg=BaseBackColor,bd=0)
weather.humidity(humidity,35,BaseBackColor)
humidity.place(x=790,y=550)

RoTemp= tk.LabelFrame(root,width=185, height=50,bg=BaseBackColor,bd=0)
room.Temp(RoTemp,35,BaseBackColor)
RoTemp.place(x=110,y=480)

RoHum= tk.LabelFrame(root,width=185, height=50,bg=BaseBackColor,bd=0)
room.Hum(RoHum,35,BaseBackColor)
RoHum.place(x=110,y=540)


wea = weather.reload()
Digi = DC.reload()
Room = room.reload()

def startup():
    wea.setup()
    Digi.setup()
    Room.setup()
    print("setup")

def mini():
    wea.min()
    Digi.min()
    Room.min()
    root.after(60000,mini)
    
def secon():
    wea.second()
    Digi.second()
    Room.second()
    root.after(1000,secon)
    

def milisecond():
    wea.milisecond()
    Digi.milisecond()
    Room.milisecond()
    root.after(100,milisecond)


startup()
milisecond()
secon()
mini()

root.mainloop()