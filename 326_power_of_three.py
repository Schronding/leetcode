import math

# Test cases
n_0 = 27
# Expected output: true

n_1 = 0
# Expected output: false

n_2 = -1

class Solution:
    def isPowerOfThree(n: int) -> bool:
        # In this problem we are asked to check if a number 'n' is a power of three, but what is precisely a power? 
        # 'An integer 'n' is a power of three, if there exists an integer 'x' such that n == 3^x.' 
        # However, the definition doesn't include that the number must also be greater than 0, as negative numbers cannot be powers. 
        # For example, if we had n = -27, we could have -3^3 but that isn't correct under the problem standards. 
        if n <= 0:
            return False
        # That is why if we have a number that is equal or less than 0, we return 'False' as that number cannot be a power of 3. 
        n = math.log10(n) / math.log10(3)
        ## This is where the magic begins: We can infer these equation by the definition they gave us in the problem. 
        ## We are interested in the integer 'x', so lets aislate it. 
        ## As we are working with the decimal system, that means we have a base of 10 digits (0 to 9). 
        ## The "opposite" of an exponential is a logarithm, so we apply log_base10 (or ln to shorten it) to both expressions
        ## ln(n) = ln(3^x) But we know from the properties of logarithms that log_base(a)(m ^ e) = e log_base(a)(m)
        ## Therefore we get that ln(n) = x ln(3). We can divide both sides by ln(3) to leave the 'x' alone. 
        ## Obtaining that ln(n) / ln(3) = x, which is exactly the equation above. We use 'n' instead of a new variable x simply because we don't really need ...
        ## ... any new space. 
        if n.is_integer(): 
        ### As we are dividing, the number we will get in 'n' is a "float" which means that it will have a '.' such as 3.5 or so. 
        ### But recall that we are being asked in the definition to return 'True' if there is an INTEGER that satisfies the conditions. 
        ### with the method 'is_integer()' we will check if what is to the right of our decimal point are ONLY zeroes. 
        ### For example 1.0. If 'n' is indeed an integer, we return 'True' 
            return True
        else:
        ### If it wasn't an integer, we return 'False'. 
            return False

    
    print(isPowerOfThree(n_0))
    print(isPowerOfThree(n_1))
    print(isPowerOfThree(n_2))
    