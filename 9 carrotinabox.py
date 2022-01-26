





import random


while True:
        print('''Carrot in a Box, 

                This is a bluffing game for two human players. Each player has a box.
                One box has a carrot in it. To win, you must have the box with 
                the carrot in it,.
                
                This is a very simple and silly game.
                
                The first player looks into their box(the second player must close their eyes during this).
                The first player then says "There is a carrot in my box"
                or "There is not a carrot in my box". 
                The second player then gets tp decide if want to swap boxes or not.        ''')

        input('Press Enter to begin.....')

        p1Name =  input('Human player1, enter your name: ')
        p2Name = input('Human player 2, enter your name: ')
        playerNames = p1Name[:11].center(11)+'    '+ p2Name[:11].center(11)

        print('''HERE ARE TWO BOXES:
        __________        __________
        /         / |     /         /| 
        +---------+ |    +---------+ |
        | RED     | |    |   GOLD  | |
        | BOX     | /    |   BOX   | /
        +---------+/     +---------+/''')

        print()
        print(playerNames)
        print()
        print(p1Name + ', you have a RED box in front of you. ')
        print(p2Name + ', you have a GOLD box in front of you. ')
        print()
        print(p1Name + ', you will get to look into your box.')
        print(p2Name.upper() + ', close your eyes and don\'t look!!!')
        print('When' + p2Name + 'has closed their eyes, pass Enter....')
        print()

        print(p1Name + 'here is the inside of your box: ')

        if random.randint(1, 2) == 1:
                carrotInFirstBox = True
        else: 
                carrotInFirstBox = False

        if carrotInFirstBox:
                print('''
                ____VV______
                |   VV      |
                |   VV      |
                |___||___  _|     __________
                /   ||    /  |    /          / |
                +---------+  |    +---------+  |
                | RED     |  |   |    GOLD  |  |
                | BOX     |  /   |    BOX   | /
                +---------+ /    +---------+/
                (carrot!) ''')
                print(playerNames)
        else:
                print('''
                ___________
                |           |
                |           |
                |___________|     __________
                /          / |    /          / |
                +---------+  |    +---------+  |
                | RED     |  |   |    GOLD  |  |
                | BOX     |  /   |    BOX   | /
                +---------+ /    +---------+/
                (no carrot!) ''')
                print(playerNames)

        input('Press Enter to continue... ')

        print('\n'* 100) #Clear the screen by printing several newlinew.
        print(p1Name + ', tell' + p2Name + ' to open their eyes')
        input('press Enter to continue... ')

        print()
        print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
        print(' 1) There is a carrot in my box. ')
        print(' 2) There is not carrot in my box. ')
        print()
        print('Then press Enter to continue....')

        print()
        print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
        while True:
                response = input('> ').upper()
                if not (response.startswith('Y') or response.startswith('N')):
                        print(p2Name +', please enter "YES" or "NO". ')
                else:
                        break

        firstBox = 'RED ' #Note the space after the "D".
        SecondBox = 'GOLD' 

        if response.startswith('Y'):
                carrotInFirstBox = not carrotInFirstBox
                firstBox, SecondBox = SecondBox , firstBox

                print('''Here are the two boxes:
                        ___________          __________
                        /          / |       /          / |
                        +---------+  |       +---------+  |
                        | {}      |  |       | {}      |  |  
                        | BOX     |  /       | BOX     |  /  
                        +---------+ /        +---------+ / '''.format(firstBox, SecondBox)) 
        print(playerNames)

        input('Press Enter to reveal the winner...')
        print()

        if carrotInFirstBox:
                print('''
                        ___________          ___VV______
                        |           |        |   VV      |
                        |           |        |   VV      |
                        |___________|        |___||___  _|
                        /          / |       /   ||    /  |
                        +---------+  |       +---------+  |
                        | {}      |  |       | {}      |  |  
                        | BOX     |  /       | BOX     |  /  
                        +---------+ /        +---------+ / '''.format(firstBox, SecondBox)) 

        else:
                print('''
                                ___________          ___VV______
                                |           |        |   VV      |
                                |           |        |   VV      |
                                |___________|        |___||___  _|
                                /          / |       /   ||    /  |
                                +---------+  |       +---------+  |
                                | {}      |  |       | {}      |  |  
                                | BOX     |  /       | BOX     |  /  
                                +---------+ /        +---------+ / '''.format(SecondBox, firstBox))

        print(playerNames)

        #This modification made possible through the 'carrotInFirstBox' variable
        if carrotInFirstBox:
                print(p1Name +'is the winner! ')
        else:
                print(p2Name + 'is the winner!')

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
print('Thanks for playing!')














