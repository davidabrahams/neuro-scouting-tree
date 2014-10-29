import sys

lines = sys.argv[1]
print(lines)  #print the user input


def generateLine(prevLine):
    thisLine = 2 * len(prevLine) * [0]  #initialize
    for i in range(len(prevLine)):
        parent = 0