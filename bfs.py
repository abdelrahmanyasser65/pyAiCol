graph1={
    'A':['B','C'],
    'B':[],
    'C':['D','E'],
    'D':[],
    'E':[]
}

def bfs_path(graph,start,goal):
    visited=[]
    queue=[start]
    while len(queue)>0:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
        if node==goal:
            break
        children=graph[node]
        for child in children:
            queue.append(child)   

    return visited


bfs=bfs_path(graph1,'A','D')
print(bfs)