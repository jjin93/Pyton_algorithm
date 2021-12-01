import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    
    N  = int(input())
    wine = [0]
    for _ in range(N):
        wine.append(int(input()))
        
    dp = [0, wine[1]]
    
    if N > 1 :
        dp.append(wine[1] + wine[2])
        
    for i in range(3, N + 1) :
        # i-1잔을 안마셨을때, i-2잔을 안마시고, i-1잔을 마셨을때, i-2잔과 i-1잔을 모두 마셨을때를 보고 max를 취한다.
        dp.append(max(dp[i-2]+wine[i], dp[i-1], dp[i-3]+ wine[i] + wine[i-1]))    
            
    print(dp[N])        
            