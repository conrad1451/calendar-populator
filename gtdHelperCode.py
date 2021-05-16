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
 
 
class CalEvent(object):
    name = ""
    age = 0
    major = ""
    
    
    theName = ""
    theDayOfWeek = ""
    theStartTime = 0
    theEndTime = 0
    theRepeat = False
    

    # The class "constructor" - It's actually an initializer 
    def __init__(self, theName, theDayOfWeek, theStartTime, theEndTime, theRepeat):
        self.theName = theName
        self.theDayOfWeek = theDayOfWeek
        self.theStartTime = theStartTime
        self.theEndTime = theEndTime
        self.theRepeat = theRepeat

def make_calEvent(theName, theDayOfWeek, theStartTime, theEndTime, theRepeat):
    calEvent = CalEvent(theName, theDayOfWeek, theStartTime, theEndTime, theRepeat)
    return calEvent
  
def stringifyCalEvent(aCalEvent):
    line1 = "name: " + aCalEvent.theName + "\n"
    line2 = "day of week: " + aCalEvent.theDayOfWeek + "\n"
    line3 = "start time: " + str(aCalEvent.theStartTime) + "\n"
    line4 = "end time: " + str(aCalEvent.theEndTime) + "\n"
    line5 = "repeating event?: " + str(aCalEvent.theRepeat) + "\n"
    
    return line1 + line2 + line3 + line4 + line5




def findMin(val1, val2):
    if (val1 < val2):
        return val1
    else:
        return val2


def findMax(val1, val2):
    if (val1 > val2):
        return val1
    else:
        return val2


theDaysOfWeek = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


def elapsedTimeBetweenTwoDates(firstTime, secondTime):
    fTime = datetime.strptime(firstTime, '%m/%d/%Y')
    sTime = datetime.strptime(secondTime, '%m/%d/%Y')
    
    print("\n")
    
    print("the first time is: ", fTime)
    print("and the second time is: ", sTime)
    



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




def grabDay(dateToSplit):
    firstTimeSplitPos = dateToSplit.find("2021")
    theDay = dateToSplit[0 : firstTimeSplitPos + 4]
    
    timeFormattedDate = datetime.strptime(theDay, '%m/%d/%Y')
    stringFormattedDate = timeFormattedDate.strftime('%a,  %m/%d/%Y %H:%M:%S')
    
    # TODO - test done
    # print("Date in dd/mm/yyy format: ", stringFormattedDate)
            
    commaPos = stringFormattedDate.find(",")
    
    return stringFormattedDate[commaPos-3 : commaPos]
    
    
    
def isEndOfDay(curTime, passedFirstHr, isAM):
    return (curTime == 1200) and (passedFirstHr) and (not isAM)
    
    
def timeAdjust(time, AM, eod):
    theTime = 0
    
    if(AM and time > 1200):
        theTime = time - 1200
    elif(  (not AM and time < 1200) or eod  ):
        theTime = time + 1200
    return theTime    


def switchToPM(curTime, prevTime):
    returnVal = False
    
    # if(not prevTime.isnumeric()), do nothing
    
    """if(prevTime.isnumeric()):
        cur12 = (1200 <= curTime and curTime <= 1259)
        cur11Under = (100 <= curTime and curTime <= 1159)
        prev12 = (1200 <= prevTime and prevTime <= 1259)
        prev11Under = (100 <= prevTime and prevTime <= 1159)
        
        
        opt1 = prev11Under and cur12
        opt2 = False
         
        if(not(prev12 and cur11Under)):
            opt2 = prevTime > curTime 
            
        returnVal = opt1 or opt2"""
    cur12 = (1200 <= curTime and curTime <= 1259)
    cur11Under = (100 <= curTime and curTime <= 1159)
    prev12 = (1200 <= prevTime and prevTime <= 1259)
    prev11Under = (100 <= prevTime and prevTime <= 1159)
        
        
    opt1 = prev11Under and cur12
    opt2 = False
     
    if(not(prev12 and cur11Under)):
        opt2 = prevTime > curTime 
        
    returnVal = opt1 or opt2        
 
    return returnVal
        
  
   
    
