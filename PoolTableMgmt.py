from datetime import datetime
import time
import json

def table_is_free(user):
    name = ""
    endTime = time.time()
    startTime = 0
    elapsed = 0
    with open('tables.json') as file_object:
        arrayOfDictionaries = json.load(file_object)
        one = arrayOfDictionaries[user - 1]
        name = one['name']
        startTime = one['startTime']
        one['avail'] = 'Not Occupied'
        one['endTime'] = endTime
        elapsed = endTime - startTime
    createFinalReport(name, startTime, endTime, elapsed)
    with open('tables.json', 'w') as file_object:
        json.dump(arrayOfDictionaries,file_object)

def table_is_occupied(user):
    sTime = time.time()
    with open('tables.json') as file_object:
        arrayOfDictionaries = json.load(file_object)
        one = arrayOfDictionaries[user - 1]
        if one['avail'] == 'Occupied':
            print ('\n' + "this table is already taken" + '\n')
        else:
            one['avail'] = 'Occupied'
            one['startTime'] = sTime
    with open('tables.json', 'w') as file_object:
        json.dump(arrayOfDictionaries,file_object)
    
    
def viewTable():
    with open('tables.json') as file_object:
        arrayOfDictionaries = json.load(file_object)
        for a in arrayOfDictionaries:
            for index in a:
                if a['avail'] == 'Occupied':
                    print (a['name'] + "  " + a['avail'] + "  " + time.ctime(a['startTime']))
                else:
                    print (a['name'] + "  " + a['avail'] + "  ")
                break

def createFinalReport(w,x,y,z):
    name = w
    formattedStart = time.ctime(x)
    formattedEnd = time.ctime(y)
    finalTime = timeFormat(formattedEnd)
    elapsed = (z)/60
    cost = (elapsed/60) * 30
    if elapsed >= 60:
        with open(finalTime,'a') as file_object:
            file_object.write('\n' + '---------------------------------' + '\n')
            file_object.write(name + '\n')
            file_object.write(str(formattedStart) + '\n')
            file_object.write(str(formattedEnd) + '\n')
            file_object.write(str(elapsed) + " minutes" + '\n')
            file_object.write("Your balance due is $" + str(cost))
    else: 
        with open(finalTime,'a') as file_object:
            file_object.write('\n' + '---------------------------------' + '\n')
            file_object.write(name + '\n')
            file_object.write(str(formattedStart) + '\n')
            file_object.write(str(formattedEnd) + '\n')
            file_object.write(str(elapsed) + " minutes")
    
def timeFormat(time):
    date = datetime.strptime(time, "%a %b %d %H:%M:%S %Y")
    stringDate = str(date.month) + "-" + str(date.day) + "-" + str(date.year) + ".txt"
    return stringDate
            

while True: 
    print("********************************" + "\n")
    viewTable() 
    
    firstUserChoice = raw_input("\n" + "Welcome Admin! Please choose what you would like to do:" + "\n" +  "'1' Assign a Table" + "\n" + "'2' Close a table" + "\n" + "'3' View Table Status" + "\n" + "'q' to quit : ")
    
    if firstUserChoice == "1":
        chooseTable = int(raw_input("What table would you like to assign? "))
        table_is_occupied(chooseTable)
    elif firstUserChoice == "2":
        chooseFreeTable = int(raw_input("What table would you like to close? "))
        table_is_free(chooseFreeTable)
    elif firstUserChoice == "3":
        viewTable()
    elif firstUserChoice.lower() == "q":
        break

    print("********************************")