





import random, sys, time

PAUSE = 0.15    #TRY CHANGING THIS TO 0.5 OR 0.0

#THERE ARE THE INDIVIDUAL ROWS OF THE DNA ANIMATION
ROWS = [
    #123456789 <- Use this to measure the number of spaces:
    '         ##',  # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    #123456789 <- Use this to measure the number of speces.

try:
    print('DNA Animaiton, by Al Sweigart............')
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    rowIndex = 0

    while True:
        #Incremant rowIndex to draw next row.
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0
        
        #Row indexes 0 and 9 don't have nucleotides.
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        '''Select random nucleotide pairs, 
        guanine-cytosine and adenine-thymine'''
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide ,rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide ,rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide ,rightNucleotide = 'G', 'C'

        # Print the row.
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)   #Add a slight pause.
except KeyboardInterrupt:
    sys.exit()  #when Ctrl-C is pressed, end the program