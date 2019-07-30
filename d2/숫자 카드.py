for t in range(int(input())):
    N = int(input())
    
    cards = list(map(int, input()))

    dict_card = {}

    for card in cards:
        if not card in dict_card:
            dict_card[card] = 1
        else:
            dict_card[card] += 1

    # print(dict_card)
    
    card, number = 0, 0
    
    for key, value in dict_card.items():
        if value > number:
            card = key
            number = value
        elif value == number:
            if key > card:
                card = key
        
    print('#{} {} {}'.format(t+1, card, number))

