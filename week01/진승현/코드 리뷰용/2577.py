import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

# 문자열은 list 붙이면 문자단위로 쪼개져서 저장
result =list(str(A*B*C))
# print(result)
count = [0 for i in range(10)]


for i in result:
   for j in range(10):
    #    print(i,j)
    if(int(i) == j):
        count[j] += 1

for i in count:
    print(i)



 




