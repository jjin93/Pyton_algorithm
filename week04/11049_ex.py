import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**6

def solution(x : int, y : int) :
    if dp[x][y] > 0 :
        return dp[x][y]
    if y - x <= 0 :
        return 0
    result  = 2**31
    
    for k in range(x, y) :
        result = min(result, solution(x, k) + solution(k + 1, y ) + R[x]*C[k]*C[y])
        
        dp[x][y] = result
    
    return dp[x][y]    

if __name__ == '__main__' :
    
    N = int(input())
    R = []
    C = []
    dp = [[0]*(N+1)for _ in range(N+1)]
    for i in range(N) :
        r,c = map(int,input().split())
        R.append(r)
        C.append(c)
    print(solution(0, N-1))    