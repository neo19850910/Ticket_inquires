#coding:utf8
'''
    auth:neo
    date:2017/9/1
'''
import sys
from Tkinter import *
import time
import tkMessageBox
import xml.etree.ElementTree as etree
import urllib

reload(sys)
sys.setdefaultencoding('utf8')


def trickit():
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    Label1.config(text=currentTime)
    root.update()
    Label1.after(1000, trickit)

def func():
    top = Toplevel(root)
    label = Label(top, text = 'receiver\'s name')
    label.pack()
    entry1 = Entry(top)
    entry1.pack()

def inqueres():
    a = come_city_value.get().encode('utf8')
    b = go_city_value.get().encode('utf8')
    data = gotime_value.get().encode('utf8')
    mudi=a+'-'+b
    context = urllib.urlopen('http://ws.qunar.com/holidayService.jcp?lane=%s' % mudi)
    tree = etree.parse(context)
    root = tree.getroot()
    for node in root[0]:
        if node.attrib["date"] == data:
            for child in node:
                for child_detail in child.attrib.keys():
                    # print child_detail
                    if child.attrib["type"] == "go" and int(child.attrib["price"])!=0:
                        tkMessageBox.showinfo("－－以下查询结果只包含当天直飞最低价格,不包含中转价格－－",
                        message= "机票查询时间:%s\r机票旅行地点:%s\r飞机票折扣:%s\r飞机票价格:%s元\r航班公司名称:%s\r起飞时间:%s\r降落时间:%s\r" % (node.attrib["date"],mudi,child.attrib["discount"],int(child.attrib["price"]),child.attrib["name"],node.attrib["go_start"],node.attrib["go_expires"]))
                        break

if __name__ == '__main__':
    root = Tk()
    root .title("机票查询")
    root.geometry("800x400")
    root.resizable(width=False, height=False)
    l = Label(root,text='特价机票查询系统', fg='red', font=('Arial', 15), width=20, height=3)
    l.pack(side=TOP)
    come_city = Label(root,text='出发城市:', width=10, height=3)
    come_city.pack(side=LEFT)
    come_city_value = StringVar()
    e = Entry(root, textvariable=come_city_value)
    e.pack(side=LEFT)
    go_city = Label(root, text='到达城市:', width=10, height=3)
    go_city.pack(side=LEFT)
    go_city_value = StringVar()
    g = Entry(root, textvariable=go_city_value)
    g.pack(side=LEFT)
    gotime = Label(root,text='出发时间:')
    gotime.pack(side=LEFT)
    gotime_value = StringVar()
    v = Entry(root, textvariable=gotime_value)
    v.pack(side=LEFT)
    Button(root, text='点击查询', command=inqueres).pack(side=LEFT)

    Label1=Label(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    Label1.pack()

    Label1.after(1000, trickit)
    root.mainloop()
