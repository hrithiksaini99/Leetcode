class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        for [u,v] in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            ans.append(curr)

            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return len(ans) == n
