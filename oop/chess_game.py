
class Board(object):
    def __init__(self, pieces, players):
        self.pieces =
        self.board = {}
        self.players = players
        self.turn = 0

    def init_pieces(self):
        pass

    def move(self, player, source, destination):
        pass

    def check_win_condition(self, player):
        pass

class Piece(object):
    # make override by making subclasses
    def __init__(self, owner, position):
        self.position = position
        self.owner = owner

    def is_valid_move(self, source, destination):
        pass

class Player():
    Players = {}
    def __init__(self):
        c = 0
        if c in Player.Players:
            c += 1
        Players[c] = self
        self.id = c
