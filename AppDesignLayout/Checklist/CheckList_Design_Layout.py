from tkinter import *

class initiate:
    def __init__(self, root):
        # Checklist Gadget Layout
        checkListMainFrame = Frame(root, bg="blue", width=480, height=270)
        checkListMainFrame.grid(row=1, column=1, columnspan=1, padx=(75, 0))
        checkListMainFrame.grid_propagate(False)

        # Secondary Frame Inside CheckList Frame
        checkListSecondaryFrame = Frame(checkListMainFrame, bg="red", width=460, height=200)
        checkListSecondaryFrame.grid(row=0, column=0, padx=10, pady=10)
        checkListSecondaryFrame.grid_propagate(False)

        #Tertiary Frame For Checklist_1
        checkListTertiaryFrame_1 = Frame(checkListSecondaryFrame, bg="blue", width=100, height=30)
        checkListTertiaryFrame_1.grid(row=0, column=0)
        checkListTertiaryFrame_1.grid_propagate(True)

        # Tertiary Frame For Checklist_2
        checkListTertiaryFrame_2 = Frame(checkListSecondaryFrame, bg="blue", width=100, height=30)
        checkListTertiaryFrame_2.grid(row=1, column=0)
        checkListTertiaryFrame_2.grid_propagate(True)

        # Tertiary Frame For Checklist_3
        checkListTertiaryFrame_3 = Frame(checkListSecondaryFrame, bg="blue", width=100, height=30)
        checkListTertiaryFrame_3.grid(row=2, column=0)
        checkListTertiaryFrame_3.grid_propagate(True)

        # Tertiary Frame For Checklist_4
        checkListTertiaryFrame_4 = Frame(checkListSecondaryFrame, bg="blue", width=100, height=30)
        checkListTertiaryFrame_4.grid(row=3, column=0)
        checkListTertiaryFrame_4.grid_propagate(True)



        #Tertiary Frame
        saveCheckListButtonFrame_1 = Frame(checkListSecondaryFrame, bg="green", width=100, height=25)
        saveCheckListButtonFrame_1.grid(row=4, column=0, padx=(0, 100), pady=(10, 10))
        saveCheckListButtonFrame_1.grid_propagate(True)

        clearCheckListButtonFrame_2 = Frame(checkListSecondaryFrame, bg="yellow", width=100, height=25)
        clearCheckListButtonFrame_2.grid(row=4, column=0, padx=(50, 0), pady=(10, 10))
        clearCheckListButtonFrame_2.grid_propagate(True)

        # Performance Input Buttons  #######################################################################################
        saveCheckListButton = Button(saveCheckListButtonFrame_1, text="SUCCESS!", padx=5)  #############################################
        saveCheckListButton.grid(row=0, column=0, padx=(0, 0))

        clearCheckListButton = Button(clearCheckListButtonFrame_2, text="FAIL!", padx=10)  ###################################################
        clearCheckListButton.grid(row=0, column=0, padx=(0, 0))























        #Checkbox #1
        checkBox_1 = StringVar() #This obtains the response on whether the checkbox has been click on or not

        checkButton_1 = Checkbutton(checkListTertiaryFrame_1, variable=checkBox_1, onvalue="SuperSize", offvalue="RegularSize")    #Onvalue and offvalue can be set to your custom needs
        checkButton_1.deselect()
        checkButton_1.grid(row=0,column=0)

        entryBox_1 = Entry(checkListTertiaryFrame_1, bd=3, width=20, font=('Helvetica', 13))
        entryBox_1.grid(row=0, column=0, pady=0, padx=0)
        entryBox_1.grid(row=0, column=1)

        myButton_1 = Button(checkListTertiaryFrame_1, text="Show Selection")
        myButton_1.grid(row=0, column=2)




        #Checkbox #2
        checkBox_2 = StringVar() #This obtains the response on whether the checkbox has been click on or not

        checkButton_2 = Checkbutton(checkListTertiaryFrame_2, variable=checkBox_2, onvalue="SuperSize", offvalue="RegularSize")    #Onvalue and offvalue can be set to your custom needs
        checkButton_2.deselect()
        checkButton_2.grid(row=0,column=0)

        entryBox_2 = Entry(checkListTertiaryFrame_2, bd=3, width=20, font=('Helvetica', 13))
        entryBox_2.grid(row=0, column=0, pady=0, padx=0)
        entryBox_2.grid(row=0, column=1)

        myButton_2 = Button(checkListTertiaryFrame_2, text="Show Selection")
        myButton_2.grid(row=0, column=2)





        #Checkbox #3
        checkBox_3 = StringVar() #This obtains the response on whether the checkbox has been click on or not

        checkButton_3 = Checkbutton(checkListTertiaryFrame_3, variable=checkBox_3, onvalue="SuperSize", offvalue="RegularSize")    #Onvalue and offvalue can be set to your custom needs
        checkButton_3.deselect()
        checkButton_3.grid(row=0,column=0)

        entryBox_3 = Entry(checkListTertiaryFrame_3, bd=3, width=20, font=('Helvetica', 13))
        entryBox_3.grid(row=0, column=0, pady=0, padx=0)
        entryBox_3.grid(row=0, column=1)

        myButton_3 = Button(checkListTertiaryFrame_3, text="Show Selection")
        myButton_3.grid(row=0, column=2)



        #Checkbox #4
        checkBox_4 = StringVar() #This obtains the response on whether the checkbox has been click on or not

        checkButton_4 = Checkbutton(checkListTertiaryFrame_4, variable=checkBox_4, onvalue="SuperSize", offvalue="RegularSize")    #Onvalue and offvalue can be set to your custom needs
        checkButton_4.deselect()
        checkButton_4.grid(row=0,column=0)

        entryBox_4 = Entry(checkListTertiaryFrame_4, bd=3, width=20, font=('Helvetica', 13))
        entryBox_4.grid(row=0, column=0, pady=0, padx=0)
        entryBox_4.grid(row=0, column=1)

        myButton_4 = Button(checkListTertiaryFrame_4, text="Show Selection")
        myButton_4.grid(row=0, column=2)