#
# this module is responsible for receiving
# the data and formatting it
#

import datetime
from datetime import date
from datetime import timedelta
import generator


def dateValidation(examDay):
    today = date.today()

    difference = examDay - today

    if difference.days < 0 :
        print("haha your exam has already happened!")
    elif difference.days == 0 :
        print("Your exam is today bro haha")
    elif difference.days > 365:
        print("You exam is way too far from now, chill out bro!")
    else:
        generator.getDates(today, examDay, difference)
    

entryDate = input('Insert the date of your exam in the MM-DD-YYYY:\t')
month, day, year = map(int, entryDate.split('-'))
examDay = datetime.date(year,month,day)
dateValidation(examDay)




