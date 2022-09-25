import datetime
import calendar
import tkinter

 
### 定数
WEEK = ["日", "月", "火", "水", "木", "金", "土"]
 
### 現在年月取得
year  = datetime.date.today().year
month = datetime.date.today().month
Day   = datetime.date.today().day
 
### 関数
def calender(master,size,basecolor):

    frame1 = tkinter.Frame(master=master,bg=basecolor)
    frame2 = tkinter.Frame(master=master,bg=basecolor)
    fontsize = size
 
    ### グローバル変数定義
    global year
    global month

    ### ラベルウィジェットを初期化
    for widget in frame1.winfo_children():
        if isinstance(widget, tkinter.Label):
            widget.destroy()
 
    ### ラベルに年月を設定
    label = tkinter.Label(master=frame1, text=str(year) + "年" + str(month) + "月",  font=("游ゴシック",int(size*0.8)),fg="white",bg=basecolor)
 
    ### 年月表示
    label.pack()
 
    ### カレンダーオブジェクト作成
    cl = calendar.Calendar(firstweekday=6)
 
    ### 該当年月のカレンダーを取得
    cal = cl.monthdayscalendar(year, month)
 
    ### ウィジェット初期化
    for widget in frame2.winfo_children():
        widget.destroy()
 
    ### 曜日配列を取得
    for i,x in enumerate(WEEK):
 
        ### 日曜日は赤、土曜日は青にする
        if   i == 0:
            Dfg = "red"
        elif i == 6:
            Dfg = "blue"
        else:
            Dfg = "white"
        
        label_day = tkinter.Label(master=frame2, text=x, font=("游ゴシック",fontsize), width=3, fg=Dfg,bg=basecolor)
 
        ### 曜日を表示
        label_day.grid(row=0, column=i, pady=2)
 
    ### 行カウンター
    row_cnt = 1
 
    ### カレンダー配列を取得
    for week in cal:
        for i,day in enumerate(week):
 
            ### 0だったら空白を設定
            if day == 0:
                day = " "
        
            DDay = "{:>2}".format(day)
 
            ### 日曜日は赤、土曜日は青にする
            if DDay == str(Day):
                fg = "white"
                bg = "red"
            elif   i == 0:
                fg = "red"
                bg = basecolor
            elif i == 6:
                fg = "blue"
                bg = basecolor
            else:
                fg = "white"
                bg = basecolor

            label_day = tkinter.Label(master=frame2, text="{:>2}".format(day), font=("游ゴシック",fontsize), height=1,fg=fg,bg=bg)


 
            ### 日にちを表示
            label_day.grid(row=row_cnt, column=i, padx=2, pady=2)
 
        ### カウントアップ
        row_cnt = row_cnt + 1
    

    frame1.pack(pady=20, side="top")
    frame2.pack()
 
