import random


class Deck:
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck = []
        for s in self.suits:
            for v in self.values:
                self.deck.append([v] + [s])
        self.shuffle_deck()

    def shuffle_deck(self):
        print("Starting deck shuffle")
        shuffled_deck = []
        i = 1
        while i <= self.deck.__len__():
            card_num = random.randint(i, self.deck.__len__())
            # Reduce max length by 1 since we are staring index with 0
            card = self.deck.pop(card_num-1)
            shuffled_deck.append(card)
        print(f"Shuffled deck: {shuffled_deck}")
        self.deck = shuffled_deck

    def draw_cards(self, count):
        drawn_cards = []
        print(f'Drawing {count} card(s) from current deck')
        try:
            count > self.deck.__len__()
        except:
            print(f'Not enough cards left in the deck. Cards left {self.deck.__len__()}')

        for i in range(0, count):
            drawn_card = self.deck.pop(i)
            drawn_cards.append(drawn_card)
        return drawn_cards


class Game:
    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.num_players = num_players
        self.player_cards = self.distribute_handcards()
        self.comm_cards = self.community_cards()

    def display_handcards(self):
        # Print out player cards
        for i in range(0, self.num_players):
            print(f'Player {i+1} cards: {self.player_cards[i]}')

    def distribute_handcards(self):
        player_cards = []
        # Distribute 2 hand cards for each player
        for i in range(0, self.num_players):
            new_card = self.deck.draw_cards(1)
            print(f'Drew {new_card} for player {i}')
            player_cards.append(new_card)
        for i in range(0, self.num_players):
            new_card = self.deck.draw_cards(1)
            print(f'Drew {new_card} for player {i}')
            player_cards[i].append(new_card[0])

        return player_cards

    def burn_card(self):
        print('Burning a card')
        self.deck.draw_cards(1)

    def community_cards(self):
        comm_cards = []
        comm_nums = [3, 1, 1]
        for j in comm_nums:
            print(f'Drawing {j} card(s)')
            self.burn_card()
            cards = self.deck.draw_cards(count=j)
            print(cards)
            comm_cards = comm_cards + cards
            print(f'Community Cards: {comm_cards}')
        return comm_cards

    def display_community_cards(self):
        print(self.comm_cards)


if __name__ == '__main__':
    new_game = Game(num_players=5)
    print('******** PLAYER CARDS ************')
    new_game.display_handcards()
    print('********COMMUNITY CARDS **********')
    new_game.display_community_cards()
    print('*******************************')
