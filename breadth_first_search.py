# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited =[]
queue = []
result = []
def bfs(graph, visited, node):
    visited.append(node)
    queue.append(node)
    while queue:
        temp = queue.pop(0)
        result.append(temp)
        for neighbor in graph[temp]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return result
bfs(graph, visited, 'A')
