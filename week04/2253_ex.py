import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    N, M = map(int,input().split())
    INF = float('inf')
    
    dp = [[INF] * (int((2 * N) ** 0.5) + 2) for _ in range(N + 1)]
    dp[1][0] = 0
    
    stone_set = set()
    for _ in range(M) :
        stone_set.add(int(input()))
    
    for i in range(2, N + 1) :
        if i in stone_set :
            continue
        
        for j in range(1, int((2 * i) ** 0.5) + 1) :
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
            
    if min(dp[N]) == INF :
        print(-1)
    else :
        print(min(dp[N]))            
    