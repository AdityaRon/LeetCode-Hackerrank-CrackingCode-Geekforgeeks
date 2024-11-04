""" graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

The time complexity of the BFS algorithm is represented in the form of O(V + E), where V is the number of nodes and E is the number of edges.

The space complexity of the algorithm is O(V)

"""

def bfs(graph, start):
    from collections import deque
    visited, queue = set(), deque()
    visited.add(start)
    queue.append(start)
    
    while queue:
        start = queue.popleft()
        for neighbor in graph[start]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

bfs(graph, '0')
