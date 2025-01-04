class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        while j < len(chars):
            char , length = chars[j], 1
            while j +1 < len(chars) and char == chars[j+1]:
                length += 1
                j += 1
            chars[i] = char
            if length >1:
                lenStr = str(length)
                chars[(i+1) : (i +1+ len(lenStr))] = lenStr
                i += len(lenStr)
            i += 1
            j += 1
        return i