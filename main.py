import csv


class Space():
    """
    Defines a singular Space. A name, color, and purchace price are required (color and purchase price can be None).
    is_go, is_jail_space, is_free_parking, and is_go_to_jail are default False. Only one must be specified, others will
    infered.
    """

    def __init__(self, name, color, purchase_price,
                 is_go=False, is_jail_space=False, is_free_parking=False, is_go_to_jail=False):
        self.name = name
        self.color = color
        self.purchasePrice = purchase_price

        if [is_go, is_jail_space, is_free_parking, is_go_to_jail].count(True) > 1:
            raise ValueError("Only one of is_go, is_jail_space, is_free_parking, and is_go_to_jail may be True")
        self.go = is_go
        self.jailSpace = is_jail_space
        self.freeParking = is_free_parking
        self.goToJail = is_go_to_jail




class Spaces():
    def __init__(self):
        self.spaces = []

    def generateDefaultBoard(self):
        pass


class Board():
    def __init__(self):
        self.spaces = Spaces()


class Player():
    def __init__(self):
        self.ownedSpaces = []


class Game():
    def __init__(self):
        self.turn = 0
        self.players = [Player]
        self.board = Board()

    def advanceTurn(self):
        self.turn += 1
        # other turn advancement things here...o
