#-------------------------------------------------------------------------------
# Name:         Saffa Gbondo
# Assignment:   A12: Stacks, Queues, and the Card Game War
# Purpose:      Create a card game called War game using queues and stacks
#               for the data structures.
# Created:     10/15/2016
# Author:      mambondiumwem
# Acknowledgements:
# Ideas and principles(no actual code taken) obtained from the following websites:
# http://stackoverflow.com/questions/13714284/stack-of-cards-and-the-game-of-war
# http://codereview.stackexchange.com/questions/131174/war-card-game-using-classes
#-------------------------------------------------------------------------------
from MyQueue import Queue                                   # uses the queue class that is provided in the question
from Stack import Stack                                     # uses the stack class that is provided in the question
import random                                               # imports the random library
import sys                                                  # imports the system library


class WarCardGame:

    """The different properties of the War card game"""

    def __init__(self):
        """Creating the different piles needed for the game, and initializing
        all instance variables"""

        self.playingPile = Stack()
        self.cpu_playingPile = Stack()
        self.storagePile = Queue()
        self.cpu_storagePile = Queue()
        self.lootPile = Queue()
        self.dealingPile = Stack()
        self.deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # the numbers on the deck cards are initialized
        self.current_playerCard = None              # This card will hold the value of the current card in game for the human player
        self.current_cpuCard = None                 # This card will hold the value of the current card in game for the computer player

    def prepare_dealPile(self):
        """Prepares the dealing deck before the game starts."""
        deck_cards = self.deck * 5
        for num in deck_cards:                              # This goes to every card in the deck
                self.dealingPile.push(num)                  # This appends the card number to the dealing pile 5 times.
                                                            # After iterating through the deck cards, the dealing pile will have 50 cards, with values from 0 to 9 repeated 5 times each.
        self.shuffle_dealingPile()                          # The dealing pile is shuffled after getting the 50 cards.

    def shuffle_dealingPile(self):
        """ This randomly shuffles the dealing pile."""
        random.shuffle(self.dealingPile.items)

    def deal(self):
        """This Deals 25 cards to each playing pile, always taking the one at the top.
        It will deal one card to player one, then one to computer, and it will
        repeat the process until both players have 25 cards and the dealing pile
        is empty."""
        self.prepare_dealPile()                                      # Calls the funtion that prepares the dealing pile by putting the cards in and shuffling it.
        first_popped_card = 0
        second_popped_card = 0
        while self.dealingPile.size() > 0:                          # Cards will be dealt as long as there are cards in the dealing pile
            first_popped_card = self.dealingPile.pop()
            self.playingPile.push(first_popped_card)                # The card dealt is placed on top of the pile
            second_popped_card = self.dealingPile.pop()
            self.cpu_playingPile.push(second_popped_card)           # The card dealt is placed on top of the pile

    def refilling_playingPile(self):
        """Refills the playing pile with the storage pile cards"""

        if self.storagePile.size() > 0:
            for card in self.storagePile.q:
                self.playingPile.push(self.storagePile.dequeue())
        else:
            self.endGame('Computer Player')                         # This Ends the game

    def refilling_cpuPile(self):
        """This Refills the cpu playing pile."""

        if self.cpu_storagePile.size() > 0:
            for card in self.cpu_storagePile.q:
                self.cpu_playingPile.push(self.cpu_storagePile.dequeue())
        else:
            self.endGame('Human Player')                            # This ends the game

    def draw_card(self):
        """Draws one card from each playing pile so that they can be
        compared."""
        if self.playingPile.size() > 0:                             # when bigger than zero
            self.current_playerCard = self.playingPile.pop()
        else:
            self.refilling_playingPile()
        if self.cpu_playingPile.size() > 0:                         # when bigger than zero
            self.current_cpuCard = self.cpu_playingPile.pop()
        else:
            self.refilling_cpuPile()

    def compare_cards(self):
        """Compares the rank of the cards drawn to decide the
        following step in the game."""
        if self.current_playerCard > self.current_cpuCard:          # This is when the values of cards of the player are bigger than the values of the cards of the computer
            self.storagePile.enqueue(self.current_playerCard)
            self.storagePile.enqueue(self.current_cpuCard)
            self.current_playerCard = None                          # This instatiates these variables to None after they have been used.
            self.current_cpuCard = None
        elif self.current_cpuCard > self.current_playerCard:        # This is when the computer has better cards than player
            self.cpu_storagePile.enqueue(self.current_cpuCard)
            self.cpu_storagePile.enqueue(self.current_playerCard)
            self.current_cpuCard = None
            self.current_playerCard = None
        else:                                                                       # This section deals with the war part of the game, when both cards are of the same rank
            self.move_my_loot(self.current_playerCard, self.current_cpuCard)     # First, the two cards are placed in the loot pile
            self.default_current_cards()                                            # This sets the current card variables to the default
            self.war_event()

    def move_my_loot(self, playerCard, cpuCard):                                 # This places the cards into a loot pile.
        """Puts the two cards onto the loot pile, one after the other."""
        self.lootPile.enqueue(playerCard)
        self.lootPile.enqueue(cpuCard)

    def default_current_cards(self):                                                # if values of cards equal None
        """Sets the value of the variables for current cards to default None."""
        self.current_playerCard = None
        self.current_cpuCard = None

    def endGame(self, winner):
        """Checks if the player has enough cards to keep playing"""
        print ("We have a winner!")                             # announces that there is a winner
        print ("The " + winner + " won")
        next_step = raw_input("Do you want to try again? Type Y for yes or N for no.")
        while next_step == "N" or next_step == "n" or next_step == "Y" or next_step == "y":
            if next_step == "N" or next_step == "n":            # if player inputs "no" the game ends
                print ("Thank you for playing the game.")
                sys.exit()                                      # this exits the game
            else:
                print('Start Again:')                           # allows the game to start over.
                self.Play_game()
        else:
            while next_step != "N" or next_step != "n" or next_step != "Y" or next_step != "y":
                print ("That was not a valid input. Try again.")    # keeps prompting the player until he puts in a valid input
                next_step = raw_input("Do you want to try again? Type Y for yes or N for no.")

    def war_event(self):
        """Controls what happens when the two players draw the same card."""
        self.draw_card()
        self.move_my_loot(self.current_playerCard,self.current_cpuCard)
        self.draw_card()                                        # Each player draws a new card from the top of their playing piles
        print('player Card: ' + str(self.current_playerCard))
        print('cpu Card: ' + str(self.current_cpuCard))

        if self.current_playerCard > self.current_cpuCard:
            self.storagePile.enqueue(self.current_playerCard)
            self.storagePile.enqueue(self.current_cpuCard)
            self.storagePile.enqueue(self.lootPile.dequeue())
            self.default_current_cards()
        elif self.current_cpuCard > self.current_playerCard:
            self.cpu_storagePile.enqueue(self.current_cpuCard)
            self.cpu_storagePile.enqueue(self.current_playerCard)
            self.cpu_storagePile.enqueue(self.lootPile.dequeue())
            self.default_current_cards()
        else:
            self.move_my_loot(self.current_playerCard, self.current_cpuCard)
            self.war_event()

    def Play_game(self):                        # this function allows the game to be played
        """This Plays the game"""
        self.__init__()
        self.deal()
        while True:
            self.draw_card()
            print('player Card: ' + str(self.current_playerCard))
            print('cpu Card: ' + str(self.current_cpuCard))
            self.compare_cards()

m = WarCardGame()           # this is the main that calls the class and its containing methods.
print ("Welcome to the War Zone Game, Lets play.")
print('Dealing Pile size: ' + str(m.dealingPile.size()))

m.deal()
print("Human Player cards:")
print (m.playingPile.items)
print("CPU Player cards:")
print (m.cpu_playingPile.items)

print('size of Human playing Pile: ' + str(m.playingPile.size()))
print('size of CPU playing Pile: ' + str(m.cpu_playingPile.size()))

for i in range(250):                                    # This will iterate through the range 200 times
    m.draw_card()
    print('player Card: ' + str(m.current_playerCard))
    print('cpu Card: ' + str(m.current_cpuCard))
    m.compare_cards()


