import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    
    N = int(input())
    stair = [0]
    for _ in range(N) :
        stair.append(int(input()))
        
    dp = [0, stair[1]]
    
    if N > 1 :
        dp.append(stair[1] + stair[2])
        
    for i in range(3, N + 1) :
        #마지막 계단은 꼭 밟아야 하므로, 현재 가중치는 무조건 들어가야한다.
        
        dp.append(max(dp[i-2] + stair[i], dp[i-3] + stair[i] + stair[i-1] ))   
        
    print(dp[N])     
            