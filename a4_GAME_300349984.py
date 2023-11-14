import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
    Returns a list of strings representing the playing deck,
    with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen 
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
    Thi shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)
    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]

    # Distribute cards from the deck to the computer and the human player
    for i in range(len(deck)):
        if i % 2 == 0:
            dealer.append(deck[i])
        else:
            other.append(deck[i])
    return (dealer, other)


def remove_pairs(l):
    '''
    (list of str) -> list of str
    Returns a copy of list l where all the consecutive cards with the same rank are removed AND
    the elements of the new list shuffled
    Precondition: elements of l are cards represented as strings described above
    '''

    # Create a copy of the list
    no_pairs = l[:]

    # Remove consecutive cards with the same rank from the list
    i = 0
    while i < len(no_pairs) - 1:
        if no_pairs[i][0] == no_pairs[i+1][0]:
            no_pairs.pop(i)
            no_pairs.pop(i)
        else:
            i += 1

    # Shuffle the elements of the new list
    random.shuffle(no_pairs)

    return no_pairs


def print_deck(deck):
    '''
    (list) -> None
    Prints elements of a given list deck separated by a space
    '''
    for card in deck:
        print(card, end=' ')
    print()


def get_valid_input(n):
    '''
    (int) -> int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives an integer outside of the range [1, n]
    Precondition: n >= 1
    '''

    while True:
        try:
            user_input = int(input(f"Please enter an integer between 1 and {n}: "))
            if 1 <= user_input <= n:
                return user_input
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


def play_game():
    '''()->None
    This function plays the game'''
    
    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
     
    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # Play the game until either the dealer or the human runs out of cards
    while len(dealer) > 0 and len(human) > 0:
        # Dealer's turn
        print("It's my turn.")
        dealer_card = dealer.pop(0)
        print("I drew a card:", dealer_card)
        wait_for_player()
        
        # Human's turn
        print("It's your turn.")
        print("Your current deck of cards is:")
        print_deck(human)
        print("I have", len(dealer), "cards. If 1 stands for my first card and", len(dealer), "for my last card, which of my cards would you like?")
        user_input = get_valid_input(len(dealer))
        print("You asked for my", user_input, "th card.")
        chosen_card = dealer[user_input - 1]
        print("Here it is. It is", chosen_card)
        human.append(chosen_card)
        print("With", chosen_card, "added, your current deck of cards is:")
        print_deck(human)
        human = remove_pairs(human)
        print("And after discarding pairs and shuffling, your deck is:")
        print_deck(human)
        wait_for_player()

    # Determine winner
    if len(dealer) == 0:
        print("I ran out of cards. You win!")
    else:
        print("You ran out of cards. I win!")

# main
play_game()
