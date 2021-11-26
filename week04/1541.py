import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    # 문자열에서 -를 기준으로 슬라이싱 해준다.
    # 최소값을 구할려면 가장 큰수를 - 주면 된다.
    form = input().strip().split('-')
    num = []
    for i in form :
        result = 0
        num1 = i.split('+')
        for j in num1 :
            result += int(j)
        num.append(result)
    n = num[0]
    for i in range(1, len(num)):
        n -= num[i]
    
    print(n)            
        
    