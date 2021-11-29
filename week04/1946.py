import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    test_case = int(input())
    for _ in range(test_case) :
        applicant_num = int(input())
        applicant_list = []
        for _ in range(applicant_num):
            record1, record2 = map(int,input().split())
            applicant_list.append((record1,record2))
        # record1 오름차순으로 정렬하고 record2를 비교하면서 합격을 선택하면 된다.
        applicant_list = sorted(applicant_list, key=lambda x : x[0])
        
        pass_count = 0
        cut_line = applicant_num + 1
        for record1, record2 in applicant_list :
            if record2 < cut_line:
                pass_count += 1
                cut_line = record2

        print(pass_count)