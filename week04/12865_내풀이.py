import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    num , bag_weight = map(int, input().split())
    products = []
    
    for _ in range(num) :
        products.append(list(map(int,input().split())))
    
    d = [[0]* (bag_weight + 1) for i in range(len(products) + 1)]   
        
 
    for i, product in enumerate(products) :
        product_weight, product_value = product[0],product[1]
        for j in range(1, bag_weight +1):
            if j >= product_weight :
                if d[i][j] > d[i][j - product_weight] + product_value :
                    d[i+1][j] = d[i][j] 
                else :
                    d[i+1][j] = d[i][j- product_weight] + product_value
            else :
                d[i+1][j] = d[i][j]    
                   
    print(d[-1][bag_weight])
    
        
        