def dispalyInstructions():
    print("Use the numbers indicated in each space to make your mark")
    print('     |     |     ')
    print('  7  |  8  |  9  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  4  |  5  |  6  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  1  |  2  |  3  ')
    print('     |     |     ')
    print('\n------------------\n')

def displayBoard(board):
    #this function prints out the board that it was passed
    #"board is a list of 10 strings representing the board
    print('The game board:')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')

def getplayermove(board,player):
    #let the player type in his move
    move=''
    while (move not in '1 2 3 4 5 6 7 8 9'.split()) or (board[int(move)]!=''):
        move=input("What is {} next move? (1-9): ".format(player))
        return int(move)

def checkwin(board,letter):
    #given a board and a player's letter, this func returns True if player has won
    win=False
    if board[7]==letter and board[8]==letter and board[9]==letter: #across top
        win=True
    elif board[4]==letter and board[5]==letter and board[6]==letter: #across mid
        win=True
    elif board[1]==letter and board[2]==letter and board[3]==letter: #across bottom
        win=True
    elif board[7]==letter and board[4]==letter and board[1]==letter: #down left
        win=True
    elif board[8]==letter and board[5]==letter and board[2]==letter: #down mid
        win=True
    elif board[9]==letter and board[6]==letter and board[3]==letter: #down right
        win=True
    elif board[1]==letter and board[5]==letter and board[9]==letter: #diagnal right
        win=True
    elif board[3]==letter and board[5]==letter and board[1]==letter:  #diagnal left
        win=True
    return win

def isboardfull(board):
    #return true if every space on the board is taken
    for i in range(1,10):
        if board[i]==' ':
            return False
    return True

def playervalidation(name):
    if name== '' or (name.isalpha()==False):
        print("Please enter a valid name!")
        return False
    return True

def main():
    print("Welcome to Tic Tac Toe")
    dispalyInstructions()
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    displayBoard(board)
    print("Player 1 will use X")
    print("Plater 2 will use O")
    player1 = ''
    player2 = ''
    while playervalidation(player1)!= True:
        player1 = input("What is the name of player 1: ")        
    while playervalidation(player2)!= True:
        player2 = input("What is the name of player 2: ")
    turn=eval(input("Which player will go first [1/2]? "))

    gameplaying=True
    while gameplaying:
        if turn==1:   #player 1 turn
            print("{}'s turn".format(player1))
            displayBoard(board)
            move=getplayermove(board,player1)
            board[move]='X'

            #check win
            if checkwin(board,'X'):
                displayBoard(board)
                print("{} won!".format(player1))
                gameplaying=False
            else:
                if isboardfull(board):
                    displayBoard(board)
                    print("It is a tie!")
                    break
                else:
                    turn=2
                    
        else: #plater 2 turn
            print("{}'s turn".format(player2))
            displayBoard(board)
            move=getplayermove(board,player2)
            board[move]='O'

            #check win
            if checkwin(board,'O'):
                displayBoard(board)
                print("{} won!".format(player2))
                gameplaying=False
            else:
                if isboardfull(board):
                    displayBoard(board)
                    print("It is a tie!")
                    break
                else:
                    turn=1

main()
            
            







    