def grabTime(dateToSplit, prevTime):
    passedFirstHr = False
    endOfDay = True
    
    timeSplitPos = dateToSplit.find("2021")
    stringifiedTime = dateToSplit[timeSplitPos + 5: -1]
    
    # no longer needed because input file is in miltary time
    # timeOfDayIdentifier = dateToSplit[timeSplitPos + 10: -1]
    
    # TODO - test done
    """print("dateToSplit is ", dateToSplit)
    print("stringifiedTime is ", stringifiedTime)
    print("\n")"""
    
    if(len(stringifiedTime) < 3):
        theHr = "0"
    else:
        theHr = stringifiedTime[0 : -3]
    
    
    theMin = stringifiedTime[-2 :]
    
    timeAsNum = int(theHr)*100 + int(theMin)
    
    
    #nowAtAM = timeOfDayIdentifier == "AM"

    if(timeAsNum <= 1159):
        passedFirstHr = True

    """ this following line determining isEndOfDay is part of why timeAdjust
      is failing and producing 3x the data (the extra data erronesouly) """
    #if (isEndOfDay(timeAsNum, passedFirstHr, nowAtAM)):
    #    endOfDay = True
    #    print("why have we reached end of day?")

    #if (switchToPM(timeAsNum, prevTime)):
    #    nowAtAM = False
    
    #correctedTime = timeAdjust(timeAsNum, nowAtAM, endOfDay)

    return timeAsNum
    #return correctedTime


def modeNameAlteration(curEvent, curMode, theStart, theEnd):
    chosenName = ""
    if (curMode == 1):
        chosenName = curEvent.theName

    elif (curMode == 2):
        timesToAdd = " start: " + str(theStart) + " end: " + str(theEnd)
        chosenName = "\n" + "[" + curEvent.theName + timesToAdd + "]"
        
    return chosenName
    

def fakeBreakPoint():
    response = input("Press space to leave breakpoint: ")

    while (response != " "):
        response = input("I said presss space if you want to leave breakpoint")
        
        
  
def splitIntoDayListEntries(theDayList, inputEvent, theDayIndex, theMode, theCounter):
    """ It seems that passing in theDayList is done by reference, because the
        edits I make to theDayList inside of this function are reflected outside
        of the function. Because of this, passing in theDayList as a parameter
        and then editing it works the same as editing a global variable
        (we avoid global variables as much as possible).
        
        Also notice how inputEvent is a parameter. if we did not want to edit
        theDayList in this function, we would have to have a helper function to
        return each 15 min interval, which are then pushed to theDayList from the
        function that called the helper function. This helper function would then,
        when a new event is reached, push the spaces to theDayList. It is much
        easier to implement as I have done.
    """
    
    #curStartTime = 0
    #curEndTime = 0
    
    # TODO - is this following line even necessary?
    startVal = findMax(0, inputEvent.theStartTime)
    endVal = findMin(startVal + 15, inputEvent.theEndTime)
    #endVal = 0
    
    # the following commented chunk of code results in a missingEvent fail 
    """
    hitShortEvent = False
    
    if(abs(inputEvent.theEndTime - inputEvent.theStartTime) < 15): #((inputEvent.theEndTime - startVal) < 15):
        # Following line never reached - all events happen to end at 15, 30, 45, or 00 of the hour
        curEndTime = inputEvent.theEndTime
        # TODO - testing
        hitShortEvent = True
        print("\n")
        print("starttime: ", inputEvent.theStartTime, "endtime: ", inputEvent.theEndTime)
        print("short event hit: ", inputEvent.theName, ": ", inputEvent.theStartTime, " - ", inputEvent.theEndTime)
        fakeBreakPoint()
        print("\n\n\n")
    else:
        curEndTime = startVal + 15
    
    print("\n\nstarttime: ", inputEvent.theStartTime, "endtime: ", inputEvent.theEndTime)
    print("curEndTime is ", curEndTime, " and inputEvent.theEndTime is ", inputEvent.theEndTime)
    """

    """                          
    if(theCounter <= 13):
        print("first event catch?: ", inputEvent.theName)
    """
                    
    # endVal should never be greater than theEndTime, so a less than sign is used in while loop
    while (endVal < inputEvent.theEndTime):

        # endVal should be corrected to represent 60-minute hours before any incrementation or use
        if((endVal % 100) == 60):
            endVal = endVal + 40    
        
        result = modeNameAlteration(inputEvent, theMode, startVal, endVal)
        
        theDayList[theDayIndex].append(result) # may need to edit later to fit multiple     events that overlap

        startVal = endVal
        
        # How close endVal is to the end time determines how much to increment endVal 
        if((inputEvent.theEndTime - endVal) <= 15):
            # Following line never reached - all events happen to end at 15, 30, 45, or 00 of the hour
            endVal = inputEvent.theEndTime 
        else:
            endVal = endVal + 15
    
    """                                
    if(theCounter <= 13):
        print("second event catch?: ", inputEvent.theName, "\n\n")
    """    
    result = modeNameAlteration(inputEvent, theMode, startVal, endVal)
    theDayList[theDayIndex].append(result)
    
    # provides spacing after the printout of each day to the log file
    theDayList[theDayIndex].append("\n\n\n")
    


    
    
