class Solution:
    def minLength(self, s, numOps):
        i, n, ans = 0, len(s), []

        while i < n:
            j, count = i, 0
            while j < n and s[i] == s[j]:
                count += 1
                j += 1 
            ans.append([int(s[i]),count])
            i = j 

        def function(k):
            total = 0

            if k == 1:
                for i in range(n):
                    if int(s[i]) == i%2:
                        total += 1 
                return min(total,n-total) <= numOps

            return sum([j//(k+1) for i,j in ans]) <= numOps

        low, high = 1, 10**5 

        while low <= high:
            mid = (low+high)//2 

            if function(mid):
                high = mid - 1 
            else:
                low = mid + 1 

        return low 