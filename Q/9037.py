T = int(input())


for i in range(T):
    N = int(input())  # 아이의 인원
    C = list(map(int, input().split()))  # 각 아이들이 초기에 가지고 있는 사탕의 개수
    cnt = 0
    while C.count(C[0])!= N:

        cnt+=1
    print(cnt)