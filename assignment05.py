# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
#Zshen, 8/5/2020, Add code under #To do area
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
lstRow2 = []
lstRow4 = []
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# TODO: Add Code Here
file = open(objFile, "a")
file = open(objFile, "r")
for row in file:
  lstRow = row.split(",")
  dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
  lstTable.append(dicRow)
  lstRow2=[lstRow[0],lstRow[1].strip()]
  lstRow4.append(lstRow2)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
      # TODO: Add Code Here
        print('Your Current Data is ')
        for Data in lstTable:
          print(Data)
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
      # TODO: Add Code Here
        strtask = input('Enter you task: ')
        strpriority = input('Enter your Priority: ')
        dicRow2 = {'Task': strtask,'Priority': strpriority.strip()}
        lstTable.append(dicRow2)
        lstRow3=[strtask,strpriority]
        lstRow4.append(lstRow3)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
      # TODO: Add Code Here
        strChoice = int(input('Enter which row of data need to be removed: '))-1
        lstTable.pop(strChoice)
        lstRow4.pop(strChoice)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
      # TODO: Add Code Here
        print('Data Saved')
        file = open(objFile, "w")
        for Save in lstRow4:
          file.write(Save[0]+','+ Save[1] + '\n')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
      # TODO: Add Code Here
        print('File Closed')
        file.close()
        break  # and Exit the program


