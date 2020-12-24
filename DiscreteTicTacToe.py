# Connor Humiston
# Discrete Math
# AI and Tic Tac Toe

import random

def drawBoard(board):
    # This function prints the board
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

def playerLetterInput():
    # this function allows the player to type which letter they want
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Would you like to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, and the second is the AI's
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    # returns a list with the player's letter first and the AI's letter second

def firstPlay():
    # Randomly chooses which player goes first
    if random.randint(0, 1) == 0:
        return 'AI'
    else:
        return 'player'

def playAgain():
    print('Would you like to play again? (yes or no)')
    return input().lower().startswith('y')
    # This function returns True if the player input starts with y (aka yes) and False otherwise

def makeMove(board, letter, move):
    # places letter on the board
    board[move] = letter

def isWinner(board, letter):
    # passed the current board and a player's letter, this function returns True if that player has won
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # a win across the top (all top filled with letter)
    (board[4] == letter and board[5] == letter and board[6] == letter) or # a win across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # a win across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # a win down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # a win down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # a win down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # a win on the first diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # a win on the second diagonal

def getBoardCopy(board):
    # creates a duplicate of the board list and returns it
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '
    # returns true if the passed move is free, aka an empty space, on the board that is passed

def getPlayerMove(board):
    # allows the player to type in their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        # if the move is not in the given spaces or not free the selection line is reprinted and any proper input is returned
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMove(board, movesList):
    # returns a valid move from the passed move list on the board or none if no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i) # appends all the free spaces
    if len(possibleMoves) != 0: # if the number of possible moves is not zero
        return random.choice(possibleMoves) #randomly chooses one
    else:
        return None

def getAIMove(board, AILetter):
    # with a board and the AI's letter, determines best move and returns that move
    if AILetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # The AI algorithm:
    # first, checks if AI can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i): # if a space is free on the board
            makeMove(copy, AILetter, i) # letter placed in that spot
            if isWinner(copy, AILetter): # if the AI is theoretically the winner on board copy, 
                return i                 # then it returns that spot to play there

    # checks if the player could win on his next move to block them
    for i in range(1, 10): # looping through the possible spots
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i): # if the space is free
            makeMove(copy, playerLetter, i) # and letter in that spot
            if isWinner(copy, playerLetter): # if the player could win there,
                return i                     # then it returns that spot to block the opponent

    # otherwise the AI tries to take one of the corners first if they are free
    move = chooseRandomMove(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # then tries to take the center if it's free
    if isSpaceFree(board, 5):
        return 5

    # lastly, if no other spots open, makes move on one of the sides
    return chooseRandomMove(board, [2, 4, 6, 8])

def isBoardFull(board):
    # returns True if every space on the board has been taken and False otherwise
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # reseting the board
    theBoard = [' '] * 10
    playerLetter, AILetter = playerLetterInput() # player letter assigned to input
    turn = firstPlay() # the first turn is assigned to random variable
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True # let the games begin

    while gameIsPlaying:
        if turn == 'player':
            # for player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter): # first if the player is a winner after move made, prints and ends game
                drawBoard(theBoard)
                print('You win!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard): # if the board is full and not already a winner then it's a tie
                    drawBoard(theBoard)
                    print('The game is a tie.')
                    break
                else:
                    turn = 'AI' # otherwise it's the AI's turn

        else:
            # For AI's turn
            move = getAIMove(theBoard, AILetter)
            makeMove(theBoard, AILetter, move)

            if isWinner(theBoard, AILetter): # if the AI is the winner, prints and ends game
                drawBoard(theBoard)
                print('The AI has beaten you. You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard): # if not a winner and board full, then a tie
                    drawBoard(theBoard)
                    print('The game is a tie.')
                    break
                else:
                    turn = 'player' # otherwise back to the player

    if not playAgain(): # if play again is false then breaks
        break
