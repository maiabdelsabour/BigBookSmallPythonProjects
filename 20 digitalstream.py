




import random, shutil, time, sys

#Set up the constants.
MIN_STREAM_LENGTH = 6   #TRY CHANGING THIS TO 1 OR 50.
MAX_STREAM_LENGTH = 14  #TRY CHANGING THIS TO 100.
PAUSE = 0.1             #TRY CHANGING THIS TO 0.0 OR 2.0
STREAM_CHARS =['0', '1'] #TRY CHANGING THIS TO OTHER CHARACTERS.

#DENSITY CAN RANGE FROM 0.- TO 1.0.
DENSITY = 0.2           #TRY CHANGINT THIS TO 0.10 OR 0.30.

#GET THE SIZE OF THE TERMINAL WINDOW.
WIDTH = shutil.get_terminal_size()[0]       #This module helps in automating process of copying and removal of files and directories.
'''We can't print to the last column on windows without id adding a newline automatically,
    so reduce the width by one.'''
WIDTH -= 1

print('Digital Stream, by Al Sweigart...........')
print('Press Ctrl-C to quit. ')
time.sleep(2)

try:
    '''For each column, when the counter is 0, no stream is shown.
    Otherwise, it acts as counter for how many times a 1 or 0.
    should be diplayed in that column. '''
    columns = [0]*WIDTH
    while True:
        # Set up the counter for each column.
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    #Restart a stream on this column.
                    columns[i] = random.randint(MIN_STREAM_LENGTH, 
                                                MAX_STREAM_LENGTH)
                
            #Display an empty space or a 1/0 character.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()     #print a newline at the end of the row columns.
        sys.stdout.flush()  #Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    print()