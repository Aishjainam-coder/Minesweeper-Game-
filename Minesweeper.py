import numpy as np

row = 4
column = 4
bombCount = 5
NONbombcount = row * column - bombCount

array = np.random.randint(1, size=(row, column))
covers = np.random.randint(1, size=(row, column))
i = 0
while i < bombCount:

    bombrow = np.random.randint(0, row)
    bombcolumn = np.random.randint(0, column)
    # print("BR",bombrow)
    # print("Bcoul",bombcolumn)
    if array[bombrow, bombcolumn] != 88:
        array[bombrow, bombcolumn] = 88
        i += 1
# print("i",i)
# print("BC",bombCount)
# print(array)

print(array)
for i in range(row):
    for j in range(column):
        if array[i, j] != 88:
            nbombCount = 0
            # print("bc", nbombCount)
            for p in range(max(i - 1, 0), min(row, i + 2)):
                for q in range(max(0, j - 1), min(column, j + 2)):
                    if array[p, q] == 88:
                        nbombCount = nbombCount + 1
            array[i, j] = nbombCount

print(array)


def printboard():
    for i in range(row):
        strm = " "
        for j in range(column):
            if covers[i, j] == -2:
                strm = strm + "F "
            elif covers[i, j] == 0:
                strm = strm + "# "
            else:
                strm = strm + str(array[i, j]) + " "
        print(strm)
    print()


printboard()

Gameover = False
NONbombcounter = 0
while Gameover == False:
    x = int(input("enter x="))
    y = int(input("enter y="))
    print(x, y)
    print("enter type of click, 1=left ,2 =right")
    m = int(input())
    if m == 1:
        print("left")
    else:
        print("right")

    if m != 1:
        covers[x, y] = -2
        printboard()
    elif array[x, y] == 88:
        covers[x, y] = -1
        printboard()
        Gameover = True
        print("GAME OVER ")
    else:
        covers[x, y] = -1
        printboard()
        NONbombcounter = NONbombcounter + 1
        if NONbombcounter == NONbombcount:
            Gameover = True
            print("HURRAY U WON")
        else:
            print("GAME conitnue")
