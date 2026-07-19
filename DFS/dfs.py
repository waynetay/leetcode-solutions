def dfsRec(adj,visited,s,res):
    visited[s] = True
    res.append(s)
    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj,visited,i,res)
def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj,visited,0,res)
    return res 
adj = [[1,2],[0,2],[0,3,4],[2],[2]]
print(dfs(adj))