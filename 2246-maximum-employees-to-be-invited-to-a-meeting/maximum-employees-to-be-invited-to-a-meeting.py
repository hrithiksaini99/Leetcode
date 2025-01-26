class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg= [0]*n
        chainLen= [0]*n
        vis = [False]*n
        q = deque()
# doing Topological sort
        for f in favorite:
            indeg[f] += 1
        
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            vis[u] = True
            v = favorite[u]
            chainLen[v] = max(chainLen[v], chainLen[u]+1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
        
        max_cycle, pair = 0, 0

        for i in range(n):
            if vis[i]:
                continue
            cycleLen = 0
            current = i

            while not vis[current]:
                vis[current] = True
                current = favorite[current]
                cycleLen+=1
            if cycleLen == 2:
                pair+= 2+ chainLen[i] + chainLen[favorite[i]]
            else:
                max_cycle = max(max_cycle, cycleLen)
        
        return max(max_cycle, pair)

        # https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/6329874/scenario-analysis-topological-sorting-cycle-detection-with-example