# Test cases:
n_0 = 3
# Expected output: ["1","2","Fizz"]

n_1 = 5
# Expected output: ["1","2","Fizz","4","Buzz"]

n_2 = 15
# Expected output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

class Solution:
    def fizzBuzz(n: int) -> list[str]:
        answer = []
        # I first initialize the list that will contain all my answers. 
        for index in range(1, n + 1):
        ## As the problem starts with a '1-indexed' list, I add one to both sides of the 'range()' function; start at 1 and end at 'n + 1'. 
            string = ""
            if index % 3 == False:
            # As 3 is the smallest of the two numbers, I started with it. 
                if index % 5 == False:
                # Here I used 'False' to be pendantic, but the truth is that this 'False' statement is exactly the same as if I were to put a 0.
                    string = "FizzBuzz"
                    # In case my index is divided both by 3 and 5 I only then execute this line, but if it isn't I just return "Fizz" as that is the output ...
                    # ... I expect when it is only divisible by 3. 
                else:
                    string = "Fizz"
            elif index % 5 == False:
                string = "Buzz"
            else:
            ## In case the index is not divisible either by 3 and 5, 3 or 5, I just transform that number into a string. 
                string = str(index)
            answer.append(string)
        return answer
    
    print(fizzBuzz(n_0))
    print(fizzBuzz(n_1))
    print(fizzBuzz(n_2))
    