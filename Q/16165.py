# 첫 번째 줄에는 총 입력 받을 걸그룹의 수 N(0 < N < 100)과 맞혀야 할 문제의 수 M(0 < M < 100)을 입력받는다.
#
# 두 번째 줄부터는 각 걸그룹마다 팀의 이름, 걸그룹의 인원 수, 멤버의 이름을 한 줄씩 차례대로 입력받는다.
# 팀과 멤버의 이름은 최대 100글자이며, 모든 글자는 알파벳 소문자이다. 하나의 걸그룹이나
# 서로 다른 두 걸그룹에 이름이 같은 두 멤버가 있는 경우는 없다.
#
# 그 다음 줄부터는 M개의 퀴즈를 입력받는다. 각각의 퀴즈는 두 줄로 이루어져 있으며,
# 팀의 이름이나 멤버의 이름이 첫 줄에 주어지고 퀴즈의 종류를 나타내는 0 또는 1이 두 번째 줄에 주어진다.
# 퀴즈의 종류가 0일 경우 팀의 이름이 주어지며, 1일 경우 멤버의 이름이 주어진다.


N,M = map(int, input().split())
dict = {}
Q = {}
for i in range(N):
    GN = input()
    list = []
    for j in range(int(input())):
        list.append(input())
    list.sort()
    dict[GN] = list

for k in range(M):
    QN,QF = input(),int(input())
    Q[QN]=QF

for i,j in Q.items():
    if j == 1:
        for k in dict:
            if dict[k].count(i) >0:
                print(k)
    else:
        for l in dict[i]:
            print(l)

# Answer
N,M = map(int,input().split())

team_mem, mem_team= {},{}
for i in range(N):
    team_name,mem_num =input(),int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name ,q = input(),int(input())
    if q:
        print(mem_team[name])
    else :
        for m in sorted(team_mem[name]):
            print(m)