def solution(genres, plays):
    from collections import defaultdict

    count = defaultdict(int)
    sort_plays = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        count[genre] += play
        sort_plays[genre].append((-play, i))

    answer = []

    for key, value in sorted(count.items(), key=lambda x: x[1], reverse=True):
        for play, idx in sorted(sort_plays[key])[:2]:
            answer.append(idx)

    return answer


solution(['classic', 'pop', 'classic', 'classic', 'classic'], [500, 600, 150, 800, 2500])