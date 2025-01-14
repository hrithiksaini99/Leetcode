class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt = 0
        n  = len(A)
        res = []
        set1, set2 = set(), set()
        for i in range(n):
            if A[i] == B[i]:
                set1.add(A[i])
                set2.add(B[i])    
                cnt += 1
            elif A[i] in set2 and B[i] in set1:
                cnt += 2
            elif A[i] in set2 or B[i] in set1: # if the num in A is seen in B or the num in B is seen in A
                cnt += 1
            res.append(cnt)
            set1.add(A[i])
            set2.add(B[i])
        return res
