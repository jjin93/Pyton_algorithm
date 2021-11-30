import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(N) :
    if N <= 2 :
        return 1
    
    elif N <= 4 :
        return 2
    
    if dp[N] != 0 :
        return dp[N]
    
    dp[N] = solution(N-1) + solution(N-5) 
    
    return dp[N]

if __name__ == '__main__' :
    test_case = int(input())
    for _ in range(test_case) :
        N = int(input())
        dp = [0]*(N+1)
        
        print(solution(N-1))        
        