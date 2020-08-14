from pynput.keyboard import Listener
from threading import Thread
import time
from BackendStuff.Database import Import_Tradelog_Data_To_Database

# Variables that hold number of presses
global total_Times_Buy_Button_Pressed
total_Times_Buy_Button_Pressed = 0
global total_Times_Sell_Button_Pressed
total_Times_Sell_Button_Pressed = 0

#Variable that will be used to perform a function a given number of times
global remaining_Buy_Button_Press_Count
remaining_Buy_Button_Press_Count = 0
global remaining_Sell_Button_Press_Count
remaining_Sell_Button_Press_Count = 0

class initiate:
    def __init__(self): #, root):
        def launch_keyboard_listener():
                # Keyboard Listener Store Variable
                global keyboard_listener

                # Keyboard Listener Functions
                def kb_listener_press_function(key):
                    #Obtain the key that was pressed and stored in variable
                    hotKeyPressed = str(key)

                    # Everytime, F4 is pressed
                        # We will keep count in total_Times_Buy_Button_Pressed variable
                    if (hotKeyPressed == "Key.f4"):
                        global total_Times_Buy_Button_Pressed
                        total_Times_Buy_Button_Pressed = total_Times_Buy_Button_Pressed + 1

                    # Everytime, F5 is pressed
                        # We will keep count in total_Times_Buy_Button_Pressed variable
                    elif (hotKeyPressed == "Key.f5"):
                        global total_Times_Sell_Button_Pressed
                        total_Times_Sell_Button_Pressed = total_Times_Sell_Button_Pressed + 1

                #Will Perform Following Function when activated
                keyboard_listener = Listener(on_press=kb_listener_press_function)
                #Will Initiate Keyboard Listener
                keyboard_listener.start()
                keyboard_listener.join()
        keyboard_listener = Thread(target=launch_keyboard_listener)
        keyboard_listener.start()

        def getBuyButtonPressCount():
            global total_Times_Buy_Button_Pressed
            return total_Times_Buy_Button_Pressed

        def getSellButtonPressCount():
            global total_Times_Sell_Button_Pressed
            return total_Times_Sell_Button_Pressed

        def launch_buy_button_action():
            while True:
                # global remaining_Buy_Button_Press_Count
                if getBuyButtonPressCount() != 0:
                    print("Buy Button")
                    buyPressed = Import_Tradelog_Data_To_Database
                    buyPressed.initiate(2)
                    global total_Times_Buy_Button_Pressed
                    # print(total_Times_Buy_Button_Pressed)
                    time.sleep(1)
                    total_Times_Buy_Button_Pressed = getBuyButtonPressCount() -1
                elif getBuyButtonPressCount() < 0:
                    total_Times_Buy_Button_Pressed = 0
                else:
                    time.sleep(2)

        def launch_sell_button_action():
            while True:
                # global remaining_Sell_Button_Press_Count
                # global total_Times_Sell_Button_Pressed
                if getSellButtonPressCount() != 0:

                    sellPressed = Import_Tradelog_Data_To_Database
                    sellPressed.initiate(1)
                    global total_Times_Sell_Button_Pressed
                    # print(total_Times_Sell_Button_Pressed)
                    time.sleep(1)
                    total_Times_Sell_Button_Pressed = getSellButtonPressCount() -1
                elif getSellButtonPressCount() < 0:
                    total_Times_Sell_Button_Pressed = 0
                else:
                    time.sleep(2)

        performBuyButtonAction = Thread(target=launch_buy_button_action)
        performBuyButtonAction.start()

        performSellButtonAction = Thread(target=launch_sell_button_action)
        performSellButtonAction.start()
