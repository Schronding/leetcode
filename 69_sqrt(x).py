# **Input:** 
x_0 = 4

# ** Expected Output:** 2

# **Input:** 
x_1 = 8
# **Expected Output:** 2

# **Input:** 
x_2 = 36
# **Expected Output:** 6

def mySqrt(x):
    # Creacion de variables necesarias
    left = 0
    right = x
    best_candidate = 0
    while left <= right:
        mid = left + (right - left) // 2
        mid_squared = mid * mid
        if mid_squared < x:
            best_candidate = mid
            left = mid + 1
        elif mid_squared > x:
            right = mid - 1
        else:
            return mid
    return best_candidate
        




print(mySqrt(x_0))
print(mySqrt(x_1))
print(mySqrt(x_2))