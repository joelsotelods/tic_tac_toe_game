
#2 players
#the board should be printed out every time a player makes a move.
#You should be able to accept input of the player position and then place a symbol on the board.

print('Welcome to the real world!')
print('Player 1: Do you wanna be X or O?')


playerone = input().upper()

if playerone == 'X' or playerone == 'O':
    print('Player 1 will go first.')
else:
    print('WFT')

print('Are you ready to play? Enter Yes or No.')

print('Choose your next position: (1-9)')

print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('-----------------')
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('-----------------')
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))
print('  {}  |  {}  |  {}  '.format('X','Y','Z'))


print('Congratulations! You have won the game!')

print('Do you wanna play again? Enter Yes or No:')
