# Test cases
arr_0 = [1,2,3,5]
k_0 = 3
# Expected output: [2,5]

class Solution:
    def kthSmallestPrimeFraction(arr: list[int], k: int) -> list[int]:
        possible_fractions = []
        for dividend in arr:
            for divisor in arr[1:]:
                possible_fractions.append(dividend/ divisor)
        possible_fractions.sort()
        return possible_fractions[k - 1]
    
    print(kthSmallestPrimeFraction(arr_0, k_0))
