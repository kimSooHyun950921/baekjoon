# 시작 15 시 10분
# 문제해석시간 15시 26분
# 코드생각시간 15시 35분
# 코드만드는시간 15시 51분
# 디버깅시간 12시 13분
# 문제파악이 오래걸림....
import sys
inputs = sys.stdin.readline


def bfs(tree, num_of_node):
    parent_node = [0] * num_of_node
    queue = [1]
    while len(queue) > 0:
        parent = queue.pop(0)
        child_nodes = tree[parent]
        for node in child_nodes:
            if parent_node[node-1] == 0:
                parent_node[node-1] = parent
                queue.append(node)
    return parent_node


def main():
    num_of_node = int(inputs())
    tree = dict()
    for i in range(num_of_node):
        tree[i+1] = list()
    for i in range(num_of_node-1):
        node_1, node_2 = map(int, inputs().strip().split(" "))
        tree[node_1].append(node_2)
        tree[node_2].append(node_1)
    nodes = bfs(tree, num_of_node)
    for node in nodes[1:]:
        print(node)


if __name__ == "__main__":
    main()
