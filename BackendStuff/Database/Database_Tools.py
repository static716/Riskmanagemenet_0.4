import sqlite3
from datetime import *

# Gets database table name
def get_Database_Table_Name():
    today = str(date.today()).replace("-", "")
    today = "a" + today
    return today

# Returns the current time
def getCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
#Customize Time to your preference
    # current_time = "01:00:00"
    return current_time

# Adds item to Trade Log Database
def add_Table_To_Database(list, db_Table_Name):
    DB_Table_Name = str(db_Table_Name)

    # list[0] = list[0].replace(".", "")
    # list[1] = list[1].replace("-", "")

    connection = sqlite3.connect('TradeLogSection.db')  ## create or connect to database
    myCursor = connection.cursor()

    myCursor.execute(
        "INSERT INTO " + DB_Table_Name + " VALUES (:Time, :Symbol, :Side, :Price, :Quantity, :Route, :ProfitLoss)",
        {
            'Time': str(list[0]),
            'Symbol': str(list[1]),
            'Side': str(list[2]),
            'Price': str(list[3]),
            'Quantity': str(list[4]),
            'Route': str(list[5]),
            'ProfitLoss': str(list[6])
        })

    connection.commit()
    connection.close()

def reorganize_DB_Table_In_Ascend_Order(db_Table_Name):
    DB_Table_Name = str(db_Table_Name)
    connection = sqlite3.connect('TradeLogSection.db')  ## create or connect to database
    myCursor = connection.cursor()
    myCursor.execute("SELECT * from " + DB_Table_Name + " ORDER BY Time DESC")
    databaseInfoList = myCursor.fetchall()

    myCursor.execute("DELETE FROM " + DB_Table_Name)
    connection.commit()
    connection.close()

    for i in range(len(databaseInfoList)):
        add_Table_To_Database(databaseInfoList[i], DB_Table_Name)

def compare_Time_Difference(databaseTime, startTime, timeList):

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

def check_If_Already_Exist(list, startTime):
    dbName = get_Database_Table_Name()
    connection = sqlite3.connect('TradeLogSection.db')
    myCursor = connection.cursor()

    rowCount = myCursor.execute("SELECT count(*) FROM " + dbName + "")
    rowCount = myCursor.fetchall()
    rowCount = int(rowCount[0][0])

    rowInfo = myCursor.execute("SELECT * FROM " + dbName + "")
    rowInfo = myCursor.fetchall()

    for currentRowSelected in range(rowCount):
        if compare_Time_Difference(dbName, startTime, rowInfo[currentRowSelected][0]):
            if rowInfo[currentRowSelected][0] == list[0]:
                count = 0
                for columnz in range(7):
                    if rowInfo[currentRowSelected][columnz] == list[columnz]:
                        count = count + 1
                        # print(count)
                        if count == 7:
                            return True

    connection.commit()
    connection.close()
    return False

