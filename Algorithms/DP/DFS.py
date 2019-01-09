def DFS(graph, start):
    stacky=[start]
    visited=[]
    
    while len(stacky)!=0:
        vertex = stacky.pop()
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stacky.append(neighbor)
    return visited



if __name__=="__main__":
    graph={1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}
    path = DFS(graph,2)
    print(path)