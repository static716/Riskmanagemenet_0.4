from threading import Thread

from BackendStuff.Database import Create_Database_Table
from AppDesignLayout import AppDesign
class initiate:
    def __init__(self):
        # Launch Database and Create Today's Table
        Create_Database_Table.initiate()

        #Load Riskmanagement Dashboard
        loadRiskmanagementDashboard = Thread(target=AppDesign.initiate())

        #Load Keyboard Listener
        #loadKeyboardListener = Thread(target=)

