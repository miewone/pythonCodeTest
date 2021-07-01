# N 문제의 갯수
# L 현정이의 역량
# K 풀 수 있는 문제의 최대 개수
N,L,K = map(int,input().split())
tp=0
for i in range(N):
    sub1,sub2 = map(int,input().split())
    if sub2 <L:
        tp+=140
        if i==K:
            break
    elif sub1 <L:
        tp += 100
        if i==K:
            break

print(tp)