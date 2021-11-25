import sys
input = sys.stdin.readline

def fibo(n) :
    #종료 조건
    if n == 1 or n ==2:
        return 1    
    # 계산 된 적 있다면 바로 dp테이블 리턴
    if d[n] != 0 :
        return d[n]
    #아직 계산 하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[n] = fibo(n - 1) + fibo(n -2)
    
    return d[n]
    
    
if __name__ == '__main__' :
    
    n = int(input())
    
    d = [0]*(n+1)
    
    print(fibo(n))
    