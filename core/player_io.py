def ask_player_action() -> str:
    ask = ''
    while ask.upper() != 'S' and  ask.upper() != 'H' :
        # test  = ask != 'S' or  ask != 'H'
        # print(test)
        ask = input('What your decision ? (S or H) :')
    return ask.upper()


