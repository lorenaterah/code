#! /usr/bin/python3

import sys


def head(textfile, n='10'):
    try:
        with open(textfile, 'r') as file:
            filetext = file.readlines()

            for i in range(int(n)):
                print(filetext[i])
    except IndexError:
        pass

if __name__ == '_main_':
    arguments = sys.argv

    
    if len(arguments) == 2:
        #['./headfile.py', 'document.txt']
        filetxt = arguments[1]

        head(filetxt)
    
    if len(arguments) == 4:
        #['./headfile.py', '-n', '5', 'document.txt']
       if arguments[1] == '-n':
           n = arguments[2]
           filetxt = arguments[3]

           head(filetxt, n)

    if len(arguments) > 4 or len(arguments) == 3:
        print('Provide Required arguments (-n number) or file or both')

    
