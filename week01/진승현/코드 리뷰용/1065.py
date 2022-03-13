# 수를 입력 받는다
# 1 <= 한수 <= N 찾는다
# 한수의 개수를 출력한다.
import sys
def hansu(n) :
    if n == 1000:
        n = 999

    if n < 100 :
        count = n
    
    else :
        count = 99
        for i in range(100,n+1):
            # 각 자리수 분리
            # 1의 자리
            a0 = int(i/10**0)%10
            # 10의 자리 
            a1 = int(i/10**1)%10
            # 100의 자리
            a2 = int(i/10**2)%10
           
            if ((a2-a1)==(a1-a0)):
                count += 1
                
    return count
             
N = int(sys.stdin.readline().strip())
print(hansu(N))            


        
