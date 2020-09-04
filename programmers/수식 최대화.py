import itertools


def solution(expression):

    arr = []
    calc = set()

    i = 0
    for j in range(1, len(expression)-1):
        if not expression[j].isdigit():
            arr.append(int(expression[i:j]))
            arr.append(expression[j])
            calc.add(expression[j])
            i = j + 1
    arr.append(int(expression[i:]))

    answer = 0
    for order in itertools.permutations(calc, len(calc)):
        arr1 = arr[:]
        for c in order:
            arr2 = []
            i = 0
            while i < len(arr1):
                if arr1[i] != c:
                    arr2.append(arr1[i])
                    i += 1
                elif c == '+':
                    arr2[-1] += arr1[i+1]
                    i += 2
                elif c == '-':
                    arr2[-1] -= arr1[i+1]
                    i += 2
                else:
                    arr2[-1] *= arr1[i+1]
                    i += 2
            arr1 = arr2[:]

        if abs(arr1[0]) > answer:
            answer = abs(arr1[0])

    return answer


print(solution("100-200*300-500+20"))
