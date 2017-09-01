#coding:utf8
'''
    auth:neo
    date:2017/9/1
'''
import sys
from Tkinter import *
import time
reload(sys)
sys.setdefaultencoding('utf8')

def rtnkey(event=None):
    return e.get()
def result():
    print ("此为查询数据结果展示接口")
root = Tk() #初始化
root .title("机票查询")
root.geometry("800x400") #设置窗口大小
root.resizable(width=False, height=False) #设置窗口大小可变否
l = Label(root,text='特价机票查询系统',bg='pink', font=('Arial', 15),width=20, height=3)
l.pack(side=TOP)
come_city = Label(root,text='出发城市:',width=10,height=3)
come_city.pack(side=LEFT)
come_city_value = Variable()
e = Entry(root, textvariable=come_city_value,relief='groove')
e.pack(side=LEFT)
e.bind('<Return>', rtnkey)
go_city = Label(root,text='到达城市:',width=10,height=3)
go_city.pack(side=LEFT)
go_city_value = Variable()
g = Entry(root, textvariable=go_city_value,relief='groove')
g.pack(side=LEFT)
e.bind('<Return>',rtnkey)
gotime = Label(root,text='出发时间:')
gotime.pack(side=LEFT)
gotime_value = Variable()
v = Entry(root, textvariable=gotime_value,relief='groove')
v.pack(side=LEFT)
v.bind('<Return>', rtnkey)
Button(root, text='点击查询', command=result).pack(side=BOTTOM)
Label1=Label(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
Label1.pack()
def trickit():
    currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    Label1.config(text=currentTime)
    root.update()
    Label1.after(1000, trickit)
Label1.after(1000, trickit)
root.mainloop()
