
def shortestPath(graph, u, v, k): 
    V = 4
    INF = 999999999999
      
    if k == 0 and u == v: 
        return 0
    if k == 1 and graph[u][v] != INF: 
        return graph[u][v]  
    if k <= 0: 
        return INF  
  
    res = INF  
  
    for i in range(V): 
        if graph[u][i] != INF and u != i and v != i: 
            rec_res = shortestPath(graph, i, v, k - 1)  
            if rec_res != INF: 
                res = min(res, graph[u][i] + rec_res) 
    return res 

if __name__ == '__main__': 
    INF = 999999999999
      
    graph = [[0, 10, 3, 2], 
             [INF, 0, INF, 7], 
             [INF, INF, 0, 6], 
             [INF, INF, INF, 0]] 
    u = 0
    v = 3
    k = 2
    print("Weight of the shortest path is", 
              shortestPath(graph, u, v, k)) 