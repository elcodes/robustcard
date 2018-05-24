# One object of this class represents black jacks, ranks, and suits.
class Card:
# this is a card constructer that constructs  a card each time it is called
    def __init__(self, rank, suit):
# This defines each cards' ranks in a special case dictionary
        self.ranks = dict([(1,"Ace"), (2,2), (3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10), (11, "Jack"),(12, "Queen"),(13, "King")])
# This defines my suits
        self.suits = {"s":"Spades","d":"Diamonds","c":"Clubs","h":"Hearts" }
# verifying the parameter passed to the __init__ function
        if type(rank) != int: # raising a error if rank isn't an integer
          raise TypeError("invalid type of rank")
        if type(suit) != str: # raising an error if suit isn't a string
          raise TypeError("Suit must be a character") #raising an error if suit isn't a character
        if type(suit) != str:
          raise NameError("invalid value of suit") # raising an error if the suit value is typed in Strings i.e. Clubs etc
        if rank < 1 or rank > 13: # raising an error if rank is less negatives and more than 13
          raise ValueError("invalid value of rank")
        if suit !="s" and suit !="h" and suit !="c" and suit != "d": # raising an error if suit is outside the defined suits
          raise ValueError("invalid value of suit")
# define my variables
# This sets the value rank & suit to be passed on to the function as a parameter into class's instance variables
        self.rank = rank
        self.suit = suit
# These functions retrieve a rank, suit, bjValue of a card
    def getRank(self): # this method calls the rank value then return the value
        return self.rank
    def getSuit(self): # this method calls the suit value then return the value
        return self.suit
    def bjValue(self): # this method calls the Black Jack then return the value
        return self.rank
    # A function that covert objects to strings
    def __str__(self):
        return "%s of %s" % (self.ranks[self.rank], self.suits[self.suit])
    # [...] in self.suits[self.rank] mean I'm enabling the the return of the type of rank and value of suit in strings
try:
    c = Card(-3, "e") # this automatically calls __init__ where we set above
    print (c)
    print (c.getRank())
    print (c.getSuit())
    print (c.bjValue())
# print the error message that was raise'd with the error from __init__                    # the data and do the validations.
except ValueError as e: #checking if there's an error in "e"
     print(str(e)) # print the message for the value error raised in __init__ for rank
except TypeError as e:
    print (str(e)) # print the message for the type error raised in __init__ for suit
except NameError as e:
    print (str(e)) # print the name error raised in __init__ for suit
"""invalid value of rank
"""