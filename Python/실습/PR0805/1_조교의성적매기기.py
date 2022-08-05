import sys
import heapq
sys.stdin = open("_조교의성적매기기.txt")
input = sys.stdin.readline

T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']                     # 학점을 리스트에 담음 // 추후에 인덱스값으로 꺼내기 위함.
for test_case in range(1, T+1):                                                 # test_case = T
    N, K = map(int, input().split())                                            # N명의 학생, 학점을 알고싶은 K번째 학생
    scores = {}                                                                 # 'Key'=학생번호, 'Value'=점수
    score_lst = []                                                              # 점수들을 내림차순으로 나열하기 위한 빈 '리스트'
    for i in range(1, N+1):                                                     # N명의 학생들을 순서대로 순회
        mid_term, final_term, report = map(int, input().split())                # 중간고사, 기말고사, 과제 점수를 입력받음
        score = round(mid_term *(0.35) + final_term*(0.45) + report*(0.2), 2)   # 각 점수 배율을 계산한 총점
        score_lst.append(score)                                                 # 총점을 빈 '리스트'에 담는다.
        scores[i] = scores.get(i, score)                                        # 딕셔너리에 학생번호와 점수를 기록한다.
    score_lst.sort(reverse=True)                                                # 리스트를 내림차순으로 인덱스 = 등수
    print(f'#{test_case} {grade[score_lst.index(scores[K])//int(N/10)]}')       # 학점은 (등수==리스트의 K번째 학생의 점수의 인덱스)//(학생수/10)