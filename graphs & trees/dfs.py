""" graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

The time complexity of the DFS algorithm is represented in the form of O(V + E), where V is the number of nodes and E is the number of edges.

The space complexity of the algorithm is O(V)  """


def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)
    return visited

dfs(graph, '0', None)
