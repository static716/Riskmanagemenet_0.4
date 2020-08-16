from tkinter import *
from AppDesignLayout.Menubar import Menubar_Design
from AppDesignLayout.MyTradingPerformance import Performance_Design_Layout
from AppDesignLayout.ChartPatterns import Chart_Pattern_Design_Layout
from AppDesignLayout.ToDoList import To_Do_List_Design_Layout
from AppDesignLayout.Checklist import CheckList_Design_Layout

def initiate():
    root = Tk()

    #Window Name
    root.title("Risk Management")

    #Window Size
    root.geometry("1920x1080+1912+10")

    Menubar_Design.initiate(root)
    Performance_Design_Layout.initiate(root)
    Chart_Pattern_Design_Layout.initiate(root)
    To_Do_List_Design_Layout.initiate(root)
    CheckList_Design_Layout.initiate(root)

    root.mainloop()