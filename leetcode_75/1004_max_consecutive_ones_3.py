# Test cases
nums_0 = [1,1,1,0,0,0,1,1,1,1,0]
k_0 = 2
# Expected output: 6

nums_1 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k_1 = 3
# Expected output: 10


class Solution:
    def longestOnes(nums: list[int], k: int) -> int:
        allowance = 0
        current, greatest = 0, 0
        right, left = 0, 0
        while right < len(nums):
            if allowance < k:
                if nums[right] == 0:
                    allowance += 1
                right += 1
            else:
                current = (right - left) + 1
                if current > greatest:
                    greatest = current
                while allowance == k:
                    #print(f"left {left}; allowance {allowance}")
                    if nums[left] == 0:
                        allowance -= 1
                    left += 1
        current = (right - left) + 1
        greatest = max(current, greatest)
        return greatest
    
    print(longestOnes(nums_0, k_0))
    print(longestOnes(nums_1, k_1))