import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    
    test_case = int(input())
    
    for _ in range(test_case) :
        N = int(input())
        coin_list = list(map(int,input().split()))
        M = int(input())
        
        d =[0 for _ in range(M + 1)]
        
        d[0] = 1
        
        for coin in coin_list :
            # M이 만약 10000원이라면 해당 동전보다 작은 금액은 만들수 없으니 시작을 coin으로 하고
            # i가 1씩 증가하면서 dp테이블을 채워나간다.
            # 만약 지금 내가 꺼낸 동전이 11원이고 30원을 만들수 있는지 없는지 볼려면 단순히 30원-11원이
            # 그 전 동전들로 만들수 있다면 가능하다.
            # 현재 11원에서 30원을 만드는 모든 가짓수를 계산할려면 그 전까지의 동전들로 30원을 만들던 가짓수와
            # 30원- 11원 = 19원을 만드는 모든 가짓수를 더해주면 된다.
            for i in range(coin, M+1) : 
                d[i] = d[i] + d[i - coin]
                
        print(d.pop())        