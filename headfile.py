import sys

def head(textfile, n='10'):
    try:
        with open(textfile, 'r') as file:
            filetext = file.readlines()

            for i in range(int(n)):
                print(filetext[i])                                                                  
    except IndexError:
        pass

if __name__ == '__main__':
    arguments = sys.argv[1:]

    if len(arguments) == 1:
        #['./headfile.py', 'document.txt']
        filetxt = arguments[0]
        head(filetxt) 
    
    elif len(arguments) == 3 and arguments[0] == '-n':
          #['./headfile.py', '-n', '5', 'document.txt']
        n = arguments[1]
        filetxt = arguments[2]
        head(filetxt, n)

    else:
        print('Provide Required arguments (-n number) or file or both')

#run
#python './headfile.py', 'document.txt'