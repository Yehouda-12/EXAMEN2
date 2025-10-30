import random

def build_standard_deck() -> list[dict]:
    list_suite = ['H','D','C','S']
    list_rank = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    list_deck = []
    for j in list_suite:
        for i in list_rank:
            list_deck.append({'rank':i,'suite':j})

    return list_deck
def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:


    count = swaps
    while count > 0:
        ind_i = random.randint(0, len(deck)-1)
        card_i = deck[ind_i]

        ind_j = random.randint(0, len(deck)-1)
        if card_i['suite'] == 'H' and ind_j % 5 != 0:
            ind_j = random.randint(0, len(deck)-1)
            continue
        elif  card_i['suite'] == 'C' and ind_j % 3 != 0:
            ind_j = random.randint(0, len(deck)-1)
            continue
        elif  card_i['suite'] == 'D' and ind_j % 2 != 0:
            ind_j = random.randint(0, len(deck))-1
            continue

        elif card_i['suite'] == 'S' and ind_j % 7 != 0:
            ind_j = random.randint(0, len(deck)-1)
            continue
        else:
            count -= 1

            deck[ind_j], deck[ind_i] = deck[ind_i],deck[ind_j]

    return deck


