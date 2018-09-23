

# from IPython.display import clear_output

import os

def playernames():
    
    playernames = {'player1':'none1', 'player1score':0, 'player2':'none2', 'player2score':0, }

    playernames['player1'] = input('\nPlayer 1: what is your name son?: ').capitalize()
    playernames['player2'] = input('\nPlayer 2: what is your name son?: ').capitalize()

    return playernames


def getplayers(playernames):

    players_xd = ['X','O']

    while True: 
            
        

        players_xd[0] = input('\n{}: Do you wanna be X or O?: '.format(playernames['player1'])).upper()

        if players_xd[0] == 'X':
            print('\nReady, {} will go first with {}.'.format(playernames['player1'],players_xd[0]))
            break
        elif players_xd[0] == 'O':
            players_xd[1] = 'X'
            print('\nReady, {} will go first with {}.'.format(playernames['player1'],players_xd[0]))
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


def win_check(myshots,turns,playernames):
    
    
    if (myshots[0] == myshots[1] == myshots[2] and myshots[1] != ' ') or \
        (myshots[3] == myshots[4] == myshots[5] and myshots[4] != ' ') or \
        (myshots[6] == myshots[7] == myshots[8] and myshots[7] != ' ') or \
        (myshots[0] == myshots[3] == myshots[6] and myshots[6] != ' ') or \
        (myshots[1] == myshots[4] == myshots[7] and myshots[4] != ' ') or \
        (myshots[2] == myshots[5] == myshots[8] and myshots[5] != ' ') or \
        (myshots[0] == myshots[4] == myshots[8] and myshots[4] != ' ') or \
        (myshots[2] == myshots[4] == myshots[6] and myshots[4] != ' '):
            
        printmatrix(myshots)

        if turns == 0:
            print('Congratulations {}! You have won the game!\n\n'.format(playernames['player2']))
            playernames['player2score'] += 1
        else:
            print('Congratulations {}! You have won the game!\n\n'.format(playernames['player1']))
            playernames['player1score'] += 1
            
        return True
    
    elif ' ' not in myshots:
        printmatrix(myshots)
        print('\nThe game was Even!')
        return True
        



def playnow(players,player_names):

    turns = 0
    shotss = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    printmatrix(shotss)

    while True:

        if (turns == 0):
            print('\n{} Choose your next position: (1-9)'.format(player_names['player1']))
        else:
            print('\n{} Choose your next position: (1-9)'.format(player_names['player2']))
        
        place = 0
        
        while True:
            try:
                place = int(input())   
            except ValueError:
                print('Only numbers between 1-9!!')
            else:
                if place in range(1,10):
                    break 
                else:
                    print('Only numbers between 1-9!!')

        if shotss[place-1] == ' ':
            shotss[place-1] = players[turns]
            
            printmatrix(shotss)

            if turns == 0:
                turns = 1
            else:
                turns = 0

        else:
            print('Oliii!.. that cell is used')

        

        if win_check(shotss,turns,player_names):
            break




os.system('clear')
#clear_output()
    
print('Neo... welcome to the real world.')

player_names = playernames()

players_chars = getplayers(player_names)

input('\nAre you ready to play?\nPress Enter.').upper()


rplayagain = 'x'

while rplayagain != 'no':
    
    playnow(players_chars,player_names)

    rplayagain = 'x'

    print('Scores:')
    print('{}: {}'.format(player_names['player1'],player_names['player1score']))
    print('{}: {}\n'.format(player_names['player2'],player_names['player2score']))

    while rplayagain != 'yes' and rplayagain != 'no':



        rplayagain = input('Do you wanna play again? Enter Yes or No:').lower()

        if rplayagain != 'yes' and rplayagain != 'no':
            print('\nPlease only Yes or No')
    
        

print('\nBye!')
