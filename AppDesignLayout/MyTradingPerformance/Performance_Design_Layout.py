from tkinter import *

class initiate:
    def __init__(self, root):

        def startButtonAction():
            if startButton["state"] == "normal" and endButton["state"] == "disabled":
                startButton["state"] = "disabled"
                endButton["state"] = "normal"
        def ending():
            if startButton["state"] == "disabled" and endButton["state"] == "normal":
                startButton["state"] = "normal"
                endButton["state"] = "disabled"

        #Performance Gadget Layout
        performanceMainFrame = Frame(root, bg="blue", width=480, height=270)
        performanceMainFrame.grid(row=0,column=0, columnspan=1)
        performanceMainFrame.grid_propagate(True)

        #Performance Frame, That changes color base on performance
        performanceSecondaryFrame = Frame(performanceMainFrame, bg="red", width=460, height=200)
        performanceSecondaryFrame.grid(row=0, column=0, padx=10, pady=10)
        performanceSecondaryFrame.grid_propagate(True)

        #Frames For Buttons
        performanceTertiaryFrame_1 = Frame(performanceMainFrame,bg="green", width=100, height=25)
        performanceTertiaryFrame_1.grid(row=1, column=0, padx=(0,100), pady=(5,13))
        performanceTertiaryFrame_1.grid_propagate(True)

        performanceTertiaryFrame_2 = Frame(performanceMainFrame, bg="red", width=100, height=25)
        performanceTertiaryFrame_2.grid(row=1, column=0, padx=(50,0), pady=(5,13))
        performanceTertiaryFrame_2.grid_propagate(True)

        #Performance Input Buttons
        startButton = Button(performanceTertiaryFrame_1, text="START!", padx=5)
        startButton.grid(row=0, column=0, padx=(0, 0))

        endButton = Button(performanceTertiaryFrame_2, text="END!", state=DISABLED, padx=10)
        endButton.grid(row=0, column=0, padx=(0,0))
