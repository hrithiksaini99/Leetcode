class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        t = [[-1]*1001 for i in range(1001)]  #constraint says the limit is 1000
        
        def isPali(i , j):
            if i >= j:
                t[i][j] = 1
                return 1
            if t[i][j] != -1:
                return t[i][j]

            if s[i] == s[j]:
                t[i][j] = isPali(i+1, j-1)
                return t[i][j]

            t[i][j] = 0
            return 0
      


        ans = ""
        maxLen= 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPali(i, j):
                    temp = s[i:j+1]
                    if len(temp) > maxLen:
                        maxLen = len(temp)
                        ans = temp

        return ans 
