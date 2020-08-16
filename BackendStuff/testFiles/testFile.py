def addToDatabase(startTime, listPosition, colorNumber):
    # if pressButtonSession:
    sessionStatus = True

    while sessionStatus:
        scanTextImg = scn.desktop_Screenshot(listPosition[0], listPosition[1], listPosition[2], listPosition[3], 3, 3)
        retrieveTradeList = scn.retrieveText(scanTextImg, 7)

        if checkIfAlreadyInDatabase(retrieveTradeList, startTime):
            printTimeInAscendingOrder(obtainDatabaseTableName())
            sessionStatus = False
            break
        else:
            add_Table_To_Database(retrieveTradeList, obtainDatabaseTableName())
            listPosition[1] = listPosition[1] + 23
            listPosition[3] = listPosition[3] + 23

            return listPosition[1], listPosition[3]

#This should be stored where buy function is at
