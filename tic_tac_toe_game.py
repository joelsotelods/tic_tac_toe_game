
#2 players
#the board should be printed out every time a player makes a move.
#You should be able to accept input of the player position and then place a symbol on the board.

# from IPython.display import clear_output

import os

def getplayers():

    while True: 
            
        print('Player 1: Do you wanna be X or O?')

        players_xd = ['X','O']

        players_xd[0] = input().upper()

        if players_xd[0] == 'X':
            print('Player 1 will go first with {}.'.format(players_xd[0]))
            break
        elif players_xd[0] == 'O':
            players_xd[1] = 'X'
            print('Player 1 will go first with {}.'.format(players_xd[0]))
            break
        else:
            print('WFT X = equis ; O = es una o no cero')
    
    return players_xd




def printmatrix (myshots):
    
    #clear_output()
    os.system('clear')

    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(myshots[0],myshots[1],myshots[2]))
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(myshots[3],myshots[4],myshots[5]))
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(myshots[6],myshots[7],myshots[8]))
    print('     |     |     ')



def playnow(players):

    turns = 0
    myshots = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    printmatrix(myshots)

    while True:

        print('\nPlayer #{} Choose your next position: (1-9)'.format(turns+1))

        place = int(input())

        if place in range(1,10) and myshots[place-1] == ' ':
            myshots[place-1] = players[turns]
            
            printmatrix(myshots)

            if turns == 0:
                turns = 1
            else:
                turns = 0
            
        elif myshots[place-1] != ' ':
            print('Motherfucker.. that cell is used')
        else:
            print('Only numbers between 1-9!!')
        


        if (myshots[0] == myshots[1] and myshots[1] == myshots[2] and myshots[1] != ' ') or (myshots[3] == myshots[4] and myshots[4] == myshots[5] and myshots[4] != ' ') or (myshots[6] == myshots[7] and myshots[7] == myshots[8] and myshots[7] != ' ') or (myshots[0] == myshots[3] and myshots[3] == myshots[6] and myshots[6] != ' ') or (myshots[1] == myshots[4] and myshots[4] == myshots[7] and myshots[4] != ' ') or (myshots[2] == myshots[5] and myshots[5] == myshots[8] and myshots[5] != ' ')  or (myshots[0] == myshots[4] and myshots[4] == myshots[8] and myshots[4] != ' '):
            
            printmatrix(myshots)
            if turns == 0:

                print('Congratulations Player 2! You have won the game!\n\n')
            else:

                print('Congratulations Player 1! You have won the game!\n\n')
            
            break
        elif myshots[0] != ' ' and myshots[1] != ' ' and myshots[2] != ' ' and myshots[3] != ' ' and myshots[4] != ' ' and myshots[5] != ' ' and myshots[6] != ' ' and myshots[7] != ' ' and myshots[8] != ' ':

            printmatrix(myshots)
            
            print('\nThe game was Even!')
            break




os.system('clear')
#clear_output()
    
print('Welcome to the real world!')

players_chars = getplayers()

input('Are you ready to play? Press Enter.').upper()




while True:
    
    playnow(players_chars)
    
    rplayagain = 'x'

    while rplayagain != 'yes' and rplayagain != 'no':

        rplayagain = input('Do you wanna play again? Enter Yes or No:').lower()

        if rplayagain == 'no':
            print('\nBye!')
            break
    
        elif rplayagain != 'yes':
            print('\nPlease only Yes or No')
            continue


