




import datetime

#Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'saturday')
Months = ('January', 'February', 'March', 'April', 'May', 'Jun', 'July',
            'August', 'September', 'October', 'November', 'December')

print('Calender Maker, ')

while True:     #loop to get a year from the user.
    print('Enter the year for the calender: ')
    response = input('> ')

    if response.isdecimal() and int(response)>0 :
        year = int(response)
        break

    print('Please enter a numeric year, like 2003 ')
    continue

while True:     # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12: ')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for march.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12. ')

 
def getCalendarFor(year, month):
    calText = ''    #calText will contain the string of our calender.

    #Put the month and year at the top of the calender.
    calText += (' ' * 34)+ Months[month-1] + ' '+ str(year) + '\n'

    
    #Add the days of the week labels to the calender.
    calText += '...Sunday....Monday....Tuesday....Wednesday....Thursday....Friday....Saturday..\n'
    
    #The horizontal line string that separate weeks.
    weekSperator = ('+------------'*7) + '+\n'
                   
    #The blank rows have ten spaces in between the | day seperators.
    blankRow = ('|            '*7) + '+\n'

    '''Get the first date in the month. 
    (The datetime module handles all the complicated calender stuff for us here. )'''
    currentDate = datetime.date(year, month, 1)

    '''Roll back currentDate untill it is Sunday. (Weekday() return 6 
    for sunday, not 0. '''
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    
    while True:     #Loop over each week in the month.
        calText += weekSperator

        #dayNumberRow is the row with the day number labels.
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' '*8)
            currentDate += datetime.timedelta(days=1)   #gO TO NEXT DAY.
        dayNumberRow += '|\n' #Add the vertical line after saturday.

        #Add the day number row and 3 blank rows to the calender text.
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        #Check if we're done with the month.
        if currentDate.month != month:
            break

    #Add the horizontal line at the very bottom of the calender.
    calText += weekSperator
    return calText


calText = getCalendarFor(year, month)
print(calText)  #Display the calender.

#save the calender to a text file.
calenderFilename = 'calender_{}_{}.txt'.format(year, month)
with open(calenderFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to' + calenderFilename)


