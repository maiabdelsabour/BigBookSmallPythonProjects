




import sys

# (!) try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of htis string:


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
.................................................................... """

print('Bitmap Message, by Al Sweigart')
print('Enter the message to diplay with bitmap.')
message = input('> ')
if message == '':
    sys.exit()

#Loop over each line in the bitmap:
for line in bitmap.splitlines():#return list of string
    #loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == '':
            #Print an empty space since there's a space in the bitmap:
            print('', end='')
        else:
            #Print a character from the message:
            print( message[i % len(message)], end='')#repetition of text in message
    print() #Print a newline.
