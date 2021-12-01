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
        if dp[-1] < arr[i] :
            dp.append(arr[i])
        else :
            # 자동으로 오름차순으로 정렬이 되있는 dp 배열에 이분탐색을 써서 최신화를 한다.
            idx = bisect.bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    
    print(len(dp))        
