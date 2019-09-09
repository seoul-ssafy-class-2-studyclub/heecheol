import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
switchs = list(input().split())

for i in range(int(input())):
    gen, num = map(int, input().split())
    if gen == 1:
        index = num-1
        while index < N:
            if switchs[index] == '0':
                switchs[index] = '1'
            else:
                switchs[index] = '0'
            index += num
    elif gen == 2:
        i = 1
        index = num - 1
        if switchs[index] == '0':
            switchs[index] = '1'
        else:
            switchs[index] = '0'
        while index - i >= 0 and index + i < N:
            if switchs[index-i] == switchs[index+i]:
                if switchs[index-i] == '0':
                    switchs[index-i] = switchs[index+i] = '1'
                else:
                    switchs[index-i] = switchs[index+i] = '0'
            else:
                break
            i += 1
j = 0
for i in range(len(switchs)//20):
    status_now = ' '.join(switchs[20*i:20*i+20])
    print(status_now)
    j = 20*(i+1)
status_now = ' '.join(switchs[j:])
print(status_now)
            