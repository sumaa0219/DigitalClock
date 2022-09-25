import tkinter as tk
import calender11 as CL
import DigitalClock as DC
import weather
import room

BaseBackColor = "black"

root = tk.Tk()
root.geometry("1920x1080")
menubar = tk.Menu(root)
root.configure(menu = menubar,bg=BaseBackColor)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
# ～内容
filemenu.add_command(label = "Open File...")
# セパレーター
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = lambda: root.destroy())

calender = tk.LabelFrame(root,width=720, height=635,bg=BaseBackColor,bd=0)
CL.calender(calender,40,BaseBackColor)
calender.place(x=50,y=30)

time = tk.LabelFrame(root,width=815, height=280,bg=BaseBackColor,bd=0)
DC.Time(time,320,BaseBackColor)
time.place(x=915,y=80)

date = tk.LabelFrame(root,width=555, height=100,bg=BaseBackColor,bd=0)
DC.Date(date,90,BaseBackColor)
date.place(x=1350,y=385)

second= tk.LabelFrame(root,width=125, height=95,bg=BaseBackColor,bd=0)
DC.Second(second,100,BaseBackColor)
second.place(x=1725,y=270)

temp= tk.LabelFrame(root,width=425, height=190,bg=BaseBackColor,bd=0)
weather.temp(temp,200,BaseBackColor)
temp.place(x=1015,y=810)

place= tk.LabelFrame(root,width=910, height=75,bg=BaseBackColor,bd=0)
weather.place(place,60,BaseBackColor)
place.place(x=985,y=515)

condition= tk.LabelFrame(root,width=495, height=90,bg=BaseBackColor,bd=0)
weather.condition(condition,80,BaseBackColor)
condition.place(x=1335,y=620)

maxtemp= tk.LabelFrame(root,width=360, height=85,bg=BaseBackColor,bd=0)
weather.MaxTemp(maxtemp,80,BaseBackColor)
maxtemp.place(x=1560,y=745)

lowtemp= tk.LabelFrame(root,width=360, height=85,bg=BaseBackColor,bd=0)
weather.LowTemp(lowtemp,80,BaseBackColor)
lowtemp.place(x=1560,y=855)

humidity= tk.LabelFrame(root,width=360, height=85,bg=BaseBackColor,bd=0)
weather.humidity(humidity,80,BaseBackColor)
humidity.place(x=1560,y=960)

RoTemp= tk.LabelFrame(root,width=400, height=100,bg=BaseBackColor,bd=0)
room.Temp(RoTemp,90,BaseBackColor)
RoTemp.place(x=150,y=810)

RoHum= tk.LabelFrame(root,width=400, height=100,bg=BaseBackColor,bd=0)
room.Hum(RoHum,90,BaseBackColor)
RoHum.place(x=150,y=930)


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