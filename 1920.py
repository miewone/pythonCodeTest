N = int(input())
A = list(map(int,input().split()))
M = int(input())
CM = list(map(int,input().split()))
dict = {}
tmpArr = [0 for i in range(M)]
for i in range(N):
    dict[A[i]] = 0
for i in range(M):
    if CM[i] in dict:
        tmpArr[i] = 1
for i in range(M):
    print(tmpArr[i])
