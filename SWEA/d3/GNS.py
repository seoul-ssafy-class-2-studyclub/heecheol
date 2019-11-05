numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for T in range(1, int(input())+1):
    testcase, length = map(str, input().split())
    data = input().split()

    sorted_data = sorted(data, key=lambda x: numbers.index(x))
    result = ' '.join(sorted_data)
    print(testcase)
    print(result)