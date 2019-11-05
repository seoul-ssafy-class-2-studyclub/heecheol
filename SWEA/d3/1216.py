import math

for test in range(10):
    test_case_num = int(input())

    board = []
    max_len = 1
    max_len_update = 1

    front_part = []
    end_part = []

    for row in range(100):                          # 입력을 바탕으로 board 만들기
        board.append(list(input()))

    for i in range(2):                               # 가로, 세로 총 두번 체크
        for row in board:
            row = list(row)                         # zip 함수 이후 tuple => list로 변환하기위해

            for length in range(100, max_len, -1):  # 검사 횟수를 줄이기위해 확인된 최대 길이보다 큰 길이만 검사
                for move in range(100-length+1):    # 한 칸씩 몇번 움직일 수 있는지
                    
                    if length % 2:                   # 길이가 홀수일때
                        half_len = length // 2      # 기준을 잡고 앞, 뒤 slice
                        front_part = row[move:move+half_len]
                        end_part = row[move+half_len+1:move+length]
                    else:                           # 길이가 짝수일때
                        half_len = length // 2
                        front_part = row[move:move+half_len]
                        end_part = row[move+half_len:move+length]

                    if front_part == list(reversed(end_part)):  # 앞, 뒤가 회문인지 확인
                        max_len_update = length
                        break

                if max_len_update > max_len:        # 최대길이 update
                    max_len = max_len_update
                    break
            
        board = list(zip(*board))                   # zip으로 가로, 세로 변환

    print(f'#{test_case_num} {max_len}')
