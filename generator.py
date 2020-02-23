#
# this module does the proper calculation
# of the best days for revision sessions
# according to the spaced repetition
# study techinique
#

from datetime import datetime, timedelta

fibonacciDays = [2,3,5,8,13,21,34,55,89,144,233,377]

def getDates(today, exam, difference):

    # First: find in what range the exam occurs
    revisionDays = fibonacciDays[:getRange(difference.days)]
    # Third: calculating the dates
    revisionDates = []
    for x in revisionDays:
        revisionDates.append(today + timedelta(days = x))
    # Fourth: printing the dates
    print("YOUR EXAM IS IN", difference.days, "days")
    printDates(revisionDates)

def getRange(difference):
    index = 0
    for value in fibonacciDays:
        if value < difference:
            index+=1
        else:
            pass
    return index

def printDates(revisionDates):
    print("And for greater chances of recalling the content,\nyour studying session should be on the following dates:")
    i = 0
    for date in revisionDates:
        print ('Your', i ,'th revision should be in:\t', date.strftime('%m/%d/%y'))
        i+=1