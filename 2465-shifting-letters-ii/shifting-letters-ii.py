class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        final = [0]*(len(s)+1)

        for st, end, d in shifts:
            if d == 0:
                final[st] -=1 
                final[end+1] += 1
            else:
                final[st] +=1 
                final[end+1] -= 1
        
        summ = 0
        for i in range(len(s)):
            summ += final[i]

            newChar = ((ord(s[i]) + summ - 97)%26) +97
            s = s[:i] + chr(newChar) + s[i+1:]

        return s

        # instead of iterating through the range, we can add a +1 if we are moving forward in the beginning of the range and -1 
        # in the end of the range to make sure we are no longer applying the change.
        #  The same thing goes for the backward direction with the -1 at the beginning and +1 at the end.