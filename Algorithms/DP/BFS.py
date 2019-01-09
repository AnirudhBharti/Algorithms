from collections import deque

def bfs(graph, start):
    Q = deque([start])
    visited=[]
    visited.append(start)

    while(len(Q)!=0):
         vertex = Q.popleft()
         for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                Q.append(neighbor)
    return visited

if __name__ == "__main__":
    graph={1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}
    v=bfs(graph, 1)
    print(v)
