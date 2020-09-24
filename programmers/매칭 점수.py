import re


def solution(word, pages):
    n = len(pages)

    base_score = [0] * n
    link_score = [0] * n

    p1 = re.compile(word, re.I)
    p2 = re.compile(r'<meta property=\"og:url\" content=\"https://(.*?)\"/>')

    index_by_url = {}

    for i in range(n):
        page = pages[i]
        patterns = p1.finditer(page)    # similar word patterns

        url = p2.search(page).group(1)
        index_by_url[url] = i

        for pat in patterns:
            s, e = pat.span()
            if page[s-1].isalpha() or page[e].isalpha():
                continue
            else:
                base_score[i] += 1

    p3 = re.compile(r'<a href=\"https://(.*?)\">')

    for i in range(n):
        page = pages[i]
        links = p3.findall(page)
        if links:
            score = base_score[i] / len(links)
            for link in links:
                if link in index_by_url.keys():
                    idx = index_by_url[link]
                    link_score[idx] += score

    max_score = base_score[0] + link_score[0]
    max_index = 0
    for i in range(1, n):
        if base_score[i] + link_score[i] > max_score:
            max_score = base_score[i] + link_score[i]
            max_index = i

    return max_index


print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
