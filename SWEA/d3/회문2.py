import sys
sys.stdin = open('input.txt', 'r')

def Columntorow(arr, N):
    result = []
    for iy in range(N):
        new = []
        for ix in range(N):
            new.append(arr[ix][iy])
        result.append(new)
    #print(result)
    return result


def Search(arr, N):
    num_list = []
    for ar in arr:
        for idx in range(0, N-1):
            for idx2 in range(idx+1, N+1):
                temp = ar[idx:idx2]
                if ar[idx:idx2] == temp[::-1]:
                    print(temp)
                    num_list.append(len(temp))
    return set(num_list)

for tc in range(1):
    T = int(input())
    N = 8

    sentences = []

    for i in range(N):
        temp = list(map(str, input()))
        sentences.append(temp)

    result1 = Search(sentences, N)

    new_sentences = Columntorow(sentences, N)

    result2 = Search(new_sentences, N)

    result3 = list(result1) + list(result2)

    print(f'#{T} {max(result3)}')