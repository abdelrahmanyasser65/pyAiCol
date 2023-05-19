


graph1={
    'A':['C','B'],
    'B':[],
    'C':['E','D'],
    'D':[],
    'E':[]
}


def dfs_path(graph,start,goal):
    visited=[]
    stack=[start]
    while len(stack)>0:
        path=stack.pop()
        node=path[-1] 
        if node not in visited:
            visited.append(node)
        if node ==goal:
            break
        children=graph[node]   
        for child in children :
            stack.append(child)
    return visited

dfs=dfs_path(graph1,'A','E')
print(dfs)        