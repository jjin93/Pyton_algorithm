import sys

input = sys.stdin.readline

def lis(num_list) :
    if not num_list :
        return 0
    
    inf = float("inf")
    dp = [[inf] for _ in range(N+1)]
    dp[0] = -inf
    dp[1] = num_list[0]
    tmp_logest = 1
    
    def solution(low, high, num) :
        if low == high :
            return low
        # 수열이 2,3,1 일때를 생각하자
        elif low + 1 == high :
            return low if dp[low] >= num else high
        
        mid = (low + high) // 2
        
        if dp[mid] == num :
            return mid
        elif dp[mid] < num :
            return solution(mid + 1, high, num)
        else :
            return solution(low, mid, num)
        
    for num in num_list :
        if dp[tmp_logest] < num :
            tmp_logest += 1
            dp[tmp_logest] = num 
        
        else : 
            next = solution(0, tmp_logest, num)
            dp[next] = num 
    return tmp_logest    

if __name__ == '__main__' :
    N = int(input())
    num_list = list(map(int,input().split())) 
    
    result = lis(num_list)
    print(result)
   
                
        