from tkinter import *
class DisplayPatternFrame:
    def __init__(self,root):
        #Display Pattern Images That I Look For Gadget
        displayPatternImagesMainFrame = Frame(root,bg="blue", width=480, height=270)
        displayPatternImagesMainFrame.grid(row=0,column=1,columnspan=1,padx=(75,0))
        displayPatternImagesMainFrame.grid_propagate(True)

        #Image Frame:1 Inside Main Image Frame
        imageFrame_1 = Frame(displayPatternImagesMainFrame, bg="red", width=220, height=117)
        imageFrame_1.grid(row=0, column=0, padx=(15,10), pady=(10,10))
        imageFrame_1.grid_propagate(True)

        #Image Frame:2 Inside Main Image Frame
        imageFrame_2 = Frame(displayPatternImagesMainFrame, bg="red", width=220, height=117)
        imageFrame_2.grid(row=0, column=1, padx=(0,10), pady=(10,10))
        imageFrame_2.grid_propagate(True)

        #Image Frame:3 Inside Main Image Frame
        imageFrame_3 = Frame(displayPatternImagesMainFrame, bg="red", width=220, height=117)
        imageFrame_3.grid(row=1, column=0, padx=(15,10), pady=(0,10))
        imageFrame_3.grid_propagate(True)

        #Image Frame:4 Inside Main Image Frame
        imageFrame_4 = Frame(displayPatternImagesMainFrame, bg="red", width=220, height=117)
        imageFrame_4.grid(row=1, column=1, padx=(0,10), pady=(0,10))
        imageFrame_4.grid_propagate(True)