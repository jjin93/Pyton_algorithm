# 입력 첫째줄 N과X가 주어진다
# 입력 둘째줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거가 같고, 10000보다 작거나 같은 정수이다.

# 출력 X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은수는 적어도 하나 존재한다.
import sys
# 빈 리스트 선언
list1 = []
# N,X 인트 타입으로 맵 괄호 안에 넣어서 한번에 여러개 입력 받는다
N,X = map(int,sys.stdin.readline().split())
# list1의 개수 정해주기
# list1 = [0 for i in range(N)]
# [:N]이 과연 개수 제한이 될지 -> 개수 제한된다 기억해 두자!
list1 = list(map(int,sys.stdin.readline().split()[:N]))

for i in range(0,N):
    if list1[i]<X:
        # print 개행 문자 띄우는법, 리스트 쓰는법
        print(list1[i],end=' ')







