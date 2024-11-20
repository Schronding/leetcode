# Case 2
arr_1 = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
k_1 = 4

class Solution:
	def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        sorted_array = sorted(arr, reverse = True)
        def replaceValues(array, desired_value, index):
            limit = 0
            while limit < k:
                if desired_value > array[index - 1]:
                    array[index - 1] = desired_value
                elif desired_value > array[index + 1]:
                    array[index + 1] = desired_value
        for value in sorted_array:
            for index, value in enumerate(arr):
                if value == item:
                    if value > arr[index - 1]:
                        arr[index - 1] = value
                    elif value > arr[index + 1]:
                        arr[index + 1] = value


