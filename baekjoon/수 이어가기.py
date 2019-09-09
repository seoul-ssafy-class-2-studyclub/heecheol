num1 = int(input())

max_cnt = 0
num2 = 0
for N in range(0, num1+1):
    cnt = 0
    n1 = num1
    n2 = N
    while n1-n2 >= 0:
        cnt += 1
        temp = n2
        n2 = n1 - n2
        n1 = temp
        
    if cnt > max_cnt:
        max_cnt = cnt
        num2 = N
        
result = [num1, num2]

for i in range(max_cnt):
    result.append(num1-num2)
    temp = num2
    num2 = num1 - num2
    num1 = temp


print(max_cnt+2)
print(' '.join(list(map(str, result))))
