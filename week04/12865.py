import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    num , bag_weight = map(int, input().split())
    products = [[0,0]]
    for _ in range(num) :
        products.append(list(map(int,input().split())))
        
    # 이중 배열 만드는 게 포인트!
    d = [[0 for _ in range(bag_weight + 1)] for _ in range(num + 1)]
    
    for i in range(1, num + 1) :
        for j in range(1, bag_weight + 1) :
            weight = products[i][0]
            value = products[i][1]
            
            if j < weight :
                d[i][j] = d[i-1][j]
            else :
                d[i][j] = max(value + d[i-1][j-weight], d[i-1][j])    
    
    print(d[num][bag_weight])
    
    #  내 코드
                
    # products = []
    
    # d = [[0]* (bag_weight + 1) for i in range(len(products) + 1)]   
  
  # products에서 꺼낼게 아니라 인덱스로 접근이 바로 가능했다. 
    # for i, product in enumerate(products) :
    #     product_weight, product_value = product[0],product[1]
    #     for j in range(1, bag_weight +1):
    #         if j >= product_weight :
    #             if d[i][j] > d[i][j - product_weight] + product_value :
    #                 d[i+1][j] = d[i][j] 
    #             else :
    #                 d[i+1][j] = d[i][j- product_weight] + product_value
                   
    # print(d[-1][bag_weight])
    
        
        