def automaticEventCreation(inputStr):
    # takes in a string called "inputStr" and returns a CalEvent
    
    # lets make following assumptions
    # every event is contained within a single day (as opposed to spanning days)
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
            
            beginTime = grabTime(firstDateToSplit, prevTime)
            prevTime = beginTime
            
            dayOfWeek = grabDay(firstDateToSplit)
            
            # TODO - test done
            # print("Day of week: ", dayOfWeek)
            # TODO - test done
            # print("begin time: ", beginTime)

        #else:
            # I’m not processing dates before Jan 1 2021. Too hard.


        if (foundInText(secondDateToSplit, "2021")):
            
            secondTimeSplitPos = secondDateToSplit.find("2021")
            endTime = grabTime(secondDateToSplit, prevTime)
            prevTime = endTime
            # TODO - test done
            # print("end time: ", endTime, "\n\n")

        #else
            # I’m not processing dates before Jan 1 2021. Too hard.

         
    testCalEvent = CalEvent(name, dayOfWeek.lower(), beginTime, endTime, False)
    return testCalEvent;



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
    


def handleLogOutput(aDayList, theMode):
    
    # TODO: this test shows that aDayList, for some reason, is not properly storing testEvent3 and
    # 4 right after testEvent1 and 2. The reason the printout is incorrect is because the data
    # stored in aDayList is incorrect, somehow.
    print(aDayList)
    
    myFilename = input("Give your log file a name (should end in \'.txt\'): ")

    while (not foundInText(myFilename, ".txt")):
        myFilename = input("text file must end in \'.txt\': ")
        
    outFile = open(myFilename, 'w')

    dayNum = 0
    for eachDay in aDayList:
        outFile.write("Now printing day: " + theDaysOfWeek[dayNum] + "\n")
        
        tmpStr = ""
        for eachLog in eachDay:
            tmpStr = tmpStr + eachLog
        
        """ if (theMode == 2):
            print(eachLog) """
            
        outFile.write(tmpStr)
        
        # TODO - test complete
        # outFile.write("\n\nNew day up\n\n")
        dayNum = dayNum + 1
        
    outFile.close()

    
    

def setMode(): 
    inputNum = input("Select a mode in which to write log file (1 or 2): ")
    
    # Implementing "until loop" in python for this application
    checksPassed = False
    
    while(not checksPassed):
        if(inputNum.isnumeric()):
            theNum = int(inputNum)
            if(theNum == 1 or theNum == 2):
                checksPassed = True
        if(not checksPassed):
            inputNum = input("Input should be either \'1\' or \'2\': ")

    return int(inputNum) 
    

def loadDayList(theListOfEventBlocks, theMode):
    theDayList = [ [], [], [], [], [], [], [] ]
        
    # TODO - test done
    #
    counter = 0
    
    dayIndex = -1
    curDay = "sun"
    
    # An event block is a single event with a name, start and end time.
    # It may be an isolated event or part of a series of events
    for eventBlock in theListOfEventBlocks:
        if(foundInText(eventBlock, ',') and not foundInText(eventBlock.lower(), "summary")):
        
            anEvent = automaticEventCreation(eventBlock)
            
            # update day to ensure each day of week gets their respective events
            if(anEvent.theDayOfWeek != curDay):
                dayIndex = dayIndex + 1
                curDay = anEvent.theDayOfWeek
                        
            # split current event into theDayList entries to load into theDayList at respective dayIndex
            
            """
            if(counter <= 13):
                print("all event catch: ", anEvent.theName)
            """
            
            if (dayIndex < 7):
                
                splitIntoDayListEntries(theDayList, anEvent, dayIndex, theMode, counter)

            
            # TODO - test verifying that every event in original csv file is converted into an event
            """
            print("Event #", str(counter), ": \n", stringifyCalEvent(anEvent), "\n\n")"""
            counter = counter + 1
            
            # FIXME: may not be necessary - I might remove
            # autoAddedCalEvents.append(anEvent)
            
    return theDayList
            
    
def modifiedDayList(aDayList):
    return 0
    
    
def autoConverter():
    # will return autoAddedCalEvents
    
    mode = setMode()
    

    autoAddedCalEvents = []

    fin = input("Enter name of the input text file (should end in \'.csv\'): ")

    while (not foundInText(fin, ".csv")):
        fin = input("text file must end in \'.csv\': ")
    
    print("\n")
    fin = "inputFiles/" + fin 
    listOfEventBlocks = loadFileContent(fin)
    
    dayList = loadDayList(listOfEventBlocks, mode)
    
    #TODO - testing now
    #newDayList = modifiedDayList(dayList)
    
    handleLogOutput(dayList, mode)

            
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

