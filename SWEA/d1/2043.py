# 비밀번호 시행착오
inputs = list(map(int, input().split()))
if len(inputs) == 2:
    p = inputs[0]
    k = inputs[1]
    if p > k:
        print(p - k + 1)
    else:
        print('잘못입력')
else:
    print('잘못입력')
