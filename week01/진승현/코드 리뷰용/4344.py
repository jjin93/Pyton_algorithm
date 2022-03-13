import sys
# 반올림,내림,올림 할때도 임포트 해야한다
import math
# 테스트 개수 입력

T = int(sys.stdin.readline())
scores = [0 for i in range(T)]
total = []
# 케이스 학생 수가 N으로 첫수로 입력 그 뒤로 N명의 점수 입력
for i in range(T):
    sum = 0
    scores[i] = list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(scores[i])):
        sum += scores[i][j]

    avg = sum/scores[i][0]
    count = 0
    for j in range(1,len(scores[i])):
        if scores[i][j] > avg :
            count += 1
    
    ratio = float(count/scores[i][0])*100
    total.append(round(ratio,3))

for i in range(len(total)):
    print(str(format(total[i],".3f"))+'%')

    

    
  
