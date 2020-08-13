import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab, Image
from datetime import *
from Performance.TradeLogSection import DatabaseFunctions as dbFunction

# pytesseract file location
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\bryan\AppData\Local\Tesseract-OCR\tesseract.exe"

global tradeLogColors
tradeLogColors = [[0, 179, 75, 255, 255, 255], [95, 179, 158, 255, 255, 255]]

########################################################################################################################################
                                        #Get Contour is needed for findColor function

#Gets the outline from given image
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True) #Calculates a contour perimeter or a curve length
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) #Approximates a polygonal curve(s) with the specified precision
            x, y, w, h = cv2.boundingRect(approx) #Calculates the up-right bounding rectangle of a point set or non-zero pixels of gray-scale image
    return x + w // 2, y

#Returns the color value from given image if our specified color is found (0 = None, 1 = Red, 2 = Blue).
def findColor(img, myColors): #We have the image, the colors we r looking for, and colors to paint our image
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #We convert our image color
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])    #1.
        upper = np.array(color[3:6])    #2.
        mask = cv2.inRange(imgHSV, lower, upper) #With 1. and 2., we are able to create a mask that detects our color.
        x, y = getContours(mask)    #We are detecting our shape and in return getting the position of our shape
        if x != 0 and y != 0:
            newPoints.append([x, y, count]) #This will store where a circle had been created on our image
        count += 1
    return newPoints #This will update our newpoints array
########################################################################################################################################






#Returns a list of text scanned at specified image location
def retrieveText(img, itemsScanning):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = pytesseract.image_to_data(gray, lang='eng', config='-c tessedit_char_blacklist=()|/\`!@#$%^&*-+{}[];><,?_{,=~')
    boxes = boxes.splitlines()
    count = 0
    list = []
    for a, b in enumerate(boxes):
        # b = boxes[a].splitlines()  # This Is The Row # This converts it into rows but the data is stored in one column ########Also by changing the index, we change the row that we are looking at
        # b = b[0].split()  # This converts the one column into multiple columns
        if a != 0:
            b = b.split()
            if len(b) == 12:
                if len(list) < itemsScanning:
                    list.append(b[11])
                    if len(list) == 4:
                        if list[3].rfind(".") == 4:
                            hello = list[3].split()
                            list[3] = str(hello[0][0]) + str(hello[0][1])+ str(hello[0][2])+ str(hello[0][3])

                    if len(list) == 3:
                        if list[2].rfind("s") == 1:
                            hello = list[2].split()
                            list[2] = str(hello[0][0])

                    if len(list) == 7:
                        if list[6].rfind(":") == 0:
                            # hello = list[6].split()
                            list[6] = list[6].replace(":", "-")
                            # list[6] = "-" + str(hello[0][1]) + str(hello[0][2])+ str(hello[0][3])+ str(hello[0][4])+ str(hello[0][5])

                    if len(list) == itemsScanning:
                        return list
#########################################################################################################
                                #Useful Functions






# Returns the current time
def getCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = "01:00:00"
    return current_time








# Returns a Screen Shot of specified Desktop Location
def screenShot(x1,y1,x2,y2, resizeX, resizeY):
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    img = np.array(img)
    img = cv2.resize(img, None, fx=resizeX, fy=resizeY)
    return img






def timeDifference(databaseTime, startTime, timeList):

    databaseTime = databaseTime.split()
    startTime = startTime.split()
    timeList = timeList.split()

    database_Year = str(databaseTime[0][1]) + str(databaseTime[0][2]) + str(databaseTime[0][3]) + str(databaseTime[0][4])
    database_Month = str(databaseTime[0][5]) + str(databaseTime[0][6])
    database_Day = str(databaseTime[0][7]) + str(databaseTime[0][8])

    startTimeHour = str(startTime[0][0]) + str(startTime[0][1])
    startTimeMinute = str(startTime[0][3]) + str(startTime[0][4])
    startTimeSecond = str(startTime[0][6]) + str(startTime[0][7])

    timeListHour = str(timeList[0][0]) + str(timeList[0][1])
    timeListMinute = str(timeList[0][3]) + str(timeList[0][4])
    timeListSecond = str(timeList[0][6]) + str(timeList[0][7])

    startTime1 = datetime(int(database_Year), int(database_Month), int(database_Day), int(startTimeHour), int(startTimeMinute), int(startTimeSecond))
    timeList1 = datetime(int(database_Year), int(database_Month), int(database_Day), int(timeListHour), int(timeListMinute), int(timeListSecond))

    if timeList1 >= startTime1:
        return True
    else:
        return False










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
                    x11, y11 = dbFunction.addToDatabase(startTime, startingCordinates, asignedColor)
                    startingCordinates[1] = x11
                    startingCordinates[3] = y11
                else:
                    startingCordinates[1] = startingCordinates[1] + 23
                    startingCordinates[3] = startingCordinates[3] + 23
            else:
                session = False
        else:
            session = False