from collections import defaultdict, deque

class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        group = defaultdict(deque)  
        group_idx = {}
        a = sorted(nums)  
        group_num = 0
        
        # Initialize the first group
        group_idx[a[0]] = group_num
        group[group_num].append(a[0])

        for i in range(1, len(a)):
            if abs(a[i] - a[i - 1]) > limit:
                group_num += 1
            group[group_num].append(a[i])
            group_idx[a[i]] = group_num

        ans = [0] * len(a)  # Initialize the answer array

        for i in range(len(a)):
            groupnum = group_idx[nums[i]]
            smallest_num = group[groupnum].popleft()  # Pop from the front of the deque
            ans[i] = smallest_num

        return ans
