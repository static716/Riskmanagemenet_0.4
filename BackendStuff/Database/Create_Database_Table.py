import sqlite3
from datetime import date

class initiate:
    def __init__(self):
        connection = sqlite3.connect('TradeLogSection.db')  ## create or connect to database
        myCursor = connection.cursor()

        today = str(date.today()).replace("-", "")
        today = "a" + today
        tableCount = myCursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table'" )
        tableCount = tableCount.fetchall()[0][0]

        if tableCount == 0 :

            myCursor.execute("""CREATE TABLE IF NOT EXISTS a (Time text,
            Symbol text,
            Side text,
            Price text,
            Quantity text,
            Route text,
            ProfitLoss text
            )""")

            myCursor.execute("ALTER TABLE a RENAME TO " + today)

        elif tableCount >= 1:

            fetchLastTableName = myCursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND oid= " + str(tableCount))
            fetchLastTableName = fetchLastTableName.fetchall()
            fetchLastTableName = fetchLastTableName[0][1]

            if fetchLastTableName != today:
                letter = str(fetchLastTableName[0])

                yearL1 = str(fetchLastTableName[1])
                yearL2 = str(fetchLastTableName[2])
                yearL3 = str(fetchLastTableName[3])
                yearL4 = str(fetchLastTableName[4])
                year = yearL1+yearL2+yearL3+yearL4

                monthL1 = str(fetchLastTableName[5])
                monthL2 = str(fetchLastTableName[6])
                month = monthL1 + monthL2

                dayL1 = str(fetchLastTableName[7])
                dayL2 = str(fetchLastTableName[8])
                day = dayL1 + dayL2

                if month == "01" or month == "03" or month =="05" or month =="07" or month =="08" or month == "10" or month == "12":
                    if day == "31":
                        day = "01"
                        if month == "12":
                            month = "01"
                            year = str(int(year)+1)
                            newtTableName = letter + year + month + day
                        else:
                            month = monthL1 + str(int(monthL2)+1)
                            newtTableName = letter+year+month+day

                    elif day == "09" or day == "19" or day == "29":
                        day = str((int(dayL1) * 10) + (int(dayL2) + 1))
                        newtTableName = letter + year + month + day
                    else:
                        day = dayL1 + str(int(dayL2) + 1)
                        newtTableName = letter + year + month + day

                elif month == "02":
                    if day == "28" and int(year)%4 != 0:
                        day = "01"
                        month = monthL1 + str(int(monthL2) + 1)
                        newtTableName = letter + year + month + day
                    elif day == "28" and int(year)%4 == 0:
                        day = "29"
                        newtTableName = letter + year + month + day
                    elif day == "29":
                        day = "01"
                        month = monthL1 + str(int(monthL2) + 1)
                        newtTableName = letter + year + month + day
                    elif day == "09" or day == "19":
                        day = str((int(dayL1) * 10) + (int(dayL2) + 1))
                        newtTableName = letter + year + month + day
                    else:
                        day = dayL1 + str(int(dayL2) + 1)
                        newtTableName = letter + year + month + day
                else:
                    if day == "30":
                        day = "01"
                        if month == "09":
                            month = str(int(monthL2)+1)
                            newtTableName = letter + year + month + day
                        else:
                            month = monthL1 + str(int(monthL2)+1)
                            newtTableName = letter + year + month + day

                    elif day == "09" or day == "19" or day == "29":
                        day = str((int(dayL1) * 10) + (int(dayL2) + 1))
                        newtTableName = letter + year + month + day
                    else:
                        day = dayL1 + str(int(dayL2) + 1)
                        newtTableName = letter + year + month + day

                try:
                    myCursor.execute("""CREATE TABLE IF NOT EXISTS a (Time text,
                                Symbol text,
                                Side text,
                                Price text,
                                Quantity text,
                                Route text,
                                ProfitLoss text
                                )""")
                    myCursor.execute("ALTER TABLE a RENAME TO " + newtTableName)
                except:
                    myCursor.execute("DELETE FROM sqlite_master WHERE type = 'table' AND name = 'a' IF EXISTS ")
                    print("Table Already Exist In Database")

        connection.commit()
        connection.close()