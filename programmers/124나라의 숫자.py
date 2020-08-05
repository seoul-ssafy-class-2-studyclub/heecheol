def solution(n):
    number = [n]
    while number[0] // 3:
        quotient = number[0] // 3
        remainder = number[0] % 3
        number[0] = remainder
        number.insert(0, quotient)

    for k in range(len(number)-1, -1, -1):
        if number[k] == 1 or number[k] == 2:
            continue
        elif number[k] == 0:
            if k > 0:
                number[k-1] -= 1
                number[k] = 4
            else:
                number.pop(0)
        else:
            number[k-1] -= 1
            number[k] = 2

    answer = ''.join(list(map(str, number)))

    return answer


solution(28)
