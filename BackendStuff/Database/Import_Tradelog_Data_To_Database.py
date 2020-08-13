from BackendStuff.Database import Database_Tools as DB_Tools
from BackendStuff.Scanning import Scanning_Tools as SCN_Tools

class initiate:
    def __init__(self, colorLookingFor):
        startingCordinates = [10, 610, 420, 633]
        current_time = DB_Tools.getCurrentTime()
        the_Color_IM_Looking_For = colorLookingFor

        global the_Color_IM_Not_Looking_For

        if the_Color_IM_Looking_For == 2:
            the_Color_IM_Not_Looking_For = 1
        else:
            the_Color_IM_Not_Looking_For = 2

        session = True
        while session:
            #We scan tradelog and try to identify color
            tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
            #If there is previous data, then we try to find out what type of data it is
            if tradeLog_Color != 0:
                #If it is the color that coordinates with out function, then we perform the add_to_database function
                if tradeLog_Color == the_Color_IM_Looking_For:

                    print("Perform Add")

                    session = False
                    break

                #If color is not what we are looking for
                else:
                    #Then we will look at the pending order section cuz the order might be pending
                    pending_Order_Color = SCN_Tools.identify_Tradelog_Color([448, 782, 640, 798], 6, 6)
                    if pending_Order_Color == 0 or pending_Order_Color == the_Color_IM_Not_Looking_For: #If the color is not there then we will scan and check trade log
                        tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
                        if tradeLog_Color == 0 or tradeLog_Color == the_Color_IM_Not_Looking_For:
                            session = False
                            break
                        else:
                            print("Perform Add")
                            # addToDatabase(current_time, 1)
                            session = False
                            break
                    else:#If it is, then we will wait until the order is no longer pending

                        if pending_Order_Color == 0:
                            tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
                            if tradeLog_Color == the_Color_IM_Looking_For:
                                print("Perform Add")
                                # addToDatabase(current_time, 1)
                                session = False
                                break

                            else:
                                session = False
                                break
            else:#If the tradelog is empty or the color is zero
                pending_Order_Color = SCN_Tools.identify_Tradelog_Color([448, 782, 640, 798], 6, 6) #We will check the order pending section
                if pending_Order_Color == 0 or pending_Order_Color == the_Color_IM_Not_Looking_For: #If it is not there we will then check the trade log section
                    tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
                    if tradeLog_Color == 0 or tradeLog_Color == the_Color_IM_Not_Looking_For:
                        session = False
                        break
                    else:
                        addToDatabase(current_time, 2)
                        session = False
                        break
                else:#If color does exist in pending order

                    pending_Order_Color = SCN_Tools.identify_Tradelog_Color([448, 782, 640, 798], 6, 6)
                    if pending_Order_Color == 0: #Then we will wait until it no longer exist and then check trade log again
                        tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
                        if tradeLog_Color == the_Color_IM_Looking_For:

                            addToDatabase(current_time, 2)

                            session = False
                            break

                        else:
                            session = False
                            break