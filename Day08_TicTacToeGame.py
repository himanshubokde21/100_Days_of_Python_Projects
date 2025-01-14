import random
import time 
def TicTacToe(US, CS):
    moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    board = [['_' for i in range(3)] for j in range(3)]
    user = com = []
    while True:
        for b in board: 
            print(b)
        while user not in moves or board[user[0]][user[1]] != '_':
            user = input('Enter your move (ex- 0, 1): ')
            user = list(int(i) for i in user.split(','))
            if board[user[0]][user[1]] != '_':
                print('already used! Enter again')
            elif user not in moves:
                print('Invalid move! Enter again')
        board[user[0]][user[1]] = US
        while com not in moves or board[com[0]][com[1]] != '_':
            if isFull(board):
                break
            com = random.choice(moves)
        print('computer\'s turn...', end='\r')
        time.sleep(1)
        print(' ' * 20, end='\r')
        print('computer\'s move is')
        board[com[0]][com[1]] = CS
        if Tie(board, US):
            break
        elif RowWin(board, US): 
            break
        elif ColWin(board, US): 
            break
        elif DigWin(board, US): 
            break

def RowWin(board, US):
    for r in board:
        if '_' in r: continue 
        if r[0] == r[1] and r[0] == r[2]:
            for b in board: print(b)
            if r[0] == US:
                print('<= User Won! =>')
            else:
                print('<= Computer Won =>')
            return True
    else:
        return False

def ColWin(board, US):
    for c in range(3):
        if '_' in [board[0][c], board[1][c], board[2][c]]: 
            continue 
        if board[0][c] == board[1][c] and board[0][c] == board[2][c]:
            for b in board: 
                print(b)
            if board[0][c] == US:
                print('<= User Won! =>')
            else:
                print('<= Computer Won =>')
            return True
    else: 
        return False

def DigWin(board, US):
    if '_' not in [board[0][0], board[1][1], board[2][2]]: 
        if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
            for b in board: 
                print(b)
            if board[1][1] == US:
                print('<= User Won! =>')
            else:
                print('<= Computer Won =>')
            return True
    
    elif '_' not in [board[0][2], board[1][1], board[2][0]]: 
        if board[0][2] == board[1][1] and board[0][2] == board[2][0]: 
            for b in board: 
                print(b)
            if board[1][1] == US:
                print('<= User Won! =>')
            else:
                print('<= Computer Won =>')
            return True
    else: 
        return False

def Tie(board, US):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_': 
                return False
    else: 
        for b in board: 
            print(b)
        print("<= It's tie! =>")
        return True

def isFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_': 
                return False
    else: 
        return True
    
if __name__ == '__main__':
    USym = input('choose symbol (x / o): ')
    while USym != 'x' and USym != 'o':
        USym = input('Invalid Symbol! choose again: ')
    if USym == 'x': 
        CSym = 'o'
    else: 
        CSym = 'x'
    TicTacToe(USym, CSym)
