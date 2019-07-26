from pprint import pprint

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for t in range(1, T + 1):
    score_list = []
    grade_list = []
    N, K = map(int, input().split())
    total_scores = {}

    for gd in grade:
        for i in range(N // 10):
            grade_list.append(gd)

    for n in range(N):
        midterm, final, homework = map(int, input().split())
        score = 0.35 * midterm + 0.45 * final + 0.2 * homework

        total_scores[n] = score

        if K - 1 == n:
            score_K = (n, score)
            
    grades = sorted(total_scores.items(), key=lambda x:x[1], reverse=True)

    K_grade = grades.index(score_K)

    pprint(grade_list[K_grade])
    
    