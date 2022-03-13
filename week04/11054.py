import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    N = int(input())
    case = list(map(int,input().split()))
    reverse_case = case[::-1]
    
    increase = [1 for i in range(N)] # 가장 긴 증가하는 부분 수열
    decrease = [1 for i in range(N)] # 가장 긴 감소하는 부분 수열(reversed)
    
    for i in range(N) :
        for j in range(i) :
            if case[i] > case[j] :
                increase[i] = max(increase[i], increase[j] + 1)
            if reverse_case[i] > reverse_case[j] :
                decrease[i] = max(decrease[i], decrease[j] + 1)
                
    result = [0 for i in range(N)]
    for i in range(N) :
        result[i] = increase[i] + decrease[N-i-1] - 1
    
    print(max(result))                    
    
    """문제를 보면 다음과 같이 정의되어있다.

수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다. 
증가하는 수열과 감소하는 수열 두 가지로 나누어서 생각해보자

주어진 수열:  1, 5, 2, 1, 4, 3, 4, 5, 2, 1

증가하는 수열 길이: 1, 2, 2, 1, 3, 3, 4, 5, 2, 1

감소하는 수열 길이: 1, 5, 2, 1, 4, 3, 3, 3, 2, 1

각 인덱스별로 증가하는 수열 길이 + 감소하는 수열 길이의 합이 가장 큰 지점이 바이토닉 수열의 Sk 원소가 된다.

즉, 주어진 수열에서의 바이토닉 수열은 1,2,3,4,5,2,1가 되며, Sk는 5가 된다.

증가하는 수열: 1,2,3,4,5

감소하는 수열: 5,2,1

합을 구하면서 주어진 수열의 8번째 원소인 5를 두 번 계산하였으므로 1을 빼주면 정답을 구할 수 있다."""
