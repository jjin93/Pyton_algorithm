"""가장 긴 증가하는 부분 수열 연습"""
import sys
import bisect
input = sys.stdin.readline

if __name__ == '__main__' :
    N = int(input())
    arr = list(map(int,input().split()))
    dp = []
    # 빈 dp를 만들고 첫번째 값을 먼저 넣어준다.
    dp.append(arr[0])
    for i in range(N) :
        if arr[i] > dp[-1] :
            dp.append(arr[i])
        else :
            # 자동으로 오름차순으로 정렬이 되있는 dp 배열에 이분탐색을 써서 최신화를 한다.
            idx = bisect.bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    
    print(len(dp))        

# # """N값이 작을때 이분탐색없이 그냥 하는 방법"""
#     N = int(input())
#     arr = list(map(int,input().split()))
#     dp2 = [1 for _ in range(N)]
    
#     for i in range(N) :
#         for j in range(i) :
#             # 현재 위치 i보다 이전에 있는 원소 (j)가 작은지 확인한다. (크거나 같으면 가장 긴 증가부분 수열이 될 수 없음)            
#             if arr[i] > arr[j] :
#                 # 작다면, 현재 위치의 이전의 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다.
#                 dp2[i] = max(dp2[i], dp2[j] + 1)
    
#     print(max(dp2))            

# LIS의 길이뿐만 아니라 LIS 원소들을 알고 싶으면 어떻게 해야 할까?
#     N = int(input())
#     arr = list(map(int,input().split()))
#     dp = [1 for _ in range(N)]
#     for i in range(N) :
#         for j in range(i) :
#             if arr[i] > arr[j] :
#                 dp[i] = max(dp[i], dp[j] + 1)
#     max_dp = max(dp)
#     print(max_dp)
    
#     max_idx = dp.index(max_dp)
#     lis = []
    
#     while max_idx >= 0 :
#         if dp[max_idx] == max_dp :
#             lis.append(arr[max_idx])
#             max_dp -= 1
#         max_idx -= 1
    
#     lis.reverse()
#     print(*lis)        
    
#     """max_idx의 값부터 시작하여 거꾸로 순회하며 arr의 원소를 추가하면 된다.

# max_dp가 4고, max_idx는 5이므로 arr[5] = 10에서부터 거꾸로 순회하면 된다. 그다음으로 올 원소는 arr[4] = 5, arr[3] = 2, arr[0] = 1이 된다. 

# lis = [10, 5, 2, 1]이며 이걸 뒤집어서 출력하면 원하는 정답을 얻을 수 있다."""
