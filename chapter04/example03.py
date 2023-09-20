# 본 코드는 적정 풀이 시간이 40분이며 2023년 9월 20일 12시 48분에 풀이를 시작하여 13시 26분에 풀이를 마쳤습니다. (총 38분)
# 2023년 9월 18일에 동일 문제 풀이를 시도했으나, 풀이를 실패했으며 그 원인은 문제에 대한 잘못된 이해입니다.
# 18일 당시 문제의 동,서,남,북과 좌표간의 맵핑 과정에 실수가 있었습니다.
# 20일 문제 풀이 성공은 문제 이해에 집중했으며, 특히 제공된 예제를 통해 알고리즘에 대한 본인의 이해가 맞는지 확인하며 발생할 수 있는 실수를 없앴습니다.
# 해당 문제와 같은 "구현 문제"의 경우 문제에 대한 이해가 관건임을 다시한번 확인했습니다.
# 1. 체크 할 포지션을 check_position 현재 포지션을 now_position 으로 명시적으로 지정한 것이 쉬운 구현에 도움을 준 것 같습니다
# 2. 포지션 count에 대해 매 loop 마다 확인하며 한 loop에는 하나의 작동만 하도록 구현한 점, direction 회전의 위치 등을 깔끔하게 잘 구현한 듯 합니다.
# 해당 문제의 알고리즘 풀이방식을 다시 진행해 보아도 좋을 것 같습니다.
def turn_left(d):
    d = d - 1
    if d < 0:
        d = 3
    return d
    
# argument
# 1. direction vector
d2v_table = {
    0: (-1, 0), \
    1: (0, 1), \
    2: (1, 0), \
    3: (0, -1)
}

# get the state
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# build map
map_type = []
map_visited = []
for ni in range(n):
    _buff_input = list(map(int, input().split()))
    map_type.append(_buff_input)
    map_visited.append([0 for _ in range(m)])

# find the results
count = 0
check = 0
while True:
    # print(f'the position {(a, b)} and direction {d}')
    if check >= 4:
        check_p = (a-d2v_table[d][0], b-d2v_table[d][1])
        if map_type[check_p[0]][check_p[1]] == 1:
            break
        a, b = check_p
        check = 0
        

    # 현재 위치 (a, b)
    # 현재 방향 d
    d = turn_left(d)
    now_p = (a, b)
    check_p = (a+d2v_table[d][0], b+d2v_table[d][1])
    if map_visited[now_p[0]][now_p[1]] == 0:
        count += 1
        map_visited[now_p[0]][now_p[1]] = 1
    # algorithm
    if map_type[check_p[0]][check_p[1]] == 1:
        check += 1 # is the sea
        continue
    if map_visited[check_p[0]][check_p[1]] == 1:
        check += 1 # is already visited
        continue
    a, b = check_p
    check = 0
    # print(check_p)
    
print(count)
