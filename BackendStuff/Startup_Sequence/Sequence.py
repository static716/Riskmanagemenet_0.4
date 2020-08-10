from BackendStuff.Database import Create_Database_Table

class initiate:
    def __init__(self):
        # Launch Database and Create Today's Table
        Create_Database_Table.initiate()

        # Use Mouse and Keyboard to load Trading Layout
