from core.deck import build_standard_deck,shuffle_by_suit
from core.game_logic import run_full_game

if __name__ == "__main__":
    deck = build_standard_deck()
    deck_shufle = shuffle_by_suit(deck)

    player = {"hand": []}
    dealer = {"hand": []}
    run_full_game(deck_shufle, player, dealer)
