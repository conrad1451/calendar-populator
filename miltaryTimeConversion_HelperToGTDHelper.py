from datetime import datetime
 
 
# ---------------------- MY STANDARD HELPER FUNCTIONS -------------------- #

# returns true if 'theChar' is found in 'theStr'
def foundInText(theStr, theChar):
    # returns true if 'theChar' is found in 'str'
    return theStr.find(theChar) != -1;

# returns true if 'substr' is found in 'theStr'
def foundInText(theStr, substr):
    # returns true if 'substr' is found in 'str'
    return theStr.find(substr) != -1;

# note that all string methods return new values
# source: https://www.w3schools.com/python/python_ref_string.asp

# things that are standard in python library (but not C++)
# "==" to compare two strings to determine if their characters are equal
# casefold() to convert a string to lower case
# lower() to convert a string to lower case
# islower() to determine if all the characters in a stirng are lowercase
# isnumeric() is a method to a string to determine if all the characters in a string are numeric 
 
# ----------------------------------------------------------------------- # 
 



def timeAdjust(time, AM, eod):
    theTime = 0
    
    if(AM and time > 1200):
        theTime = time - 1200
    elif(  (not AM and time < 1200) or eod  ):
        theTime = time + 1200
    return theTime    



def loadFileContent(inputFilename):
    # open input file to read content
    infile = open(inputFilename, 'r')
    fileContent = infile.readlines()
    
    listOfLines = []
    for line in fileContent:
        if(line[-1] == '\n'):
            listOfLines.append(line[:-1])
        else:
            listOfLines.append(line)

    infile.close()
    return listOfLines 
    



def doTheThing(theListOfEventBlocks, theMode):
    theDayList = [ [], [], [], [], [], [], [] ]
        
    # TODO - test done
    # counter = 0
    
    dayIndex = -1
    curDay = "sun"
    
    myFilename = input("Give your output file a name (should end in \'.csv\'): ")
    
    while (not foundInText(myFilename, ".csv")):
        myFilename = input("text file must end in \'.csv\': ")
        
    outFile = open(myFilename, 'w')
    
    
    # An event block is a single event with a name, start and end time.
    # It may be an isolated event or part of a series of events
    for eventBlock in theListOfEventBlocks:
        isADataLine = foundInText(eventBlock, ',') and not foundInText(eventBlock.lower(), "summary")
        
        if(not isADataLine):
            outFile.write(eventBlock + "\n")
        else:        
            aLine = csvLineConversion(eventBlock)
            outFile.write(aLine + "\n")
        
            
    outFile.close() 


def splitIntoStringList(theStr, charSplitter):
    # takes in a string called "theStr" and character called "theChar" and returns a list of strings
    
    theList = []
    startPos = 0
    endPos = 0

    while (foundInText(theStr, charSplitter) and endPos != -1):
    
        endPos = theStr.find(charSplitter, startPos)
        if (endPos != -1):
        
            theList.append(theStr[startPos : endPos+1])
            startPos = endPos + 1

    # end of while loop, last step is to return from function

    # TODO
    #print("shown following for testing purposes", theList[2], "\n\n")
    return theList;




   
    
def grabTime(dateToSplit, prevTime):
    passedFirstHr = False
    endOfDay = True
    
    timeSplitPos = dateToSplit.find("2021")
    stringifiedTime = dateToSplit[timeSplitPos + 5: -4]
    
    theHr = stringifiedTime[0 : -3]
    theMin = stringifiedTime[-2 :]
    
    timeAsNum = int(theHr)*100 + int(theMin) 
    
    return timeAsNum


def newTimeConversion(theTime, theTimeIsAM):
    hourPart = ""
    minPart = ""

    # TODO - test done
    # print("theTime is ", theTime) 
    if(theTime >= 1200 and theTimeIsAM):
        theTime = theTime - 1200
        hourPart = "00"
        
    elif(theTime < 1200 and theTimeIsAM):
        hourPart = "0" + str(int(theTime / 100))
        
    else:
        hourPart = str(int(theTime / 100))
        

    if(theTime % 100 == 0):
        minPart = "00"
        
    elif(theTime % 100 < 10):
        minPart = "0" + str(int(theTime % 100))
        
    else:
        minPart = str(int(theTime % 100))
        
    return hourPart + ":" + minPart
        
         

    
    csvLineConversion
    
    
