def prime(n):
    arr = [True]*n
    m = int(n **0.5)
    for i in range(2, m+1):
        if arr[i] == True:
            for j in range(i+i,n,i):
                arr[j] = False
    return [i for i in range(2,n) if arr[i] == True]

def sosu(n):
    li= prime(n)
    tmp = max([k for k in range(len(li)) if li[k]<= n/2])
    for x in range(tmp,-1,-1):
        for y in range(x,len(li)):
            if li[x]+li[y] == n:
                return li[x],li[y]


for _ in range(int(input())):
    n=int(input())
    print(" ".join(map(str,sosu(n))))

    # print(" ".join(map(str,sosu(x))))
    # T_list.append(x)
# 입력 받은 숫자 까지의 소수 구하기

# for i in T_list:
#     arr = prime(int(i))
#     prime_number =[]
#     for j in range(2,len(arr)):    
#         if arr[j] ==True:
#             prime_number.append(j)
            # 입력 받은 값까지의 소수 구함
    
    # print(prime_number)
    # print(prime_number[0])
    # print(prime_number[1])
    # print(prime_number[2])

    
    

    # tmp = max([k for k in range(len(prime_number)) if prime_number[k]<= int(i)/2])
    # # print(prime_number[tmp])
    # for x in range(tmp,-1,-1):
    #     for y in range(x,len(prime_number)):
    #         if prime_number[x]+prime_number[y] == i:
    #             print(prime_number[x],prime_number[y])
                

                
                 
    # a= int(i)/2
    # b= int(i)/2
    

    
# print(prime_number)        

            

