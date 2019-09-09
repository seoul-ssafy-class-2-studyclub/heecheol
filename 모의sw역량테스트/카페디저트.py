import sys
sys.stdin = open('input.txt', 'r')

# N x N
# 대각선으로 이동가능
# 사각형모양으로 그리고 돌아와야함
    # 시계 방향으로 고정
    # 시작 지점 범위
# 같은 종류 디저트 노, 같은 카페 두번도 노
# 되도록 많은 디저트카페에 들리기, 이때 개수 출력


def move(idx1, idx2):
    global flag
    
    if flag == 1:
        for di in range(2):
            idx3 = idx1 + nxt1[di][0]
            idx4 = idx2 + nxt1[di][1]
            if di == 0:     
                if idx3 < N-1 and idx4 < N:
                    route.append((idx3, idx4))
                    move(idx3, idx4)
                    route.pop()
            else:
                flag = 2
                route.append((idx3, idx4))
                move(idx3, idx4)
                route.pop()

    elif flag == 2:
        for di in range(2):
            idx3 = idx1 + nxt2[di][0]
            idx4 = idx2 + nxt2[di][1]
            if di == 0:     
                if idx3 < N-1 and idx4 > 0:
                    route.append((idx3, idx4))
                    move(idx3, idx4)
                    route.pop()
            else:
                flag = 3
                route.append((idx3, idx4))
                move(idx3, idx4)
                route.pop()

    elif flag == 3:
        idx3 = idx1-1
        idx4 = idx2-1
        if i != idx3 and (j-idx4)/(i-idx3) == 1.0:
            print('oh yes')        
        move(idx3, idx4)
        



TC = int(input())
N = int(input())
board = [input().split() for _ in range(N)]

nxt1 = [(1, 1), (1, -1)]
nxt2 = [(1, -1), (-1, -1)]
nxt3 = [(-1, -1), (-1, 1)]
nxt4 = [(-1, 1)]

cafes = -1
# for i in range(N-2):
#     for j in range(1, N-1):
#         flag = 1
#         route = []
#         move(i, j)
#         pass

flag = 1
route = [(0, 1)]
i = 0
j = 1
move(i, j+1)
