# S01D02H03H04
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    card = []
    card_info = input()

    for i in range(len(card_info)//3):
        new_card = card_info[3*i:3*(i+1)]

        if new_card in card:
            print(f'#{tc} ERROR')
            break
        else:
            card.append(new_card)
    else:
        patt = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
        for i in range(len(card)):
            card_patt = card[i][0]
            patt[card_patt] -= 1

        print(f'#{tc}', ' '.join(map(str, patt.values())))
        
