import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    test_case = int(input())
    for _ in range(test_case) :
        N = int(input())
        dp = [[0,0]for _ in range(N + 1)]
        dp[0] = [1,0]
        if N == 0 :
            print(*dp[0])
            continue
        dp[1] = [0,1]
        if N == 1 :
            print(*dp[1])
            continue
        
        for i in range(2, N+1) :
            for j in range(2) :
                dp[i][j] = dp[i-1][j] + dp[i-2][j]
            
            
        print(*dp[N])    