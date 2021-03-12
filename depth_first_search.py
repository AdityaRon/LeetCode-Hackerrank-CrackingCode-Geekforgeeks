# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


def dfs_path(graph):
    visited = set()
    result = []
    def dfs(graph, visited, node):
        if node not in visited:
            visited.add(node)
            return(node)
            for neighbor in graph[node]:
                dfs(graph, visited, neighbor)
    return result.append(dfs_path(graph, visited, 'A'))
                
