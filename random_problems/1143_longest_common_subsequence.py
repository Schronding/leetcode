def longestCommonSubsequence(text1, text2):
    dp = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1] 
            else:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])
    return dp[0][0]

text_00 = "abcde"
text_01 = "ace"

print(longestCommonSubsequence(text_00, text_01))

text_10 = "abc"
text_11 = "abc"

print(longestCommonSubsequence(text_10, text_11))


text_20 = "abc"
text_21 = "def"

print(longestCommonSubsequence(text_20, text_21))
