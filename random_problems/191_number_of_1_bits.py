# Test cases
n_0 = 11
# Expected output: 3

n_1 = 128
# Expected output: 1

n_2 = 2147483645
# Expected output: 30

class Solution:
    def hammingWeight(n: int) -> int:
        counter = 0
        # The "Hamming weight" is defined as the amount of digits that are different from zero, in this case, that digit is 1. 
        # In my first approach I first transformed the decimal number into its binary representation, however python does it for me once I simply use any ...
        # ... bitwise operator. 
        while n:
        ## The idea behind this code is to do the loop just the amount of times that I do have 1 in my binary representation. 
        ## That makes so the time complexity of this algorithm is O(1) or O(k) where k is the amount of ones. 
            n = n & (n - 1)
            # The magic of this program occurs at the line above. What does it tell me? That I will update 'n' to the AND (&) operation of 'n' itself ...
            # ... and n - 1, as to "substract" a one to add it to my 'counter' variable. 
            ## Why does this work? The AND operator only outputs 1, when both of its inputs are one too. 
            ## Recall that binary are just very long sequences of the combinations of 0s and 1s. 
            ## So when we iterpolate two long strings, we can check on each column independently and use the '&' on that column before going to another. 
            ## That means that on each iteration of the problem we will drastically reduce the scope to what we consider important; it would no longer be ...
            ## ... each digit, it will be the ones that contains two ones. Check the simulation below >> 
            counter += 1
            ### We don't have to worry about 'n' being empty and providing incorrect output when the 'while' loop is never executed, as 'counter' is ...
            ### ... initialized outside of the loop. 
        return counter
    
    print(hammingWeight(n_0))
    print(hammingWeight(n_1))
    print(hammingWeight(n_2))
    
    # >> Let's assume n = 18. The binary representation is 10010
    # [0] n     = 10010
    # [0] n - 1 = 10001 
    # [0] Output: 10000     counter += 1 (counter = 1)

    # [1] n     = 10000     n = 16
    # [1] n - 1 = 01111 
    # [1] Output: 00000     counter += 1 (counter = 2)

    # As the output is 0, our 'while' loop is finished. 
    # Note how we did 2 iterations when the binary representation indeed had just 2 digits of 1. 