def frequency(toeicScores): # 점수대별 빈도수 구하기
    counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for toeicScore in toeicScores:
        counters[toeicScore//100] += 1
    return counters

def max_frequency(counters): # 가장 큰 빈도스 값과 점수대 구하기
    max = 0
    scoreBase = 0
    N = len(counters)
    for i in range(N):
        if max < counters[i]:
            max = counters[i]
            scoreBase = i * 100
    return scoreBase, max

def min_frequency(counters): # 가장 적은 빈도수 값과 점수대 구하기
    scoreBase = 0
    N = len(counters)
    min = 11
    for i in range(N):
        if counters[i] != 0 and min > counters[i]:
            scoreBase = i * 100
            min = counters[i]
    return scoreBase, min

toeicScores = []

for i in range(10): # 10번 반복
    temp = int(input("%d번째 토익 값 입력 " %(i+1))) # 입력받은 값을 temp에 저장
    toeicScores.append(temp) # 토익 점수 list에 추가

counters = frequency(toeicScores)

scoreBase, maxCount = max_frequency(counters)

print("가장 많은 점수대= %d, 빈도수= %d" %(scoreBase, maxCount))

scoreBase, minCount = min_frequency(counters)

print("가장 적은 점수대= %d, 빈도수= %d" %(scoreBase, minCount))
