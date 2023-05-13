#Use this file to start games
from properties import Property, Station, Utility
from player import Player
from board import board, pos_prop, pos_stat, pos_util
import random

def pay_rent_prop(property: Property, player: Player) -> None:
    has_monopoly = property.has_monopoly(property.owned)
    rent = property.get_rent(has_monopoly)
    if rent > player.money:
        print(f"{player} is bankrupt! They cannot pay their rent.")
        player.bankrupt()
    else:
        player.money -= rent
        property.get_owner().money += rent

def pay_rent_stat(station: Station, player: Player) -> None:
    stat_owned = len(station.get_player_pairs(station.owned))
    rent = station.get_rent(stat_owned)
    if rent > player.money:
        print(f"{player} is bankrupt! They cannot pay their rent.")
        player.bankrupt()
    else:
        player.money -= rent
        station.get_owner().money += rent

def pay_rent_util(util: Utility, player: Player) -> None:
    utils_owned = len(util.get_player_pairs(util.owned))
    rent = util.get_rent(utils_owned)
    if rent > player.money:
        print(f"{player} is bankrupt! They cannot pay their rent.")
        player.bankrupt()
    else:
        player.money -= rent
        util.get_owner().money += rent


def on_property(property: Property, player: Player) -> None:
    """When moving onto a property, there is either the option to buy it if it is
    unowned or you pay rent if it is owned and the owner is not in Jail.
    """
    prop_owned = property.is_owned()
    owner = property.get_owner()
    if prop_owned and owner != player:
        print(f"You landed on {owner}'s property.")
        has_monopoly = property.has_monopoly(owner)
        if (not property.is_mortgaged()) and (not owner.in_jail):
            print(f"You must pay {owner} rent! The rent is {property.get_rent(has_monopoly)}.")
            pay_rent_prop(property, player)
        else:
            print('You do not have to pay rent to this owner.')
    elif prop_owned and owner == player:
        print('You own this property! Enjoy your stay.')
    else:
        print(f'{property} is unowned. Would you like to buy it?')
        #Takes input from player. I think if we want to make AI to play this has to be changed
        buy = input('Type Y and press Enter to buy. To decline, type N and press Enter')
        if buy == 'Y':
            print(f'{player} just bought {property}!')
            property.buy(player)
        else:
            print(f'You have chosen not to purchase this property. Thanks for staying at {property}.')

def on_station(station: Station, player: Player) -> None:
    """When moving onto a railroad, there is either the option to buy it if it is
    unowned or you pay rent if it is owned and the owner is not in Jail.
    """
    stat_owned = station.is_owned()
    owner = station.get_owner()
    if stat_owned and owner != player:
        print(f"You landed on {owner}'s railroad.")
        num_stat_owned = len(station.get_player_pairs(owner))
        if (not station.is_mortgaged()) and (not owner.in_jail):
            print(f"You must pay {owner} rent! The rent is {station.get_rent(num_stat_owned)}.")
            pay_rent_stat(station, player)
        else:
            print('You do not have to pay rent to this owner.')
    elif stat_owned and owner == player:
        print('You own this railroad! Enjoy your stay.')
    else:
        print(f'{station} is unowned. Would you like to buy it?')
        buy = input('Type Y and press Enter to buy. To decline, type N and press Enter')
        if buy == 'Y':
            print(f'{player} just bought {station}!')
            station.buy(player)
        else:
            print(f'You have chosen not to purchase this Railroad. Thanks for staying at {station}.')

def on_util(util: Utility, player: Player) -> None:
    """When moving onto a Utility, there is either the option to buy it if it is
    unowned or you pay rent if it is owned and the owner is not in Jail.
    """
    util_owned = util.is_owned()
    owner = util.get_owner()
    if util_owned and owner != player:
        print(f"You landed on {owner}'s railroad.")
        num_util_owned = len(util.get_player_pairs(owner))
        if (not util.is_mortgaged()) and (not owner.in_jail):
            print(f"You must pay {owner} rent! The rent is {util.get_rent(num_util_owned)}.")
            pay_rent_util(util, player)
        else:
            print('You do not have to pay rent to this owner.')
    elif util_owned and owner == player:
        print('You own this Utility!')
    else:
        print(f'{util} is unowned. Would you like to buy it?')
        buy = input('Type Y and press Enter to buy. To decline, type N and press Enter')
        if buy == 'Y':
            print(f'{player} just bought {util}!')
            util.buy(player)
        else:
            print(f'You have chosen not to purchase this Utility. Thanks for staying at {util}.')


def move(player: Player) -> bool:
    """Rolls 2 random dice and changes the position of the player.
       Return True if doubles were rolled, False if not"""
    curr_pos = player.position
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    new_pos = (curr_pos + dice1 + dice2) % 40
    player.set_pos(new_pos)
    if dice1 == dice2:
        return True
    else:
        return False
    




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