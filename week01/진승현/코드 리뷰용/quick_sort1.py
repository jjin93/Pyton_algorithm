from typing import MutableSequence
import sys
def qsort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x= a[(left + right) // 2] #피벗(가운데 원소)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr: #값이 아닌 커서 위치를 말한다.
            a[pl],a[pr] = a[pr],a[pl] #자리 바꿈
            pl +=1
            pr -=1 #자리 바꾸고 계속 진행함을 의미, 같을때는 교차가 일어난다

    if left < pr: qsort(a,left,pr) # while 빠져나와서 교차 혹은 같음이 일어난 상태에서 다시 퀵 정렬을 하기 위해 
    #pr은 지금 right에서 피벗을 지나 교차하거나 같은 상태 그래서 left와 비교할 수 있고 qsort할수 있다.
    if pl < right : qsort(a,pl,right)

def quick_sort(a: MutableSequence) -> None:

    qsort(a,0,len(a) - 1) #len(a)-1 의 의미는 입력받은 갯수 배열의 길이 -1이 마지막 인덱스 번호이다.

if __name__ == '__main__':

    num = int(sys.stdin.readline())
    x= [None]* num #배열갯수 정함
    while True :

        try:

            for i in range(num):
        
                x[i] = int(sys.stdin.readline())
            if i == num-1 :
                break    
        except:
            break
    quick_sort(x)    

        # print('오름차순으로 정렬했습니다.')
    
    for i in range(num) :
            # print(f'x[{i}] = {x[i]}')
        print(x[i])


