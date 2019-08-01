import sys
sys.stdin = open('input.txt', 'r')

for T in range(int(input())):
    N = int(input())
    string = input()
    marks = ['!', '.', '?']
    points = []
    for i in range(len(string)):
        if string[i] in marks:
            points.append(i)
    
    index_1 = 0
    for i in range(len(points)):
        index_2 = points[i]
        sentence = string[index_1:index_2]
        print(sentence)
        index_1 = index_2 + 2   # marks + ' '


