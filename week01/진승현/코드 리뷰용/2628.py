import sys
x, y = map(int,sys.stdin.readline().split())

x_list = [0,x]  #가로 각각 길이
y_list = [0,y]  #세로 각각 길이

for _ in range(int(sys.stdin.readline())):
    xy , length = map(int,sys.stdin.readline().split())
    if xy == 0:
        y_list.append(length)
    else :
        x_list.append(length) 

x_list.sort() # 낮은 수 부터 정렬
y_list.sort()

max_square = 0
for i in range(1,len(x_list)):
    for j in range(1,len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        #밑에가 멋진 문장
        max_square = max(max_square, width*height)

print(max_square)

    




