import os

def createTodayDir(ymd):
# Get current working directory
    path = ymd
# Check if folder exists for this date and create if not
    if not os.path.isdir(path):
        os.mkdir(path)
    return
