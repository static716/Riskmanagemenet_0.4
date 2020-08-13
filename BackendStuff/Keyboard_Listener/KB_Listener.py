from pynput.keyboard import Listener
from threading import Thread
import time

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
                    print(hotKeyPressed)
                    # Everytime, F4 is pressed
                        # We will keep count in total_Times_Buy_Button_Pressed variable
                        # remaining_Buy_Button_Press_Count purpose is to keep track of how many times a process should be performed
                    if (hotKeyPressed == "Key.f4"):
                        print("f4")
                        global total_Times_Buy_Button_Pressed
                        # global remaining_Buy_Button_Press_Count
                        total_Times_Buy_Button_Pressed = total_Times_Buy_Button_Pressed + 1
                        # remaining_Buy_Button_Press_Count = total_Times_Buy_Button_Pressed

                    # Everytime, F5 is pressed
                        # We will keep count in total_Times_Buy_Button_Pressed variable
                        # remaining_Sell_Button_Press_Count purpose is to keep track of how many times a process should be performed
                    elif (hotKeyPressed == "Key.f5"):
                        global total_Times_Sell_Button_Pressed
                        # global remaining_Sell_Button_Press_Count
                        total_Times_Sell_Button_Pressed = total_Times_Sell_Button_Pressed + 1
                        # remaining_Sell_Button_Press_Count = total_Times_Sell_Button_Pressed

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
                global total_Times_Buy_Button_Pressed

                if getBuyButtonPressCount() != 0:
                    print("hello")
                    total_Times_Buy_Button_Pressed = getBuyButtonPressCount() -1
                else:
                    time.sleep(2)
                # if remaining_Buy_Button_Press_Count == 0 or remaining_Buy_Button_Press_Count >= 1:
                #     time.sleep(2)
                #     for i in range(remaining_Buy_Button_Press_Count):
                #         print("buyButtonPressed")
                #         # testing.pressBuyButton()
                #
                #         remaining_Buy_Button_Press_Count = remaining_Buy_Button_Press_Count - 1
                #     if remaining_Buy_Button_Press_Count == 0:
                #         total_Times_Sell_Button_Pressed = 0
                # else:
                #     time.sleep(2)

        def launch_sell_button_action():
            while True:
                # global remaining_Sell_Button_Press_Count
                global total_Times_Sell_Button_Pressed
                if getSellButtonPressCount() != 0:
                    print("Sell Button Function")
                    total_Times_Sell_Button_Pressed = getSellButtonPressCount() -1
                else:
                    time.sleep(2)


#                 if remaining_Sell_Button_Press_Count == 0 or remaining_Sell_Button_Press_Count >= 1:
#                     time.sleep(2)
#                     for i in range(remaining_Sell_Button_Press_Count):
#                         print("sellButtonPressed")
#
# #                        print("Current Value: " + str(total_Sell_Button_Presses))
#
#                         remaining_Sell_Button_Press_Count = remaining_Sell_Button_Press_Count - 1
#                     if remaining_Sell_Button_Press_Count == 0:
#                         total_Times_Sell_Button_Pressed = 0
#                 else:
#                     time.sleep(2)



        performBuyButtonAction = Thread(target=launch_buy_button_action)
        performBuyButtonAction.start()

        performSellButtonAction = Thread(target=launch_sell_button_action)
        performSellButtonAction.start()

initiate()