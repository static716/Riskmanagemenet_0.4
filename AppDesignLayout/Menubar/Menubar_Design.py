from tkinter import *

class initiate:
    def __init__(self, root):
        # Main Menu
        my_menu = Menu(root)
        root.config(menu=my_menu)

        # Menu click command
        def our_command(root):
            print("Hello")

        # Create a menu item

        file_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New...", command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # Create an edit menu item
        edit_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Edit", menu=our_command)
        edit_menu.add_command(label="Cut", command=our_command)
        edit_menu.add_command(label="Copy", command=our_command)

        # Create an Options menu item
        option_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Options", menu=option_menu)
        option_menu.add_command(label="Find", command=our_command)
        option_menu.add_command(label="Find Next", command=our_command)