from random import shuffle


stack = [1, 1, 100, 100]
direction = ["up", "up", "down", "down"]


deck = [i for i in range(2, 100)]
shuffle(deck)


def take_card(deck):
    return deck.pop()


def fill_up_hand(hand):
    while len(hand) < 6:
        hand.append(take_card(deck))
    hand.sort()
    return hand


def calculate_diff_and_indices(card, s, index, smallest_diff, stack_index, hand_index):
    diff = abs(card - s)
    if diff < smallest_diff:
        return diff, index, hand.index(card)
    return smallest_diff, stack_index, hand_index


def index_smallest_diff(hand):
    stack_index = 0
    hand_index = 0
    smallest_diff = 100

    for card in hand:
        for index, s in enumerate(stack):
            if (direction[index] == "up" and card > s) or (
                direction[index] != "up" and card < s
            ):
                smallest_diff, stack_index, hand_index = calculate_diff_and_indices(
                    card, s, index, smallest_diff, stack_index, hand_index
                )
    print(f"Smallest diff: {smallest_diff}")
    print(f"Stack index: {stack_index}")
    print(f"Hand index: {hand_index}")
    print(f"Card: {hand[hand_index]}")
    print(f"Stack: {stack[stack_index]}")
    return hand_index, stack_index, smallest_diff


def play_card(hand, cards_played=0):
    # multiple cards can be played
    print(f"Hand: {hand}")
    index, stack_index, smallest_diff = index_smallest_diff(hand)

    # play at least 2 cards
    if cards_played < 2:
        another_card = True
    else:
        # player can choose to play another card
        another_card = (
            input(f"Smallest diff: {smallest_diff}. Play another card? (y/n) ") == "y"
        )
    # cant play another card if hand is empty
    if len(hand) == 0:
        another_card = False
        print("Hand is empty")
    # only play card if the decision is to play another card
    if another_card:
        card = hand.pop(index)
        stack[stack_index] = card
        print(f"Stack: {stack}")
        play_card(hand, cards_played + 1)
    else:
        fill_up_hand(hand)


hand = []
hand = fill_up_hand(hand)
print(f"Hand: {hand}")
play_card(hand)
print(f"Deck: {stack}")
