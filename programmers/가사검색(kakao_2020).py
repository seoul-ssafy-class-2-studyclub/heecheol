import sys
sys.stdin = open('input.txt', 'r')


def solution(words, queries):
    len_words = len(words)
    len_queries = len(queries)

    len_each_word = [len(word) for word in words]

    q_mark = [0] * len_queries
    answer = [0] * len_queries

    for q in range(len_queries):
        query = queries[q]
        len_query = len(query)

        if query[0] == '?':
            if q_mark[q] == 0:
                idx = query.count('?')
                q_mark[q] = idx
            else:
                idx = q_mark[q]

            query_part = query[idx:]

            for w in range(len_words):
                if len_query == len_each_word[w] and query_part == words[w][idx:]:
                    answer[q] += 1

        else:
            if q_mark[q] == 0:
                idx = len_query - query.count('?')
                q_mark[q] = idx
            else:
                idx = q_mark[q]

            query_part = query[:idx]

            for w in range(len_words):
                if len_query == len_each_word[w] and query_part == words[w][:idx]:
                    answer[q] += 1

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
