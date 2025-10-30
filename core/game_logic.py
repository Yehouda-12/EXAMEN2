from core.player_io import ask_player_action
from core.deck import build_standard_deck

def calculate_hand_value(hand: list[dict]) -> int:
    count = 0

    for i in range(len(hand)):
        if hand[i]['rank'] == 'K' :
            count += 10
        elif hand[i]['rank'] == 'Q':
            count += 10
        elif hand[i]['rank'] == 'J':
            count += 10
        elif hand[i]['rank'] == 'A':
            count += 1
        elif hand[i]['rank'].isdigit():
            count += int(hand[i]['rank'])

    return count

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player = player['hand']
    dealer = dealer['hand']

    card_1_player = deck.pop()
    card_2_player = deck.pop()
    player.append(card_1_player)
    player.append(card_2_player)
    print(calculate_hand_value(player))

    card_1_dealer = deck.pop()
    card_2_dealer = deck.pop()
    dealer.append(card_1_dealer)
    dealer.append(card_2_dealer)
    print(calculate_hand_value(dealer))



def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer = dealer['hand']

    while calculate_hand_value(dealer) < 17:
        card_dealer = deck.pop()
        dealer.append(card_dealer)
    if calculate_hand_value(dealer) > 21 :
        print('There is a disqualification for dealer .')
        return False
    elif 17 < calculate_hand_value(dealer) >21:
        return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    ask = ask_player_action()


    while ask == 'H':
        card_player = deck.pop()
        player['hand'].append(card_player)
        calculate_hand_value(player['hand'])
        if calculate_hand_value(player['hand']) > 21:
            print('The player lose .')
            break
        elif calculate_hand_value(player['hand']) <= 21:
            continue
    if ask == 'S':
        deal = dealer_play(deck,dealer)
        if deal is True:
            if calculate_hand_value(player['hand']) == calculate_hand_value(dealer['hand']):
                print('teko')
            elif calculate_hand_value(player['hand']) > calculate_hand_value(dealer['hand']):
                if calculate_hand_value(player['hand']) <= 21 :
                    print('The player win !!!')
                else:
                    print('The player lose !')
            else:
                print('The dealer lose')


    print(f"Player :{calculate_hand_value(player['hand'])}\n"
          f"Dealer : {calculate_hand_value(dealer['hand'])}")
    










