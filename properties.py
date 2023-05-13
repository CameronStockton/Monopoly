#Info about properties here
from typing import Optional, Tuple, List
from player import Player
import random

class Property:
    """A property card
    
    Each card has multiple different features. 
    
    === Public Attributes ===
    id: the card id
    name: name of the property
    cost: how much the player must pay to purchase the property
    rent: how much the player collects from owning the property when 
          someone else lands on it. This depends on how many houses are
          on the property at the time.
    num_houses: number of houses. 5 indicates a hotel
    building_cost: how much each building costs
    mortgage_value: how much money the player gets back when mortgaging
    mortgaged: whether the property is currently mortgaged
    buyback_cost: how much to buy back the house once mortgaged
    owned: id of the player who owns the property. If unowned, value is 0
    pair: which cards are also paired with this card. this is important
          because you need the full set to build houses"""
    id: id
    name: str
    cost: int
    rent: Tuple[int, int, int, int, int, int]
    num_houses: int
    building_cost: int
    mortgage_value: int
    mortgaged: int
    buyback_cost: int
    owned: Optional[Player]
    pair: Optional[List]

    def __init__(self, id: int, name: str, cost: int, rent: Tuple[int, int, int, int, int, int],
                 building_cost: int, mortgage_value: int, buyback_cost: int, 
                 pair: Optional[List]) -> None:
        """Initialize this card with static details"""
        self.id = id
        self.name = name
        self.cost = cost
        self.rent = rent
        self.building_cost = building_cost
        self.mortgage_value = mortgage_value
        self.buyback_cost = buyback_cost
        self.pair = pair

        self.num_houses = 0
        self.mortgaged = 0
        self.owned = None
        

    def __str__(self) -> str:
        return self.name

    def is_owned(self) -> bool:
        """Checks if the property is owned (used for buying/paying rent)"""
        if self.owned == None:
            return False
        else:
            return True
    
    def add_property(self, player: Player) -> None:
        player.properties.append(self)
        print(f"{player} just bought {self}")

    def buy(self, player: Player) -> None:
        """Sets the new owner of the card based on player buying"""
        if player.money < self.cost:
            print(f"{player} does not have enough money to buy {self}.")
        else:
            player.money -= self.cost
            self.add_property(player)
            self.owned = player
        

    def get_owner(self) -> Optional[Player]:
        """Returns the owner if there is one. if not, returns Player"""
        return self.owned
    
    def mortgage(self) -> int:
        """Set mortgaged status to 1 and return the mortgage cost"""
        self.mortgaged = 1
        return self.mortgage_value
    
    def buyback(self) -> int:
        """Set mortgaged status to 0 and returns the buyback cost"""
        self.mortgaged = 0
        return self.buyback_cost
    
    def is_mortgaged(self) -> bool:
        """Checks if the property is mortgaged (useful for paying rent)"""
        if self.mortgaged == 0:
            return False
        else:
            return True
    
    def get_rent(self, monopoly) -> int:
        """Returns the value of rent need to be paid if landed on"""
        if monopoly and self.num_houses == 0:
            return self.rent[0] * 2
        else:
            return self.rent[self.num_houses]

    def buy_house(self, player, num_to_buy) -> int:
        """"Buys inputted number of houses and returns price"""
        if player == self.get_owner():
            if num_to_buy > 0 and (self.num_houses + num_to_buy) <= 5:
                self.num_houses += num_to_buy
                return (self.building_cost * num_to_buy)
            else:
                print("You can't do that!")
                return 0
        else:
            print(f"You do not own {self}")

    def has_monopoly(self, player: Player) -> bool:
        """Returns True or False if a player has a monopoly"""
        player_pairs = []
        pairs_to_search = self.pair
        for property in player.properties:
            if property in pairs_to_search:
                player_pairs.append(property)

        if len(player_pairs) == len(pairs_to_search):
            return True
        else:
            return False
        
    
