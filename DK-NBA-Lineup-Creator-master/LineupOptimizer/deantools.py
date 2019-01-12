import datetime

def ymd():
    #returns a string where the format for March 01, 2001 would be 20010301
    now = datetime.datetime.now()
    year = str(now.year)
    if len(str(now.month)) < 2:
        month = '0' + str(now.month)
    else:
        month = str(now.month)
    if len(str(now.day)) < 2:
        day = '0' + str(now.day)
    else:
        day = str(now.day)
    ymd =  year + month + day #YearMonthDay
    
    return ymd

def dateNBAStats():
    
    now = datetime.datetime.now()
    year = str(now.year)
    if len(str(now.month)) < 2:
        month = '0' + str(now.month)
    else:
        month = str(now.month)
    if len(str(now.day)) < 2:
        day = '0' + str(now.day)
    else:
        day = str(now.day)
    
    return month, day, year
