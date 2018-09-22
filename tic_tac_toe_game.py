
#2 players
#the board should be printed out every time a player makes a move.
#You should be able to accept input of the player position and then place a symbol on the board.


def printmatrix (myshots):
    
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


def playnow():

    print('Welcome to the real world!')

    while True: 
        
        print('Player 1: Do you wanna be X or O?')

        players = ['X','O']

        players[0] = input().upper()

        if players[0] == 'X':
            print('Player 1 will go first with {}.'.format(players[0]))
            break
        elif players[0] == 'O':
            players[1] = 'X'
            print('Player 1 will go first with {}.'.format(players[0]))
            break
        else:
            print('WFT X = equis ; O = es una o no cero')


    input('Are you ready to play? Press Enter.').upper()

    turns = 0
    myshots = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    printmatrix(myshots)

    while True:

        print('\nChoose your next position: (1-9)')

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
            if turns == 0:
                print('\nPlayer 2 won!')
            else:
                print('\nPlayer 1 won!')
            
            break
        




    print('Congratulations! You have won the game!\n\n')

    

playagain = True

while playagain == True:
    
    playnow()
    
    rplayagain = 'x'

    while rplayagain != 'yes' and rplayagain != 'no':

        print('Do you wanna play again? Enter Yes or No:')

        rplayagain = input().lower()

        if rplayagain == 'no':
            playagain = False
            print('\nBye!')
        elif rplayagain != 'yes':
            print('\nPlease only Yes or No')
            continue


