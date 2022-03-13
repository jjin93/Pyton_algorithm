import sys
# 최대 수 지정해서 소수들 구해서 빈배열에 저장
def prime(n):
    arr = [True]*(n+1)

    for i in range(2, n+1):
        if arr[i] == True:
            j =2

            while(i*j)  <= n:
                arr[i*j]=False
                j+=1

    return arr
list1 = []
list2 =[]
N = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split()[:N]))
arr = prime(1000)
for i in range(2,len(arr)):
    if arr[i] ==True:
       list2.append(i)

count = 0
for i in range(len(list1)):
    
    if list1[i] in list2:
        count += 1
print(count)        
        