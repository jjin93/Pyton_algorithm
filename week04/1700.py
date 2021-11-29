import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    # N : 멀티탭 구멍의 수, K : 전기 용품 총 사용 횟수
    N, K = map(int, input().split())
    
    # 전기 용품 사용 순서를 K_list에 담는다.
    K_list = list(map(int,input().split()))
    
    #현재 플러그인 되어있는 멀티탭 리스트 이다.
    multitap = []
    count = 0
    for i in range(K) :
        if K_list[i] in multitap :
            continue
        
        if len(multitap) < N :
            multitap.append(K_list[i])
            continue
    
        to_be_using = []
        for j in range(N) :
            # 사용 하고 있는 전기 용품이 향후 사용 순서에 있다면
            if multitap[j] in K_list[i:] :
                # 해당 인덱스를 to_be_idx에 담아준다
                to_be_idx = K_list[i:].index(multitap[j])
            else :
                to_be_idx = 101
                    
            to_be_using.append(to_be_idx)
    
        change = to_be_using.index(max(to_be_using)) 
    
        del multitap[change]
    
        multitap.append(K_list[i])
    
        count += 1   
    print(count)
