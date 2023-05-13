#Need Player Class, HumanPlayer child, CompPlayer child

#own_pair: bool that indicates whether the full set is owned
from typing import List, Optional, Tuple
import random

class Player:
    """A player in Monopoly. 

    === Public Attributes ===
    id: the player's number
    money: how much money the player currently holds
    properties: a list of properties the player currently holds
    position: what space the player is currently on, from 0-39
    is_bankrupt: status of player. If the player is bankrupt at the end of the turn
                 they will be removed from the game
    in_jail: whether the player is in jail. if in jail, can not collect rent
    """
    id: int
    money: int
    properties: List
    position: int
    is_bankrupt: bool
    in_jail: bool

    def __init__(self, player_id: int) -> None:
        self.id = player_id
        self.money = 1500
        self.properties = []
        self.position = 0
        self.is_bankrupt = False
        self.in_jail = False

    def __str__(self) -> str:
        return (f'Player {self.id}')

    def bankrupt(self) -> None:
        print(f"{self} is bankrupt!")
        for property in self.properties:
            property.owned = None
        self.properties = []
        self.money = 0
        self.is_bankrupt = True

    def send_to_jail(self) -> None:
        self.in_jail = True
    
    def get_out_jail(self) -> None:
        self.in_jail = False

    def set_pos(self, pos: int) -> None:
        self.position = pos
