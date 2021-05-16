''' source for help:
reading from a file: https://youtu.be/0EgSo7hsRWM
writing to a file: https://youtu.be/W0fPZQBFpVE
'''

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
# isnumeric() to determine if all the characters in a string are numeric 
 
# ----------------------------------------------------------------------- #

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

def printList():
    for line in listOfLines:
        if(foundInText(line, ',') and not foundInText(line.lower(), "summary")):
            print(line)



fin = input("input a csv file (should end in \'.csv\'): ")

while (not foundInText(fin, ".csv")):
    fin = input("text file must end in \'.csv\': ")

fin = "inputFiles/" + fin

listOfLines = loadFileContent(fin)

print("success loading a file! Here are the contents:")

printList()


print("\n\nNow we will write to a file")

myNewFilename = input("Give your new file a name: ")

outFile = open(myNewFilename, 'w')
outFile.write("This is a test")
outFile.close()



