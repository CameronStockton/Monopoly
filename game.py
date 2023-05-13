#Use this file to start games
from properties import Property, Station, Utility
from player import Player
from board import board, pos_prop, pos_stat, pos_util
from actions import pay_rent_prop, pay_rent_stat, pay_rent_util, on_property, on_station, on_util, move
import random



# Create players
num_players = int(input("Enter number of players (2-4): "))
players = []
for i in range(num_players):
    players.append(Player(i+1))


#Actual Game Loop
game_over = False
while not game_over:
    for player in players:
        end_turn = False
        while not end_turn:
            print(f"\n{player}'s turn")
            player_move = move(player)
            if player.position in pos_prop:
                #Moved onto property
                on_property(board[player.position], player)
                end_turn = True
            elif player.position in pos_stat:
                #Moved onto station
                on_station(board[player.position], player)
                end_turn = True
            elif player.position in pos_util:
                #Moved onto utility
                on_util(board[player.position], player)
                end_turn = True
            elif board[player.position] == 'Go':
                #Moved onto Go
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            elif board[player.position] == 'Community Chest':
                #Moved onto Community Chest
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            elif board[player.position] == 'Income Tax':
                #Moved onto Income Tax
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            elif board[player.position] == 'Chance':
                #Moved onto Chance
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            elif board[player.position] == 'Jail':
                #Moved onto Jail
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            elif board[player.position] == 'Free Parking':
                #Moved onto Free Parking
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            elif board[player.position] == 'Go To Jail':
                #Moved onto Go To Jail
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            elif board[player.position] == 'Luxury Tax':
                #Moved onto Luxury Tax
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True
            else:
                #Are there any other options we should catch?
                print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                end_turn = True

            #After a players turn, lets first check if they are bankrupt to end their turn.
            #Then we check to see if they rolled doubles, if they did not then we end their turn
            if player_move:
                end_turn = False

            if player.is_bankrupt:
                end_turn = True

    #After every player has their turn, the game needs to check if anyone is bankrupt, then it checks
    #if the game is over
    for player in players:
        if player.is_bankrupt:
            players.remove(player)
    
    if len(players) == 1:
        print(f"{players[0]} has won the game with ${players[0].money}!")
        game_over = True