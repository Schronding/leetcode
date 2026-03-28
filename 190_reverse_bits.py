# Test cases
n_0 = "00000010100101000001111010011100" # 43261596 
# Expected output: 964176192 (00111001011110000010100101000000)

class Solution:
    def reverseBits(n: int) -> int:
        reversed_string = int(n[::-1])
        return reversed_string & reversed_string
    
    print(reverseBits(n_0))