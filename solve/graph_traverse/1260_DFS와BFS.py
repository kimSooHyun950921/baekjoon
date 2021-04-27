#시작 9시 2분
#코딩 완료 9시 21분
#디버깅 완료 10시 36분
#뭔가 더 효율적인 방법이 필요하긴함..
import sys
import heapq
import copy
input = sys.stdin.readline


def dfs(graph, start):
    stack = [-start]
    visited = [False] * (len(graph.keys()) + 1)
    result = []
    while len(stack) > 0:
        vertex = stack.pop()
        if not visited[abs(vertex)]:
            visited[abs(vertex)] = True
            result.append(abs(vertex))
        while len(graph[vertex]) > 0:
            adjacement_vertex = abs(heapq.heappop(graph[vertex]))
            if not visited[abs(adjacement_vertex)]:
                stack.append(-adjacement_vertex)
    return result


def bfs(graph, start):
    queue = [start]
    visited = [False] * (len(graph.keys()) + 1)
    result = []
    while len(queue) > 0:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
        while len(graph[vertex]) > 0:
            adjacement_vertex = abs(heapq.heappop(graph[vertex]))
            if not visited[abs(adjacement_vertex)]:
                queue.append(adjacement_vertex)
    return result


def main():
    graph = dict()
    bfs_graph = dict()
    vertex, edge, start_vertex = map(int, input().rstrip().split(" "))
    # make vertex
    for i in range(vertex):
        graph[-(i+1)] = list()
        bfs_graph[(i+1)] = list()
    for i in range(edge):
        start, end = map(int, input().split(" "))
        heapq.heappush(graph[-start], -end)
        heapq.heappush(graph[-end], -start)
        heapq.heappush(bfs_graph[start], end)
        heapq.heappush(bfs_graph[end], start)

    print(*dfs(graph, start_vertex))
    print(*bfs(bfs_graph, start_vertex))

if __name__ == "__main__":
    main()