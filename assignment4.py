import sys
from collections import deque
from operator import eq
def showMatrix(mainboard):
    for i in mainboard:
        for j in i:
            print(j+" ",end="")
        print()

def checkForEnd(mainboard):
    a = 0
    for i in range(1,len(mainboard)-1):
        for j in range(1,len(mainboard[0])-1):
            up = mainboard[i-1][j]
            down = mainboard[i+1][j]
            right = mainboard[i][j+1]
            left = mainboard[i][j-1]
            if(mainboard[i][j] != " "):
                if(mainboard[i][j] == up or mainboard[i][j] == down or mainboard[i][j] == right or mainboard[i][j] == left):
                    a = 1

    if mainboard[0][0] != " " and (mainboard[0][0] == mainboard[0][1] or mainboard[0][0] == mainboard[1][0]):
        a = 1
    elif mainboard[-1][0] != " " and (mainboard[-1][0] == mainboard[-1][1] or mainboard[-1][0] == mainboard[-2][0]):
        a = 1
    elif mainboard[0][-1] != " " and (mainboard[0][-1] == mainboard[0][-2] or mainboard[0][-1] == mainboard[1][-1]):
        a = 1
    elif mainboard[-1][-1] != " " and (mainboard[-1][-1] == mainboard[-1][-2] or mainboard[-1][-1] == mainboard[-2][-1]):
        a = 1
    return a
file = open(sys.argv[1],"r").read().split("\n")
mainboard = []

def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
for i in file:
    mainboard.append(i.split(" "))
a = checkForEnd(mainboard)
showMatrix(mainboard)
print()
print("Your score is:0")
print()
scored = 0
def slideUpDown(col):
        temp = ""
        checkEmptyCol = True
        for i in range(len(mainboard)-1):
            if (mainboard[i][col] != " " and mainboard[i+1][col] == " "):
                temp = mainboard[i][col]
                mainboard[i][col] = mainboard[i+1][col]
                mainboard[i+1][col] = temp
                slideUpDown(col)
        temp2 = ""
        for j in range(len(mainboard)):
            if (mainboard[j][col] != " "):
                checkEmptyCol = False
        if(checkEmptyCol == True):
            for k in range(len(mainboard)):
                for m in range(col,len(mainboard[0])-1):
                    temp2 = mainboard[k][m]
                    mainboard[k][m] = mainboard[k][m+1]
                    mainboard[k][m+1] = temp2
while(a == 1):

    def main(mainboard,scored):

        neighbors = (-1, 0), (0, +1), (+1, 0), (0, -1)
        row, col = input("Enter two numbers here: ").split()
        print()
        row = int(row)-1
        col = int(col)-1
        start = row , col
        similar = eq
        if mainboard[row][col] == " ":
            print("Please enter a correct size!")
            print()
            row, col = input("Please enter a row and column number: ").split()
            print()
            row = int(row)-1
            col = int(col)-1
            start = row , col
        head = int(mainboard[row][col])
        tuple = list(find_similar(mainboard, neighbors, start, similar, 'BFS'))

        if (len(tuple) > 1):
            scored = scored + head*rec_fib(len(tuple))
        print("Your score is:{}".format(scored))
        return scored


    def find_similar(array, neighbors, start, similar, mode):
        match = get_item(array, start)
        block = {start}
        visit = deque(block)
        child = dict(BFS=deque.popleft, DFS=deque.pop)[mode]
        while visit:
            node = child(visit)
            for offset in neighbors:
                index = get_next(node, offset)
                if index not in block:
                    block.add(index)
                    if is_valid(array, index):
                        value = get_item(array, index)
                        if similar(value, match):
                            visit.append(index)
                            mainboard[start[0]][start[1]] = " "
                            mainboard[index[0]][index[1]] = " "
            yield node
    def get_item(array, index):
        row, column = index
        return array[row][column]


    def get_next(node, offset):
        row, column = node
        row_offset, column_offset = offset
        return row + row_offset, column + column_offset


    def is_valid(array, index):
        row, column = index
        return 0 <= row < len(array) and 0 <= column < len(array[row])
    scored = main(mainboard,scored)


    for i in range(len(mainboard[0])):
        slideUpDown(i)
    showMatrix(mainboard)
    print()

    a = checkForEnd(mainboard)
if ( a == 0):
    print("Game over")
