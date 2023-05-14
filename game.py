#Use this file to start games
from properties import Property, Station, Utility
from player import Player
from board import board, pos_prop, pos_stat, pos_util
from actions import pay_rent_prop, pay_rent_stat, pay_rent_util, on_property, on_station, on_util, move, on_go, on_inctax, on_luxtax, on_freepark, on_gojail, on_justvisit
import random



# Create players
num_players = int(input("Enter number of players (2-4): "))
players = []
for i in range(num_players):
    players.append(Player(i+1))


#Actual Game Loop
game_over = False
while not game_over:
    print("================================================================")
    for player in players:
        end_turn = False
        if not player.in_jail:
            #This is what happens when the player is not in jail
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
                    on_go(player)
                    end_turn = True
                elif board[player.position] == 'Community Chest':
                    #Moved onto Community Chest
                    print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                    end_turn = True
                elif board[player.position] == 'Income Tax':
                    #Moved onto Income Tax
                    on_inctax(player)
                    end_turn = True
                elif board[player.position] == 'Chance':
                    #Moved onto Chance
                    print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                    end_turn = True
                elif board[player.position] == 'Just Visiting':
                    #Moved onto Just Visiting
                    on_justvisit(player)
                    end_turn = True
                elif board[player.position] == 'Free Parking':
                    #Moved onto Free Parking
                    on_freepark(player)
                    end_turn = True
                elif board[player.position] == 'Go To Jail':
                    #Moved onto Go To Jail
                    on_gojail(player)
                    end_turn = True
                elif board[player.position] == 'Luxury Tax':
                    #Moved onto Luxury Tax
                    on_luxtax(player)
                    end_turn = True
                else:
                    #Are there any other options we should catch?
                    print(f'You landed on {board[player.position]}. Unfortunately, I have not coded this part yet!')
                    end_turn = True
            else:
                #This is what happens when the player is in jail
                if player.time_jail == 3:
                    player.get_out_jail()
                    end_turn = False
                else:
                    print(f"{player} is in Jail!")
                    roll_or_fine = input("Type P to pay the fine, type anything to Roll then press Enter.")
                    if roll_or_fine == "P":
                        print(f"{player} has paid the fine.")
                        player.get_out_jail()
                        player.money -= 75
                        end_turn = False
                    else:
                        dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
                        print(f"{player} has rolled a {dice1} and {dice2}")
                        if dice1 == dice2:
                            print(f"{player} rolled doubles! They get out of jail")
                            player.get_out_jail()
                            end_turn = False
                        else:
                            player.night_in_jail()
                            end_turn = True

            print(f"{player} has ${player.money}!")
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