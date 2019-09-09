# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

alpabets = str(input())

numbers = ''
for alpabet in alpabets:
    number = ord(alpabet) - 64
    numbers = f'{numbers} {number}'
print(numbers[1:])
