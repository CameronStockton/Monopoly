from board import board
from properties import Property, Station, Utility
import random

#Test moving around board
pos = 0
print(f'You are currently on {board[pos]}')
i = 0
while i < 10:
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    print(f'You rolled a {dice1} and {dice2}')
    pos = (pos + dice1 + dice2) % 40
    print(f'Now you are on {board[pos]}')
    if type(board[pos]) == Property:
        print('This is a property!')
    elif type(board[pos]) == Station:
        print('This is a railroad!')
    elif type(board[pos]) == Utility:
        print('This is a utility!')
    else:
        print(f'This is the {board[pos]} square.')
    i += 1
