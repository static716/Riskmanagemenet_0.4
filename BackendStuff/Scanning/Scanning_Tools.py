import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab

# pytesseract file location
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\bryan\AppData\Local\Tesseract-OCR\tesseract.exe"

# Returns a Screen Shot of specified Desktop Location
def desktop_Screenshot(x1, y1, x2, y2, resizeX, resizeY):
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    img = np.array(img)
    img = cv2.resize(img, None, fx=resizeX, fy=resizeY)
    return img

#########################################################################################################
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
def findColor(img): #We have the image, the colors we r looking for, and colors to paint our image
    myColors = [[0, 179, 75, 255, 255, 255], [95, 179, 158, 255, 255, 255]]
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
#########################################################################################################
#Returns a list of text scanned at specified image location
def retrieveText(img, itemsScanning):
    givenImage = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
                        hello = list[6].split()
                        print(hello)
                        print("Second Version")

                        if hello[0][0].rfind(".") == 0:
                            createNewString = ""
                            for x in range(len(hello[0])):
                                if x == 0:
                                    createNewString = createNewString + "-"
                                    x += 1
                                else:
                                    createNewString = createNewString + str(hello[0][x])
                            list[6] = createNewString
                        elif list[6].rfind(":") == 0:
                            hello = list[6].split()
                            list[6] = list[6].replace(":", "-")
                            # list[6] = "-" + str(hello[0][1]) + str(hello[0][2])+ str(hello[0][3])+ str(hello[0][4])+ str(hello[0][5])


                    if len(list) == itemsScanning:
                        return list

def identify_Tradelog_Color(startingCordinates, resizeX, resizeY):
    imgTradeLogScreenShot = desktop_Screenshot(startingCordinates[0], startingCordinates[1], startingCordinates[2],startingCordinates[3], resizeX, resizeY)
    imgTradeLogColor = cv2.cvtColor(imgTradeLogScreenShot, cv2.COLOR_BGR2RGB)
    tradeLogColorIdentifier = findColor(imgTradeLogColor)

    return len(tradeLogColorIdentifier)