def csvLineConversion(inputStr):
    # takes in a string called "inputStr" and returns a CalEvent
    
    logPrintingForTesting = False
    
    # TODO - testing
    #print(inputStr)
    stringList = splitIntoStringList(inputStr, ',')
    firstTimeSplitPos = 0
    secondTimeSplitPos = 0
    
    # FIXME
    dayOfWeek = ""
    stringifiedBeginTime = ""
    stringifiedEndTime = ""
    beginTime = 0
    endTime = 0
    
    dayOfWeek = ""
    
    name = stringList[0]
    name = name[:-1]
    # TODO - test complete
    # print("name is", name)
    firstDateToSplit = stringList[1]
    secondDateToSplit = stringList[2]


    # TODO - will this make a bug?
    prevTime = 0
    
    # TODO - test done
    # print("shown following for testing purposes", inputStr, "\n\n")
    
    if(len(stringList) > 0):
        if (foundInText(firstDateToSplit, "2021")):
            
            newStringifiedTime = ""
            
            firstTimeSplitPos = firstDateToSplit.find("2021")
            
            beginTimeIsAM = foundInText(firstDateToSplit, "AM")
            beginTimeIsPM = foundInText(firstDateToSplit, "PM") 
            
            beginTime = grabTime(firstDateToSplit, 0)
            
            if(beginTimeIsPM and beginTime < 1200):
                beginTime = beginTime + 1200 
                            
            substr1 = firstDateToSplit[0 : firstTimeSplitPos + 5]
            aNewDate = substr1 + newTimeConversion(beginTime, beginTimeIsAM) + ","

            oldDate = stringList[1]
            stringList[1] = aNewDate
            newDate = stringList[1]
            
            if(logPrintingForTesting):            
                print("Start time for an event:")
                print("\tthe old date is: ", oldDate)
                print("\tthe new date is: ", newDate) 


        if (foundInText(secondDateToSplit, "2021")):
            
            newStringifiedTime = ""
            
            secondTimeSplitPos = secondDateToSplit.find("2021")
            
            endTimeIsAM = foundInText(secondDateToSplit, "AM")
            endTimeIsPM = foundInText(secondDateToSplit, "PM") 
            
            endTime = grabTime(secondDateToSplit, 0)
            
            if(endTimeIsPM and endTime < 1200):
                endTime = endTime + 1200
                            
            substr1 = secondDateToSplit[0 : secondTimeSplitPos + 5]
            aNewDate = substr1 + newTimeConversion(endTime, endTimeIsAM) + ","
            
            oldDate = stringList[2]
            stringList[2] = aNewDate
            newDate = stringList[2]
            
            if(logPrintingForTesting): 
                print("End time for an event:")
                print("\tthe old date is: ", oldDate)
                print("\tthe new date is: ", newDate) 
            
            
            
            
    return stringList[0] + stringList[1] + stringList[2] + stringList[3] #+ stringList[4] 


def autoConverter():
    # will return autoAddedCalEvents
    
    # FIXME: not needed and will delete
    mode = 2
    

    autoAddedCalEvents = []

    fin = input("Enter name of the input text file (should end in \'.csv\'): ")

    while (not foundInText(fin, ".csv")):
        fin = input("text file must end in \'.csv\': ")
    
    print("\n")
    fin = "inputFiles/" + fin 
    listOfEventBlocks = loadFileContent(fin)
    
    doTheThing(listOfEventBlocks, mode) 
            
    return autoAddedCalEvents



def main():
    allCalEvents = []
        
    anInput = input("Select 1 for the manual event scanning or 2 for the automatic event scanning): ")

    while(anInput != "1" and anInput != "2"):
        anInput = input("Select a valid input! (1 for the manual event scanning or 2 for the automatic event scanning): ")

    if(anInput == "1"):
        theCondition = True
        while (theCondition):
            # FIXME: Add manualEventCreation as a function
            #allCalEvents.append(manualEventCreation())
            
            myStr = input("\nwant to add new event (Y|N): ")
            print("\n\n")
            theCondition = (len(myStr) == 1) and ( (myStr.lower())[0] == 'y' )

    elif (anInput == "2"):
        listOfEvents = autoConverter()



main()
    