# 임포트 할꺼 정하기
# 입력 숫자 받기
# 구현 하기
import sys
N = int(sys.stdin.readline())

for star in range(1,N+1):    
    
    for star2 in range(0,star):
        print('*',end='')
    print()
# 2중 포문 쓸때 주의해서 쓸것 생각잘해서 몇번 돌릴지 생각하고 쓸것 개행 문자도 주의하고 
        
        