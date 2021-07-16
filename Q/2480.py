A = list(map(int,input().split()))
B = []
cnt =0
mx = max(A)

for i in range(3):
    t = A.count(A[i])
    if t == 3 :
        B.append(10000+(A[i]*1000))
    elif t == 2 :
        B.append(1000+(A[i]*100))
    elif t == 1:
        B.append(mx*100)

print(max(B))

#choi

dice = list(map(int, input().split()))

if (dice.count(dice[0])==3):
  print (10000+dice[0]*1000)

elif (dice.count(dice[0])==2):
  print (1000+dice[0]*100)

elif (dice.count(dice[1])==2):
  print (1000+dice[1]*100)

else:
  print (max(dice)*100)