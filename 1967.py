from collections import deque
from sys import stdin


def solution(n, arr):
    result = 0
    # 한 정점에 연결된 다른 정점들 정보
    # 중복 방지 등을 위해 set 사용
    nodes = [set() for i in range(n + 1)]
    total_length = [[set(), set()] for i in range(n + 1)]
    # 큐 초기화
    q = deque()
    # 부모 노드에 자식 노드들 연결
    for n1, n2, lgth in arr:
        nodes[n1].add((n2, lgth))
    # 시작점 위치 큐에 넣어줌
    # 시작점인 경우 -1로 표시
    q.append([1, 1, 0, -1])
    while len(q) > 0:
        # pop
        origin, index, lgth, side = q.popleft()
        # 시작점이 아닌 경우
        if side != -1:
            if side >= len(total_length[origin]):
                while side >= len(total_length[origin]):
                    total_length[origin].append(set())
            # 길이 추가
            total_length[origin][side].add(lgth)
        # 자식 노드들 순회하면서 좌우 방향과 노드, 노드까지 길이 확인
        for lr, tmp in enumerate(nodes[index]):
            next_vertex, nxt_lgth = tmp
            # 시작점인 경우
            if side == -1:
                # 큐에 시작점 / 다음 노드 / 다음 노드까지 길이 / 좌우 방향을 넣어줌
                q.append([origin, next_vertex, lgth + nxt_lgth, lr])
            # 시작점이 아닌 경우
            else:
                # 큐에 시작점 / 다음 노드 / 다음 노드까지 길이 / 원 방향을 넣어줌ㅏ
                q.append([origin, next_vertex, lgth + nxt_lgth, side])
            # 다음 자식 노드를 시작점으로 잡도록 -1로 삽입
            q.append([next_vertex, next_vertex, 0, -1])
    for sets in total_length:
        tmp_result = sorted([max(i) for i in sets if len(i) > 0])
        if len(tmp_result) > 1:
            result = max(result, tmp_result[-1] + tmp_result[-2])
        elif len(tmp_result) == 1:
            result = max(result, tmp_result[-1])
        # 좌우 최대 값 더하기
    return result


# n = int(stdin.readline())
# arr = [map(int, stdin.readline().strip().split()) for i in range(n - 1)]
# print(solution(n, arr))

# 11
print(solution(5, [[1, 3, 2], [3, 4, 3], [4, 2, 4], [4, 5, 6]]))
# 53
print(solution(3, [[1, 2, 3], [1, 3, 50]]))
# 9
print(solution(5, [[1, 5, 5], [5, 2, 2], [5, 3, 3], [5, 4, 4]]))
# 273
print(solution(14, [[1, 3, 90], [1, 5, 80], [1,  6, 70],
                    [1, 13, 60], [2, 4, 20], [2, 7, 18],
                    [3, 12, 100], [6, 10, 9], [6, 14, 11],
                    [13, 2, 3], [13, 8, 2], [13, 9, 1], [13, 11, 4]]))
# 156
print(solution(7, [[1, 5, 100], [3, 7, 3], [5, 6, 50], [6, 2, 5], [6, 3, 3], [6, 4, 4]]))
