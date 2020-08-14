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
            #First CHeck If Tradelog section is empty or not
            tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
            if tradeLog_Color != 0: #If It isn't empty, perform the following
                scanTextImg = SCN_Tools.desktop_Screenshot(startingCordinates[0], startingCordinates[1],startingCordinates[2], startingCordinates[3], 3, 3) ##
                retrieveTimeList = SCN_Tools.retrieveText(scanTextImg, 1)
                if DB_Tools.compare_Time_Difference(DB_Tools.get_Database_Table_Name(), current_time, retrieveTimeList[0]):
                    if tradeLog_Color == the_Color_IM_Looking_For:
                        retrieveTradeList = SCN_Tools.retrieveText(scanTextImg, 7)##
                        # Check if already exist in database
                        if DB_Tools.check_If_Already_Exist(retrieveTradeList, current_time):
                            startingCordinates[1] = startingCordinates[1] + 23
                            startingCordinates[3] = startingCordinates[3] + 23
                        else:
                            DB_Tools.add_Table_To_Database(retrieveTradeList, DB_Tools.get_Database_Table_Name())
                            startingCordinates[1] = startingCordinates[1] + 23
                            startingCordinates[3] = startingCordinates[3] + 23
                    else:
                        startingCordinates[1] = startingCordinates[1] + 23
                        startingCordinates[3] = startingCordinates[3] + 23
                else:
                    DB_Tools.reorganize_DB_Table_In_Ascend_Order(DB_Tools.get_Database_Table_Name())
                    session = False
                    break
#############################################################################################################
            else:
                pending_Order_Color = SCN_Tools.identify_Tradelog_Color([448, 782, 640, 798], 6, 6)
                if pending_Order_Color == 0 or pending_Order_Color == the_Color_IM_Not_Looking_For:
                    tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
                    if tradeLog_Color == 0 or tradeLog_Color == the_Color_IM_Not_Looking_For: ####
                        DB_Tools.reorganize_DB_Table_In_Ascend_Order(DB_Tools.get_Database_Table_Name())
                        session = False
                        break
                    else:
                        scanTextImg = SCN_Tools.desktop_Screenshot(startingCordinates[0], startingCordinates[1],startingCordinates[2], startingCordinates[3], 3, 3)
                        retrieveTimeList = SCN_Tools.retrieveText(scanTextImg, 1)
                        if DB_Tools.compare_Time_Difference(DB_Tools.get_Database_Table_Name(), current_time,retrieveTimeList[0]):
                            if tradeLog_Color == the_Color_IM_Looking_For:
                                retrieveTradeList = SCN_Tools.retrieveText(scanTextImg, 7)
                                # Check if already exist in database
                                if DB_Tools.check_If_Already_Exist(retrieveTradeList, current_time):
                                    startingCordinates[1] = startingCordinates[1] + 23
                                    startingCordinates[3] = startingCordinates[3] + 23
                                else:
                                    DB_Tools.add_Table_To_Database(retrieveTradeList,DB_Tools.get_Database_Table_Name())
                                    startingCordinates[1] = startingCordinates[1] + 23
                                    startingCordinates[3] = startingCordinates[3] + 23
                            else:
                                startingCordinates[1] = startingCordinates[1] + 23
                                startingCordinates[3] = startingCordinates[3] + 23
                        else:
                            DB_Tools.reorganize_DB_Table_In_Ascend_Order(DB_Tools.get_Database_Table_Name())
                            session = False
                            break
#############################################################################################################
                else:
                    pending_Order_Color = SCN_Tools.identify_Tradelog_Color([448, 782, 640, 798], 6, 6)
                    if pending_Order_Color == 0:  # Then we will wait until it no longer exist and then check trade log again
                        tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
                        if tradeLog_Color == 0 or tradeLog_Color == the_Color_IM_Not_Looking_For:  ####
                            DB_Tools.reorganize_DB_Table_In_Ascend_Order(DB_Tools.get_Database_Table_Name())
                            session = False
                            break
                        else:
                            scanTextImg = SCN_Tools.desktop_Screenshot(startingCordinates[0], startingCordinates[1],startingCordinates[2], startingCordinates[3], 3, 3)
                            retrieveTimeList = SCN_Tools.retrieveText(scanTextImg, 1)
                            if DB_Tools.compare_Time_Difference(DB_Tools.get_Database_Table_Name(), current_time,retrieveTimeList[0]):
                                tradeLog_Color = SCN_Tools.identify_Tradelog_Color(startingCordinates, 6, 6)
                                if tradeLog_Color == the_Color_IM_Looking_For:
                                    scanTextImg = SCN_Tools.desktop_Screenshot(startingCordinates[0], startingCordinates[1],startingCordinates[2], startingCordinates[3], 3,3)
                                    retrieveTradeList = SCN_Tools.retrieveText(scanTextImg, 7)
                                    if DB_Tools.check_If_Already_Exist(retrieveTradeList, current_time):
                                        startingCordinates[1] = startingCordinates[1] + 23
                                        startingCordinates[3] = startingCordinates[3] + 23
                                    else:
                                        DB_Tools.add_Table_To_Database(retrieveTradeList, DB_Tools.get_Database_Table_Name())
                                        startingCordinates[1] = startingCordinates[1] + 23
                                        startingCordinates[3] = startingCordinates[3] + 23
                                else:
                                    startingCordinates[1] = startingCordinates[1] + 23
                                    startingCordinates[3] = startingCordinates[3] + 23
                            else:
                                DB_Tools.reorganize_DB_Table_In_Ascend_Order(DB_Tools.get_Database_Table_Name())
                                session = False
                                break
                #Check Other areas before deciding to end program