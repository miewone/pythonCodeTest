T = int(input())
for i in range(T):
    N = int(input())  # 아이의 인원
    C = list(map(int, input().split()))  # 각 아이들이 초기에 가지고 있는 사탕의 개수
    cnt = 0
    for candySet in range(N):
        if C[candySet] % 2 != 0:
            C[candySet] += 1
    while C.count(C[0]) != N:
        send = [0 for i in range(N)]
        receiver = 0
        for candyMove in range(N):
            if candyMove == N - 1:
                receiver = 0
            else:
                receiver = candyMove + 1
            send[receiver] = int(C[candyMove] / 2)
            C[candyMove] /= 2
        C = [C[j] + send[j] for j in range(len(C))]
        for candySet in range(N):
            if C[candySet] % 2 != 0:
                C[candySet] += 1
        cnt += 1
    print(cnt)


# Answer
def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy += 1
    return len(set(candy)) == 1


def teacher(N, candy):
    tmp_list = [0 for i in range(N)]
    for idx, cd in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_list[(idx + 1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_list[idx]

    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


for i in range(int(input())):
    process()