class Station:
    """A Train Station card
    
    Each card has multiple different features. 
    
    === Public Attributes ===
    id: the card id
    name: name of the station
    cost: how much the player must pay to purchase the station
    rent: how much the player collects from owning the station when 
          someone else lands on it. This depends on how many stations are
          owned by the same player
    mortgage_value: how much money the player gets back when mortgaging
    buyback_cost: how much to buy back the house once mortgaged
    owned: id of the player who owns the property. If unowned, value is 0
    pair: which cards are also paired with this card. this is important
          because you need the full set to build houses"""
    id: int
    name: str
    cost: int
    rent: Tuple[int, int, int, int]
    mortgage_value: int
    mortgaged: int
    buyback_cost: int
    owned: Optional[Player]
    pair: Optional[List]

    def __init__(self, id: int, name: str, cost: int, rent: Tuple[int, int, int, int],
                 mortgage_value: int, buyback_cost: int, pair: Optional[List]) -> None:
        """Initialize this card with static details"""
        self.id = id
        self.name = name
        self.cost = cost
        self.rent = rent
        self.mortgage_value = mortgage_value
        self.buyback_cost = buyback_cost
        self.pair = pair

        self.mortgaged = 0
        self.owned = None
        

    def __str__(self) -> str:
        return self.name

    def is_owned(self) -> bool:
        """Checks if the station is owned (used for buying/paying rent)"""
        if self.owned == None:
            return False
        else:
            return True
    
    def add_station(self, player: Player) -> None:
        player.properties.append(self)
        print(f"{player} just bought {self}")

    def buy(self, player: Player) -> None:
        """Sets the new owner of the card based on player buying"""
        if player.money < self.cost:
            print(f"{player} does not have enough money to buy {self}.")
        else:
            player.money -= self.cost
            self.add_station(player)
            self.owned = player

    def get_owner(self) -> Optional[Player]:
        """Returns the owner id if there is one. if not, returns 0"""
        return self.owned
    
    def mortgage(self) -> int:
        """Set mortgaged status to 1 and return the mortgage cost"""
        self.mortgaged = 1
        return self.mortgage_value
    
    def buyback(self) -> int:
        """Set mortgaged status to 0 and returns the buyback cost"""
        self.mortgaged = 0
        return self.buyback_cost
    
    def is_mortgaged(self) -> bool:
        """Checks if the property is mortgaged (useful for paying rent)"""
        if self.mortgaged == 0:
            return False
        else:
            return True
    
    def get_rent(self, stations_owned: int) -> int:
        """Returns the value of rent need to be paid if landed on"""
        return self.rent[stations_owned-1]
    
    def get_player_pairs(self, player: Player) -> Optional[List]:
        """Returns a list of all the pairs that the player has"""
        player_pairs = []
        pairs_to_search = self.pair
        for property in player.properties:
            if property in pairs_to_search:
                player_pairs.append(property)

        return player_pairs
    
class Utility:
    """A Utility card
    
    Each card has multiple different features. 
    
    === Public Attributes ===
    id: the card id
    name: name of the utility
    cost: how much the player must pay to purchase the utility
    rent: how much the player collects from owning the utility when 
          someone else lands on it. This depends on what the player rolls
    mortgage_value: how much money the player gets back when mortgaging
    buyback_cost: how much to buy back the house once mortgaged
    owned: id of the player who owns the property. If unowned, value is 0
    pair: which cards are also paired with this card. this is important
          because you need the full set to build houses"""
    id: int
    name: str
    cost: int
    rent: Tuple[int, int]
    mortgage_value: int
    mortgaged: int
    buyback_cost: int
    owned: Optional[Player]
    pair: Optional[List]

    def __init__(self, id: int, name: str, cost: int, rent: Tuple[int, int],
                 mortgage_value: int, buyback_cost: int, pair: Optional[List]) -> None:
        """Initialize this card with static details"""
        self.id = id
        self.name = name
        self.cost = cost
        self.rent = rent
        self.mortgage_value = mortgage_value
        self.buyback_cost = buyback_cost
        self.pair = pair

        self.mortgaged = 0
        self.owned = None
        

    def __str__(self) -> str:
        return self.name

    def is_owned(self) -> bool:
        """Checks if the utility is owned (used for buying/paying rent)"""
        if self.owned == None:
            return False
        else:
            return True
    
    def add_util(self, player: Player) -> None:
        player.properties.append(self)
        print(f"{player} just bought {self}")

    def buy(self, player: Player) -> None:
        """Sets the new owner of the card based on player buying"""
        if player.money < self.cost:
            print(f"{player} does not have enough money to buy {self}.")
        else:
            player.money -= self.cost
            self.add_util(player)
            self.owned = player

    def get_owner(self) -> Optional[Player]:
        """Returns the owner id if there is one. if not, returns 0"""
        return self.owned
    
    def mortgage(self) -> int:
        """Set mortgaged status to 1 and return the mortgage cost"""
        self.mortgaged = 1
        return self.mortgage_value
    
    def buyback(self) -> int:
        """Set mortgaged status to 0 and returns the buyback cost"""
        self.mortgaged = 0
        return self.buyback_cost
    
    def is_mortgaged(self) -> bool:
        """Checks if the property is mortgaged (useful for paying rent)"""
        if self.mortgaged == 0:
            return False
        else:
            return True
    
    def get_rent(self, utilities_owned) -> int:
        """Returns the value of rent need to be paid if landed on"""
        #Re-roll dice
        dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
        print(f'You rolled a {dice1} and {dice2}.')
        return (self.rent[utilities_owned-1] * (dice1+dice2))
    
    def get_player_pairs(self, player: Player) -> Optional[List]:
        """Returns a list of all the pairs that the player has"""
        player_pairs = []
        pairs_to_search = self.pair
        for property in player.properties:
            if property in pairs_to_search:
                player_pairs.append(property)

        return player_pairs

    
    