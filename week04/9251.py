import sys

input = sys.stdin.readline

if __name__ == '__main__' :
    
    sequence_1 = input().strip()
    sequence_2 = input().strip()
   
    d = [[0]*(len(sequence_1)+1) for i in range(len(sequence_2) + 1)]

    for i in range(1,len(sequence_2) + 1) :
        for j in range(1,len(sequence_1) + 1) :
            if sequence_1[j-1] == sequence_2[i-1] :
                d[i][j] = d[i-1][j-1] + 1
                
            else :
                d[i][j] = max(d[i-1][j], d[i][j-1])
                
               

    print(d[len(sequence_2)][len(sequence_1)])                          
   
   