class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt = 0
        res = []
        setA, setB = set(), set()
        
        for a, b in zip(A, B):
            setA.add(a)
            setB.add(b)
            cnt = len(setA & setB)  # Count common elements in both sets
            res.append(cnt)
        
        return res
