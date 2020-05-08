import re

def solution(word, pages):
    number_of_pages = len(pages)
    word_length = len(word)

    page_number = {}
    linked_pages = [[] for _ in range(number_of_pages)]

    word = word.lower()
    point1 = [0] * number_of_pages
    point2 = [0] * number_of_pages
    point3 = [0] * number_of_pages
    point4 = [0] * number_of_pages

    for i in range(number_of_pages):
        page = pages[i].lower()
        


        temp = page.split('<head>')[1]
        temp = temp.split('</head>')
        head = temp[0]
        body = temp[1]

        rows = page.replace('\n', ', ')
        print(rows)
        p1 = 0
        p2 = 0
        flag = False
        for row in rows:
            # print(row)
            n = len(row) - word_length
            for j in range(n + 1):
                for k in range(word_length):
                    if word[k] != row[j + k]:
                        break
                else:
                    if j > 0 and row[j - 1].isalpha():
                        break
                    if j + word_length < len(row) and row[j + word_length].isalpha():
                        break
                    p1 += 1
            if flag:
                if row[:3] == '<a ':
                    url = row[17:].split('">')[0]
                    linked_pages[i].append(url)
                    p2 += 1

            elif row[:9] == '  <meta p':
                page_url = row[35:].split('"')[0].split('//')[1]
                page_number[page_url] = i
                flag = True

        point1[i] = p1
        point2[i] = p2
    print(page_number)
    print(linked_pages)
    print(point1)
    print(point2)

    for name, idx in page_number.items():
        for nxt in linked_pages[idx]:
            nxt_idx = page_number.get(nxt)
            if nxt_idx is not None:
                nxt_idx = page_number[nxt]
                point3[nxt_idx] += point1[idx] / point2[idx]

    print(point3)
    answer = 0
    temp = 0
    for i in range(number_of_pages):
        point4[i] = point1[i] + point3[i]
        if point4[i] > temp:
            temp = point4[i]
            answer = i
    print(point4)
    print(answer)

    return answer


input1 = 'blind'
input2 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

solution(input1, input2)
