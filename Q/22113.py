N,M = map(int,input().split())
B = list(map(int,input().split()))
Money = list()
t=0;
for i in range(N):
    Money.append(list(map(int,input().split())))

for i in range(len(B)-1):
    t += Money[(B[i]-1)][B[i+1]-1]

print(t)