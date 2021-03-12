# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
result = set()
def dfs(graph, visited, node):
    if node not in visited:
        visited.add(node)
        result.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, visited, neighbor)
    return result
