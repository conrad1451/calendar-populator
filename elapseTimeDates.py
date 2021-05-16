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
# isnumeric() to determine if all the characters in a string are numeric 
 
# ----------------------------------------------------------------------- # 
 
 
 
def elapsedTimeBetweenTwoDates(firstTime, secondTime):
    fTime = datetime.strptime(firstTime, '%m/%d/%Y')
    sTime = datetime.strptime(secondTime, '%m/%d/%Y')
    
    print("\n")
    
    print("the first time is: ", fTime)
    print("and the second time is: ", sTime)
    

    
a = input("enter first time: ")
b = input("enter second time: ")


elapsedTimeBetweenTwoDates(a, b)