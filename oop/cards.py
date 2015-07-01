
class Card(object):
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def suit(self):
        return self._suit

    def value(self):
        return self._value

class BlackJackCard(Card):
    def value(self):
        if Card.value(self) == 1:
            return 11
        elif Card.value(self) >= 10:
            return 10
        else:
            return Card.value(self)

a = BlackJackCard(3, 1)
b = BlackJackCard(3, 3)
c = BlackJackCard(2, 13)
print a.value(), b.value(), c.value()
