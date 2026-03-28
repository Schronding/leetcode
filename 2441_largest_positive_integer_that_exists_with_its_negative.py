# Test cases
nums_0 = [-1,2,-3,3]
# Expected output: 3

nums_1 = [-1,10,6,7,-7,1]
# Expected output: 7

nums_2 = [-10,8,6,7,-2,-3]
# Expected output: -1

class Solution:
    def findMaxK(nums: list[int]) -> int:
        positive_set, negative_set = set(), set()
        for number in nums:
            if number > 0:
                positive_set.add(-number)
            else:
                negative_set.add(number)
        common_elements = positive_set & negative_set
        if common_elements:
            return min(common_elements) * -1
        else:
            return -1
    
    print(findMaxK(nums_0))
    print(findMaxK(nums_1))
    print(findMaxK(nums_2))
    
            #print(f"positive_set: {positive_set}    negative_set: {negative_set}    common_elements: {common_elements}")
