import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    N, M = map(int,input().split())
    # 
    dp = [[float('inf')] * (int((2 * N) ** 0.5) + 2) for _ in range(N + 1)]
    dp[1][0] =  0
    
    stone_set = set()
    for _ in range(M) :
        stone_set.add(int(input()))
    for i in range(2, N + 1) :
        if i in stone_set :
            continue
        # int((2*N)^ 0.5)의 의미
        # int((2 * i) ** 0.5) + 1)은 1부터 속도가 끊임없이 1씩 증가하며 점프할 때 N에 도달했을때의 근사값이다.
        # 등차 수열의 합 공식 = k(2a + (k-1)d) / 2   (이 문제에서 a(첫번째 수) = 1, d(공차) = 1 )
        # 따라서 마지막에 있는 돌까지 가장 빠르게 갈 수 있는 돌들의 수의 합 N = k(k+1)/2
        # k = (2N-k)^0.5 <= 2N^0.5
        for j in range(1, int((2 * i) ** 0.5) + 1) :
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
            
    if min(dp[N]) == float('inf') :
        print(-1)
    else :
        print(min(dp[N]))                