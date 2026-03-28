# Test cases
strs_0 = ["flower","flow","flight"]
# Expected output: "fl"

strs_1 = ["dog","racecar","car"]
# Expected output: ""

strs_2 = [""]


class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        smallest_str, prefix = strs[0], ""
        # As I have certainty from the constraints that 'strs' cannot be empty, I take the freedom to assume the first string in the list could be the ...
        # ... smallest one. 
        for string in strs:
        ## As the prefix has to be COMMON to all the strings, the smallest string is the bottleneck to my prefix; 'prefix' cannot be larger that the ...
        ## ... smallest of my strings. 
            if len(string) == 0:
            # So if there comes a time in which I find an empty string, I know that the only common prefix that string can have is another empty string. 
                return prefix
                # And as I initialized an empty string above, I just need to return it directly if I found such case. 
            elif len(string) < len(smallest_str):
            ## While it could be relatively expensive to check each string directly, as I am looking for the smallest string, this entire 'for' loop ...
            ## ... could save me a lot of time in the second one, as I can reduce the number of iterations in the second loop, or return the correct ...
            ## ... output directly in this loop. 
                smallest_str = string
        for index in range(len(smallest_str)):
        ### This 'index' variable can only be as large as the lenght of our 'smallest_str' - 1, so this program will never run out of bounds.
        ### This loop just creates a poiter 'index' that stays in the same position for each string. 
            for string in strs:
            ### But as we can only compare two things at a time, we nest another loop that has the purpose of going through each string in 'strs', even ...
            ### ... comparing the 'smallest_str' with itself. Why we do this? Because as paradoxical as it might seem, removing the string from 'strs' ...
            ### ... would require a "resize" of the list, which has a O(n) time complexity. 
            ### On the other hand, for the way my nested loop works, I just check for ONE character at a time on each string. 
            ### That comparisson is 0(1) which is much more efficient and has the potential of ending before I have used all the characters in my 'smallest_str'. 
                if smallest_str[index] != string[index]:
                ## In case any one character is different, that means it isn't common, so I know I should return 'prefix' in whatever state it is now. >>
                    return smallest_str[:index]
        return smallest_str
        
    print(longestCommonPrefix(strs_0))
    print(longestCommonPrefix(strs_1))
    print(longestCommonPrefix(strs_2))
    