import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    coins, sum_coin = map(int,input().split())
    coin_list = []
    count = 0
    for _ in range(coins):
        coin_list.append(int(input()))
    
    for i in range(len(coin_list)-1,-1,-1):
        count += sum_coin// coin_list[i]
        sum_coin %= coin_list[i]
        
    print(count)    
        
        
        