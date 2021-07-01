# 숭고한 알고리즘 캠프 퀴즈 타임이 시작되었다! PS 기초, 동적 계획법, 파라메트릭 서치, 욱제의 생일, 탐색, 그리디,
# 최단경로 알고리즘, 구데기컵, 서로소 집합, 최소 신장 트리, 최소 공통 조상, 세그먼트 트리, 코드포스에서 C++로 높은 수준의
# 난수를 생성하는 방법, 최대 유량, 볼록 껍질, 스타트링크 사무실에 있는 게임용 컴퓨터의 RAM의 총 용량 등등 수많은 주제를
# 총망라하고 있는 이 미니 대회는 수많은 참가자들의 도전으로 오늘도 빛나고 있고, 제출된 OX표의 개수는 셀 수 없을 정도이다.
#
# 운영진들은 이 OX표들을 채점하고, 점수를 계산해낸 다음, 시상식을 진행하며 화기애애하게 행사를 마무리해야 한다.
# 숭고한 알고리즘 캠프 퀴즈 타임에서 OX표의 점수는 다음과 같이 계산된다.
#
# OX표에 N개의 문제들이 있을 때, 1번 문제, 2번 문제, ..., N번 문제 순으로 채점된다.
# 문제는 뒤로 갈수록 어려워지기 때문에, i 번 문제의 기본 점수는 i 점이다.
# 문제를 맞히면 그 문제의 기본 점수(즉 i 번 문제의 경우 i 점)를 획득하며, 틀리면 얻지 못한다.
# 기본 점수와 별개로, '보너스 점수'라는 값이 존재한다. 이는 처음에는 0점이다.
# 문제를 맞히면 그 때의 '보너스 점수'를 획득하고, '보너스 점수'의 값이 1점 증가한다.
# 문제를 틀리면 '보너스 점수'를 얻지 못하고, '보너스 점수'의 값이 0점으로 초기화된다.
# 민성이는 얼떨결에 숭고한 알고리즘 캠프 퀴즈 타임의 OX표를 채점해야 하는 업무를 맡게 되었다. 수많은 OX표를 볼 생각에 머리가
# 지끈거리는 민성이는 프로그램을 세워 이를 자동화하려고 한다. 시상식까지 4시간밖에 남지 않은 민성이를 도와 점수를 계산해주자.

N = int(input())
S = input()
tp,bp = 0,0
for i in range(N) :
    if S[i] == 'X' :
        bp = 0
    elif S[i] == 'O' :
        tp += (i+1) + bp
        bp = bp + 1
print(tp)

#  인강
# for idx,OX in enumerate(S):
#     if OX =='O':
#         tp+=idx+1+bp
#         bp+=1
#     else :
#         bp =0