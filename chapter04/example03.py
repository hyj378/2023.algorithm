# 12: 48
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
# 1: 26