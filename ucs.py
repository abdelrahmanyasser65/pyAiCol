


class graph:
    def __init__(self) -> None:
        self.edgs={}
        self.weight={}

    def neighbors(self,node):
        return self.edgs[node]

    def get_coast(self,from_node,to_node):
        return self.weight[(from_node+to_node)]   
    

from queue import PriorityQueue

def ucs(graph,start,goal):
    visited=set()
    queue=PriorityQueue()
    queue.put([0,start])

    while queue:
        cost,node=queue.get()
        if node not in visited:
            visited.add(node)

            if node==goal:
                break
            
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    total_coast=cost +graph.get_cost(node,neighbor)
                    queue.put((total_coast,neighbor))
    return visited