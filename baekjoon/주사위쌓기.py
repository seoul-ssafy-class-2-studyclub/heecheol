import sys
sys.stdin = open('input.txt', 'r')

def dice(bottom, order):
    next_index = [5, 3, 4, 1, 2, 0]
    index_bottom = dices[order].index(bottom)
    index_upper = next_index[index_bottom]

    upper = dices[order][index_upper]
    return upper


N = int(input())

dices = [input().split() for i in range(N)]
sum_side = []

for i in range(6):
    sides = []
    bottom = dices[0][i]
    for j in range(N):
        
        upper = dice(bottom, j)
        if upper != '6' and bottom != '6':
            sides.append(6)
        elif upper != '5' and bottom != '5':
            sides.append(5)
        else:
            sides.append(4)
        bottom = upper

    sum_side.append(sum(sides))
print(max(sum_side))