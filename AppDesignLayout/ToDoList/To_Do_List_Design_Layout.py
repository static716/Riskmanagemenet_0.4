from tkinter import *

class initiate:
    def __init__(self, root):
        # To Do List Gadget
        toDoListMainFrame = Frame(root, bg="blue", width=480, height=270)
        toDoListMainFrame.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(25, 0))
        toDoListMainFrame.grid_propagate(True)

        #Secondar Frame Inside Main To Do List Frame
        toDoListSecondaryFrame = Frame(toDoListMainFrame, bg="red", width=460, height=200)
        toDoListSecondaryFrame.grid(row=0, column=0, padx=10, pady=10)
        toDoListSecondaryFrame.grid_propagate(True)

        # To Do List Frame AND Scrollbar
        toDoList_Scrollbar = Scrollbar(toDoListSecondaryFrame, orient=VERTICAL)
        toDoListGadget = Listbox(toDoListSecondaryFrame, background="blue", width=71, height=15, selectmode=MULTIPLE, yscrollcommand=toDoList_Scrollbar.set)
        toDoList_Scrollbar.config(command=toDoListGadget.yview)
        toDoListGadget.grid(row=0,column=0, columnspan =1)
        toDoList_Scrollbar.grid(row=0,column=0, padx=(444,0),sticky=N+S)

        # Add item to listbox
        toDoListGadget.insert(END, "This is an item")
        toDoListGadget.insert(END, "Second Item!")
        





        #Entry Frame AND Submit Button Frame
        #Entry Frame
        entryFrameBox = Frame(toDoListSecondaryFrame, bg="green", width=100, height=25)
        entryFrameBox.grid(row=1, column=0, padx=(0,100), pady=(10,10))
        entryFrameBox.grid_propagate(True)

        #Entry Box
        entryBox = Entry(entryFrameBox, bd=3, width=20, font=('Helvetica', 13))
        entryBox.grid(row = 0, column=0, pady=0, padx=0)



        #Submit Button Frame
        submitButtonFrame = Frame(toDoListSecondaryFrame, bg="yellow", width=100, height=25)
        submitButtonFrame.grid(row=1, column=0, padx=(204, 0), pady=(10, 10))
        submitButtonFrame.grid_propagate(True)

        #Submit Button Gadget
        submitButton = Button(submitButtonFrame, text="Submit", padx=10, pady=2)  ###################################################
        submitButton.grid(row=0, column=0, padx=(0, 0))













        #To Do List Button Frames
        toDoListButtonFrame_1 = Frame(toDoListSecondaryFrame, bg="green", width=100, height=25)
        toDoListButtonFrame_1.grid(row=2, column=0, padx=(0,100), pady=(10,10))
        toDoListButtonFrame_1.grid_propagate(True)

        toDoListButtonFrame_2 = Frame(toDoListSecondaryFrame, bg="yellow", width=100, height=25)
        toDoListButtonFrame_2.grid(row=2, column=0, padx=(50, 0), pady=(10, 10))
        toDoListButtonFrame_2.grid_propagate(True)

        #Performance Input Buttons  #######################################################################################
        successButton = Button(toDoListButtonFrame_1, text="SUCCESS!", padx=5) #############################################
        successButton.grid(row=0, column=0, padx=(0, 0))

        failButton = Button(toDoListButtonFrame_2, text="FAIL!", padx=10)###################################################
        failButton.grid(row=0, column=0, padx=(0,0))

