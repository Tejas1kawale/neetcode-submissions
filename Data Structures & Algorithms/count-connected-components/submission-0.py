class Solution:

    def dfs(self, node: int, adjList: List[List[int]], visited: List[int]):
        if visited[node]:
            return
        visited[node] = 1
        for adj in adjList[node]:
            if not visited[adj]:
                self.dfs(adj, adjList, visited)
            
        

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [ 0 for _ in range(n)]
        print(visited)
        adjList = [[] for _ in range(n)]
        print(adjList)
        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])
        
        count = 0
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, adjList, visited)
                count += 1
        
        return count 