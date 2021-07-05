S = input()


for i in range(97, 123):
    for j in range(len(S)):
        if S[j] == chr(i):
            print(j,end=" ")

S = list(input()) # 문자 입력받아서 리스트에 삽입
SOL = list() # 정답 넣을 리스트 생성
for i in range(26): # 알파벳 수만큼 for문 실행
    if S.count(chr(97+i)) > 0: # chr(97) = 'a'이므로, +i 해 주면 a부터 z까지 순서대로 확인 가능
        SOL.append(S.index(chr(97+i))) # 리스트 S 안에 해당하는 알파벳이 있다면 위치를 정답 리스트에 삽입
    else:
        SOL.append(-1) # 리스트 안에 해당 알파벳이 없다면 -1 삽입

for i in range(26):
    print(str(SOL[i]), end=" ") # 순서대로 출력, 띄어쓰기로 구