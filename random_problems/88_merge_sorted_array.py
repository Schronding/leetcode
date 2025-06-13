# **Input:** 
nums_10 = [1,2,3,0,0,0]
m_10 = 3
nums_20 = [2,5,6] 
n_20 = 3

# Expected **Output:** [1,2,2,3,5,6]

nums_11 = [1]
m_11 = 1
nums_21 = [] 
n_21 = 0

# Expected **Output:** [1]

nums_12 = [0]
m_12 = 0
nums_22 = [1] 
n_22 = 1

# Expected **Output:** [1]

nums_13 = [1,0]
m_13 = 1
nums_23 = [2] 
n_23 = 1

# Expected **Output:** [1, 2]

nums_14 = [2,0]
m_14 = 1
nums_24 = [1] 
n_24 = 1

# Expected **Output:** [1, 2]


def merge(nums1, m, nums2, n):
    one_pointer = m - 1
    two_pointer = n - 1
    change = m + n - 1
    value_one = 0 
    while two_pointer > -1:
        if one_pointer > -1:
            value_one = nums1[one_pointer]
        else:
            value_one = -1000
        if nums2[two_pointer] >= value_one:
            nums1[change] = nums2[two_pointer]
            change -= 1
            two_pointer -= 1
        else:
            nums1[change] = value_one
            change -= 1
            one_pointer -= 1
    

merge(nums_10, m_10, nums_20, n_20)
print(nums_10)

merge(nums_11, m_11, nums_21, n_21)
print(nums_11)

merge(nums_12, m_12, nums_22, n_22)
print(nums_12)

merge(nums_13, m_13, nums_23, n_23)
print(nums_13)

merge(nums_14, m_14, nums_24, n_24)
print(nums_14)