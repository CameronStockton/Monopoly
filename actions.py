#roll dice, move character (include a "to" option for stuff like "go directly to jail")
#pay rent, give money, buy property, end turn, pass go

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