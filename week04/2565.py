import sys
input = sys.stdin.readline
               
if __name__ == '__main__' :
    N = int(input())
    line_list = []
    for _ in range(N):
        line_list.append(list(map(int,input().split())))
    dp = [1 for _ in range(N)]
    line_list.sort()
    
    for i in range(N) :
        for j in range(i) :
            if line_list[i][1] > line_list[j][1] :
                dp[i] = max(dp[i],dp[j] + 1)
    
    
    print(N -max(dp))           
                
