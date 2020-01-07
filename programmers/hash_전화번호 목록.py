def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) > len(phone_book[i + 1]):
            continue

        n = len(phone_book[i])

        if phone_book[i] == phone_book[i + 1][:n]:
            return False

    return answer

