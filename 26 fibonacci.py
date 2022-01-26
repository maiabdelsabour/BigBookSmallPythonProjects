




import sys

print('''Fibonacci Sequence, by Al Sweigart.........
    
        The Fibonacci sequence begins with 0 and 1, the next number is the sum of the previous two numbers.
        the sequence continues forever:
        
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 ... 
        ''')

while True:       #main program loop.
    while True:     #keep asking until the user enters valid input.
        print('''Enter the Nth Fibonacci number you wish to calculate
                (such as 5, 50, 1000, 9999), or QUIT to quit: ''')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break #Exit the loop when the user enters a valid number.

        print('Please enter a number greater than 0, or QUIT.')
    print()

    # Handle the special cases if the user entered 1 or 2:
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci is 1.')
        continue

    #Display warning if the user entered a large number.
    if nth >= 10000:
        print('''WARNIGN: This will take a while to display on the screen.
                If you want to quit this program before it is done,
                press Ctrl-C.''')
        input('Press Enter to begin...')

    #Calculate the Nth Fibonancci number.
    secondToLastNumber = 0 
    lastNumber = 1
    fibNumbersCaluclulated = 2
    print('0, 1, ', end='') #Display the first two fibonacci numbers.

    #Display all the later numbers of the Fibonnaci sequence.
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCaluclulated += 1

        #Display the next number in the sequence.
        print(nextNumber, end='')

        #Check if we've found the Nth number user wants:
        if fibNumbersCaluclulated == nth:
            print()
            print()
            print('The #', fibNumbersCaluclulated, ' Fibancci',
                    'number is ', nextNumber, sep='')
            break

        #Print a comma in between the sequence numbers.
        print(', ', end='')

        #Shift the last two numbers.
        secondToLastNumber = lastNumber
        lastNumber = nextNumber


