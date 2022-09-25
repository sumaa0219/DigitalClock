import tkinter as tk
import calender11 as CL
import DigitalClock as DC
import weather
import room

BaseBackColor = "black"

root = tk.Tk()
root.geometry("1265x690")
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
calender.place(x=35,y=15)

time = tk.LabelFrame(root,width=445, height=150,bg=BaseBackColor,bd=0)
DC.Time(time,140,BaseBackColor)
time.place(x=550,y=40)

date = tk.LabelFrame(root,width=330, height=65,bg=BaseBackColor,bd=0)
DC.Date(date,54,BaseBackColor)
date.place(x=670,y=240)

second= tk.LabelFrame(root,width=75, height=60,bg=BaseBackColor,bd=0)
DC.Second(second,64,BaseBackColor)
second.place(x=1100,y=150)

temp= tk.LabelFrame(root,width=350, height=105,bg=BaseBackColor,bd=0)
weather.temp(temp,100,BaseBackColor)
temp.place(x=530,y=465)

place= tk.LabelFrame(root,width=450, height=40,bg=BaseBackColor,bd=0)
weather.place(place,30,BaseBackColor)
place.place(x=515,y=350)

condition= tk.LabelFrame(root,width=260, height=50,bg=BaseBackColor,bd=0)
weather.condition(condition,41,BaseBackColor)
condition.place(x=760,y=400)

maxtemp= tk.LabelFrame(root,width=150, height=40,bg=BaseBackColor,bd=0)
weather.MaxTemp(maxtemp,35,BaseBackColor)
maxtemp.place(x=900,y=460)

lowtemp= tk.LabelFrame(root,width=150, height=40,bg=BaseBackColor,bd=0)
weather.LowTemp(lowtemp,35,BaseBackColor)
lowtemp.place(x=900,y=510)

humidity= tk.LabelFrame(root,width=150, height=40,bg=BaseBackColor,bd=0)
weather.humidity(humidity,35,BaseBackColor)
humidity.place(x=900,y=560)

RoTemp= tk.LabelFrame(root,width=200, height=45,bg=BaseBackColor,bd=0)
room.Temp(RoTemp,43,BaseBackColor)
RoTemp.place(x=105,y=470)

RoHum= tk.LabelFrame(root,width=200, height=45,bg=BaseBackColor,bd=0)
room.Hum(RoHum,43,BaseBackColor)
RoHum.place(x=105,y=530)


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