class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sor_w=sorted(words,key=len)
        n=len(sor_w)
        sub=[]
        for i in range(n-1):
            for j in range(i+1,n):
                if sor_w[i] in sor_w[j]:
                    sub.append(sor_w[i])
        return list(set(sub))