
def drawBoard(board,s):
    x=0
    print ('Column:', end='')
    for i in range(0, s):
        print('{:^5}'.format(str(i+1)), end='')
    print()
    for i in range (0,s):
        print ('Row'+ str(i+1)+ ': ', end='|')
        for j in range (0,s):
            print ('{:^4}'.format(str(board[i][j])), end='|')
        print ()
        print ('      ', end='')
        print ('|'+'-----'*(s-1) + '----' +'|')
        x=x+s

size = int(input("Size of grid?(X * X)"))
streak = int(input("Length to win?(X * X)"))
board=[['-' for i in range (0,size)]for j in range(0,size)]

drawBoard(board,size)

def XMove():
    x = [None] * 2
    print('Player1:')
    x[0] = int(input("Column to put X?"))
    x[1] = int(input("Row to put X?"))
    return x

def OMove():
    o = [None] * 2
    print('Player2:')
    o[0] = int(input("Column to put O?"))
    o[1] = int(input("Row to put O?"))
    return o

def check_rows(board, size, streak, i):
    Ostreak = 0
    Xstreak = 0
    win = [-1] * 2

    for j in range(0, size):
        if (board[i][j] == '-'):
            Ostreak = 0
            Xstreak = 0

        if (board[i][j] == 'O'):
            Ostreak = Ostreak + 1
            Xstreak = 0

        if (board[i][j] == 'X'):
            Xstreak = Xstreak + 1
            Ostreak = 0

        if (Xstreak == streak):
            win[0] = i
            return win
        if (Ostreak == streak):
            win[1] = i
            return win
    return win



def check_columns(board, size, streak, i):
    Ostreak = 0
    Xstreak = 0
    win = [-1]*2

    for j in range(0, size):
        if (board[j][i] == '-'):
            Ostreak = 0
            Xstreak = 0

        if (board[j][i] == 'O'):
            Ostreak = Ostreak + 1
            Xstreak = 0

        if (board[j][i] == 'X'):
            Xstreak = Xstreak + 1
            Ostreak = 0

        if (Xstreak == streak):
            win[0]=i
            return win
        if (Ostreak == streak):
            win[1]=i
            return win
    return win

def AI(board, size, streak):
    vb = board
    scoreboard=[[0 for i in range (0,size)]for j in range(0,size)]
    for i in range (0,size):
        for j in range (0,size):

            if board[i][j] == '-':
                vb[i][j] = 'O'
                ro = (check_rows(vb, size, streak, i))
                col = (check_columns(vb, size, streak, i))
                if (ro[1] != -1):
                    drawBoard(vb, size)
                    print('Player 2 Wins! ROW ' + str(ro[1] + 1))
                    exit()
                if (col[1] != -1):
                    drawBoard(vb, size)
                    print('Player 2 Wins! COLUMN ' + str(col[1] + 1))
                    exit()
                vb[i][j] = '-'
    # for i in range(0, size):
    #     for j in range(0, size):
    #         if board[i][j] == '-':
    #             vb[i][j] = 'X'
    #             ro = (check_rows(vb, size, streak, i))
    #             col = (check_columns(vb, size, streak, i))
    #
    #             if (ro[0] != -1):
    #                 print('Player 1 almost wins @ ROW ' + str(ro[0] + 1))
    #                 board[i][j] = 'O'
    #
    #                 return board
    #             if (col[0] != -1):
    #                 print('Player 1 almost wins @ COLUMN ' + str(col[0] + 1))
    #                 board[i][j] = 'O'
    #
    #                 return board
    #             # if not won, or blocked, then (for now) AI places @ first vacant space
    # for i in range(0, size):
    #     for j in range(0, size):
    #         if vb[i][j] == '-':
    #             board[i][j] = 'O'
    #             return board

            ro = (check_rows(board, size, streak-1, i))
            col = (check_columns(board, size, streak-1, i))
            if (ro[0] != -1):
                print('Almost in row ' + str(ro[0] + 1))
                for i in range (0,size):
                    if board[ro[0]][i] == '-':
                        board[ro[0]][i] = 'O'
                        return board
            if (col[0] != -1):
                print('Almost in column ' + str(col[0] + 1))
                for i in range (0,size):
                    if board[i][col[0]] == '-':
                        board[i][col[0]] = 'O'
                        return board

            ro = (check_rows(board, size, streak - 2, i))
            col = (check_columns(board, size, streak - 2, i))
            if (ro[0] != -1):
                print('-2 in row ' + str(ro[0] + 1))
                for i in range(0, size):
                    if board[ro[0]][i] == '-':
                        board[ro[0]][i] = 'O'
                        return board
            if (col[0] != -1):
                print('-2 in column ' + str(col[0] + 1))
                for i in range(0, size):
                    if board[i][col[0]] == '-':
                        board[i][col[0]] = 'O'
                        return board
    # if ai can't win, or block, then it places @ first vacant space
    for i in range(0, size):
        for j in range(0, size):
            if board[i][j] == '-':
                board[i][j] = 'O'
                return board


    return board


while True:
    #Player 1 chooses place (X)
    while True:
        MX = XMove()
        if (board [MX[1]-1][MX[0]-1] == '-'):
            break
        else:
            print ('Place taken!')
    board [MX[1]-1][MX[0]-1] = 'X'
    drawBoard(board,size)
    for i in range (0,size):
        ro = (check_rows(board, size, streak, i))
        col = (check_columns(board, size, streak, i))
        if (ro[0] != -1):
            print('Player 1 Wins! ROW '+str(ro[0]+1))
            exit()
        if (col[0] != -1):
            print ('Player 1 Wins! COLUMN '+str(col[0]+1))
            exit()

    board = AI(board, size, streak)
    drawBoard(board, size)
    for i in range(0, size):
        ro = (check_rows(board, size, streak, i))
        col = (check_columns(board, size, streak, i))
        if (ro[1] != -1):
            print('Player 2 Wins! ROW ' + str(ro[1] + 1))
            exit()
        if (col[1] != -1):
            print('Player 2 Wins! COLUMN ' + str(col[1] + 1))
            exit()

    #Player 2 chooses place (O)

    # while True:
    #     OX = OMove()
    #     if (board[OX[1] - 1][OX[0] - 1] == '-'):
    #         break
    #     else:
    #         print ('Place taken!')
    # board[OX[1] - 1][OX[0] - 1] = 'O'
    # drawBoard(board, size)
    # for i in range(0, size):
    #     ro = (check_rows(board, size, streak, i))
    #     col = (check_columns(board, size, streak, i))
    #     if (ro[1] != -1):
    #         print('Player 2 Wins! ROW ' + str(ro[1] + 1))
    #         exit()
    #     if (col[1] != -1):
    #         print('Player 2 Wins! COLUMN ' + str(col[1] + 1))
    #         exit()


    #AI?!

