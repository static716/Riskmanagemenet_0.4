#This should be implemented elsewhere

def examineDataORAddToDatabase(startingCordinates, startTime, asignedColor):
    session = True

    while session:
        imgTradeLogColor = screenShot(startingCordinates[0], startingCordinates[1], startingCordinates[2], startingCordinates[3], 6, 6)
        imgTradeLogColor = cv2.cvtColor(imgTradeLogColor, cv2.COLOR_BGR2RGB)

        tradeLogColorIdentifier = findColor(imgTradeLogColor, tradeLogColors)

        if len(tradeLogColorIdentifier) != 0:
            scanTextImg = screenShot(startingCordinates[0], startingCordinates[1], startingCordinates[2], startingCordinates[3], 3, 3)
            retrieveTimeList = retrieveText(scanTextImg, 1)

            if timeDifference(dbFunction.obtainDatabaseTableName(), startTime, retrieveTimeList[0]):
                imgTradeLogColor = screenShot(startingCordinates[0], startingCordinates[1], startingCordinates[2],startingCordinates[3], 6, 6)
                imgTradeLogColor = cv2.cvtColor(imgTradeLogColor, cv2.COLOR_BGR2RGB)
                tradeLogColorIdentifier = findColor(imgTradeLogColor, tradeLogColors)
                if len(tradeLogColorIdentifier) == asignedColor:
                    x11, y11 = dbFunction.obtain_Info_Then_Upload_To_Database(startTime, startingCordinates, asignedColor)
                    startingCordinates[1] = x11
                    startingCordinates[3] = y11
                else:
                    startingCordinates[1] = startingCordinates[1] + 23
                    startingCordinates[3] = startingCordinates[3] + 23
            else:
                session = False
        else:
            session = False