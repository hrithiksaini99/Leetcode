class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length of the string is odd, it can't be valid
        if len(s) % 2 == 1:
            return False

        open_count = 0  # Count of open brackets
        close_count = 0  # Count of close brackets

        # First pass: Check from left to right
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                close_count += 1
            
            # If we have more close brackets than open brackets, it's invalid
            if close_count > open_count:
                return False

        open_count = 0
        close_count = 0

        # Second pass: Check from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                open_count += 1
            
            # If we have more open brackets than close brackets, it's invalid
            if open_count > close_count:
                return False

        return True  # If we pass both checks, it's valid
