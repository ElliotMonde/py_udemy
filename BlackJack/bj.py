from random import randint

def gen_deck():
    """
    generates a full 52-cards deck
    """
    suit = [val for val in range(2, 11)]+['Ace', 'Jack', 'Queen', 'King']
    curr_deck = {
        'Clubs': [card for card in suit],
        'Diamonds': [card for card in suit],
        'Hearts': [card for card in suit],
        'Spades': [card for card in suit]
    }
    return curr_deck


def choose_card(user_hand,deck):
    """
    draws a card for the user, removes chosen card from deck dict, params: (user_hand_list, card_deck)
    """
    card_suit = list(deck)[randint(0, 3)]
    choosen_card = deck[card_suit][randint(0, len(deck[card_suit])-1)]
    deck[card_suit].remove(choosen_card)
    user_hand.append(choosen_card)

def draw_more(user_hand,deck):
    """
    asks user if draw one more card for the user, params: (user_hand_list, card_deck)
    """
    if str.upper(input("Do you want to draw one more card?[Y/N] : ")) == "Y":
        choose_card(user_hand,deck)
        print(user_hand)
        draw_more(user_hand,deck)

def card_to_score(com_hand):
    """
    converts cards to total score value for computer, params: (com_hand_list)
    """
    com_val = 0
    ace_count = 0
    for card in com_hand:
        match(card):
            case 'Ace':
                ace_count += 1
            case 'Jack' | 'Queen' | 'King':
                com_val += 10
            case _:
                com_val += card
    if ace_count > 0:
        ace_count -= 1
        if com_val <= 10:
            com_val += 10
        else:
            com_val += 1
    return com_val

def win_check(user_hand,com_hand,deck):
    """
    checks for winner, params: (user_hand_list, com_hand_list, card_deck)
    """
    user_val,com_val = 0,0
    for card in user_hand:
        match(card):
            case 'Ace':
                if int(input('Count Ace as 1 or 10? ')) == 1:
                    user_val += 1
                else:
                    user_val += 11
            case 'Jack' | 'Queen' | 'King':
                user_val += 10
            case _:
                user_val += card

    com_val = card_to_score(com_hand)

    while com_val < 17:
        choose_card(com_hand,deck)
        com_val = card_to_score(com_hand)


    if com_val<=21 and com_val > user_val:
        print("You lose!")
    elif user_val == com_val or (user_val > 21 and com_val >21):
        print("draw!")
    elif user_val == 21:
        print("BLACKJACK! You Win!")
    elif user_val > 21 and com_val <=21:
        print("Over 21!")
    else:
        print("You Win!")
    print(f"com's hand: {com_val} : {com_hand}, your hand: {user_val} : {user_hand}")

def init_game():
    """
    starts the game!
    """
    curr_deck = gen_deck()
    user_hand = []
    choose_card(user_hand,curr_deck)
    choose_card(user_hand,curr_deck)
    print("current user's hand: ",user_hand)
    com_hand = []
    choose_card(com_hand,curr_deck)
    choose_card(com_hand, curr_deck)
    print("com's hand: ", com_hand[0])
    draw_more(user_hand,curr_deck)
    win_check(user_hand,com_hand,curr_deck)

init_game()