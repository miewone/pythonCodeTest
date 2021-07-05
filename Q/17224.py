# N 문제의 갯수
# L 현정이의 역량
# K 풀 수 있는 문제의 최대 개수
N, L, K = map(int, input().split())
AQ = []
tp = 0
cnt = 0
for i in range(N):
    list = []
    sub1, sub2 = map(int, input().split())
    list.append(sub1)
    list.append(sub2)
    AQ.append(list)

for i in range(1, -1, -1):
    for j in range(N):
        if cnt == K:
            break
        if AQ[j][i] <= L:
            if i == 1:
                AQ[j][i - 1] = L + 1
                tp += 140
                cnt += 1
            else:
                tp += 100
                cnt += 1
print(tp)

# Answer

easy, hard = 0, 0
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

ans = min(hard, K) * 140

if hard < K:
    ans += min(K - hard, easy) * 100

print(ans)

# https://www.acmicpc.net/problem/17224 풀이

# N=문제 수, L=역량, K=풀 수 있는 최대 문제 수
N, L, K = map(int, input().split())

SOL = 0

sub1 = list()
sub2 = list()

for i in range(N):
    a, b = map(int, input().split())
    if b > L:
        if a <= L:
            sub1.append(a)
    elif b <= L:
        sub2.append(b)


sub1.sort()
sub2.sort()

solve = 0
score = 0
## 풀 수 있는 문제까지

PROB = len(sub1) + len(sub2)
if K > PROB:
    K = PROB

while solve < K:
    hund = K - len(sub2)

    for j in range(len(sub2)):
        solve += 1
        score += 140

    for j in range(hund):
        solve += 1
        score += 100

print(score)