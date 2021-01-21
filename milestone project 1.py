#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def displayboard(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


#board display test
testinput = [' ']*10
displayboard(testinput)


# In[3]:


def playerinput():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[4]:


def placemarker(board, marker, position):
    board[position]=marker


# In[5]:


def wincheck(board,marker):
    
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[1] == marker and board[2] == marker and board[3] == marker) or
    (board[7] == marker and board[4] == marker and board[1] == marker) or
    (board[8] == marker and board[5] == marker and board[2] == marker) or
    (board[9] == marker and board[6] == marker and board[3] == marker) or
    (board[7] == marker and board[5] == marker and board[3] == marker) or
    (board[9] == marker and board[5] == marker and board[1] == marker))


# In[6]:


import random

def choosefirst():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[7]:


def spacecheck(board, position):
    
    return board[position] == ' '


# In[8]:


def fullboard(board):
    for i in range(1,10):
        if spacecheck(board, i):
            return False
    return True


# In[9]:


def playerchoice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not spacecheck(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[10]:


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[12]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = playerinput()
    turn = choosefirst()
    print(turn + ' will go first.')
    
    playgame = input('Are you ready to play? Enter Yes or No.')
    
    if playgame.lower()[0] == 'y':
        gameon = True
    else:
        gameon = False

    while gameon:
        if turn == 'Player 1':
            # Player1's turn.
            
            displayboard(theBoard)
            position = playerchoice(theBoard)
            placemarker(theBoard, player1_marker, position)

            if wincheck(theBoard, player1_marker):
                displayboard(theBoard)
                print('Congratulations! You have won the game!')
                gameon = False
            else:
                if fullboard(theBoard):
                    displayboard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            displayboard(theBoard)
            position = playerchoice(theBoard)
            placemarker(theBoard, player2_marker, position)

            if wincheck(theBoard, player2_marker):
                displayboard(theBoard)
                print('Player 2 has won!')
                gameon = False
            else:
                if fullboard(theBoard):
                    displayboard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:













# In[ ]:




