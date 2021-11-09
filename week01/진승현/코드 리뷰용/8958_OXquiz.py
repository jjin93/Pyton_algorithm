# OX문제 연속된 0가 해당 번호의 점수가 된다
# 연속해서 문제를 맞힐수록 해당 번호의 해당 점수가 올라간다.
# 그래서 긴 OX가 주어졌을때 각 해당번호 점수를 다 더해서 토탈 점수를 구해보자

import sys
# 테스트 케이스의 갯수
T = int(sys.stdin.readline())
# OX문제 입력, X개의 갯수 제한
quizs = []
for i in range(T):
    # 문자열 받고 앞뒤로 공백 제거하기
    quiz = sys.stdin.readline().strip()
    # quizs라는 리스트에 문자열 추가하기
    quizs.append(quiz)
    # quizs 배열 상태 ["OXXOXXOOXXXOXXOXO","OOXOXOXOOXOXOXXX","OOXOXXXOXO"]

# quizs의 리스트 갯수만큼 반복
for i in range(len(quizs)):
# quizs[i]의 해당 원소 문자열에서 'X' 제거하기
    quizs[i] = quizs[i].split('X')
    # quizs[i]의 배열중에 빈 배열 제거하기
    # X가 연속되었을때 " "배열이 생긴다
    quizs[i] = list(filter(None,quizs[i]))
    # quizs[i]의 배열 상태 ["O","O","OO","OOOO","OO","OOO"]
    sum = 0
    # quizs[i]안에 원소 개수만큼 반복
    for j in range(len(quizs[i])):
        # quizs[[i]안의 해당 원소 point에 넣음
        # 해당 quizs[i[j]]의 문자열의 길이를 0의 개수로 정하고 point에 저장
        point = len(quizs[i][j])
        # 1부터 point까지 더한 값,공식
        a=int((point*(point+1))/2)
        # sum에 저장
        sum += a        
        
    print(sum)    
        
    
        



