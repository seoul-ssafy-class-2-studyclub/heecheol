import sys
sys.stdin = open('input.txt', 'r')


num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    end = 0
    flag = False
    for _ in range(N):
        code = input()
        if flag is False:
            for j in range(M):
                if code[j] == '1':
                    end = j
                    flag = True
            if flag is True:
                c = [code[end-55:end-48],
                     code[end-48:end-41],
                     code[end-41:end-34],
                     code[end-34:end-27],
                     code[end-27:end-20],
                     code[end-20:end-13],
                     code[end-13:end-6],
                     code[end-6:end+1]]
                # print(c)
                for a in range(8):
                    for b in range(10):
                        if c[a] == num[b]:
                            c[a] = b
                            break
                # print(c)
                check = (c[0]+c[2]+c[4]+c[6])*3+c[1]+c[3]+c[5]+c[7]
                if check % 10 == 0:
                    print('#{} {}'.format(tc, sum(c)))
                else:
                    print('#{} 0'.format(tc))
