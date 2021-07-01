N, M = map(int, input().split())
A, B = map(str, input().split())
mergestr = ""
transArr = []
resultArr = []
dic = {"A": 3,"B": 2,"C": 1,"D": 2,"E": 4,"F": 3,"G": 1,"H": 3,"I": 1,"J": 1,"K": 3,"L": 1,"M": 3,"N": 2,"O": 1,"P": 2,"Q": 2,"R": 2,"S": 1,"T": 2,"U": 1,"V": 1,"W": 1,"X": 2,"Y": 2,"Z": 1}
for i in range(0, len(A)):
    if i>=len(A):
        mergestr += B[i:]
        break
    if i>=len(B):
        mergestr += A[i:]
        break
    mergestr += A[i] + B[i]
if i<len(B):
    mergestr += B[i+1:]
for i in range(0, len(mergestr)):
    transArr.append(dic[mergestr[i]])
while len(transArr) > 2:
    for i in range(0, len(transArr) - 1):
        tmp = transArr[i] + transArr[i + 1]
        if(tmp < 10):
            transArr[i] = tmp
        else:
            transArr[i] = tmp%10
    transArr.pop()
if transArr[0] == 0 :
    print(str(transArr[1]) + '%',end='')
else:
    print(str(transArr[0])+str(transArr[1])+'%',end='')