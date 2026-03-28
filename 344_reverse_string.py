# Test cases
s_0 = ["h","e","l","l","o"]
# Expected output: ["o","l","l","e","h"]

s_1 = ["H","a","n","n","a","h"]
# Expected output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(s: list[str]) -> None:
        left_pointer, right_pointer = 0, len(s) - 1
        for _ in range(len(s) >> 1):
        # As we only need to iterate through half of the size of 's' (rounding down; that is why I used the bitwise operator '>>') the time complexity is ...
        # ... O(n), when n is the size of my input (in this case a string). 
        # However, as I don't use any extra memory (note how the swap is made "in-place") my memory complexity is constant, O(1), which is what the problem ...
        # ... is asking for. 
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            # In python we have this beautiful syntax that allow us to swap two elements simultaneously, without having to initialize a temporary variable ...
            # ... to do so. 
            left_pointer += 1
            right_pointer -= 1
        ## As the list is modified we don't really have to return anything. 
                
    print(reverseString(s_0))
    print(reverseString(s_1))
        