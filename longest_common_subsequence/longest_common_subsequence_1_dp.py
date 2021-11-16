def longestCommonSubsequence(text1, text2):

    m,n = len(text1), len(text2)

    dp=[[0]*(n+1) for z in range(m+1)]

    lcs=[]
    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                dp[i+1][j+1]=dp[i][j]+1
                lcs.append(text1[i])
            else:
                dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
    
    #print("lcs:", ''.join(lcs))
    #print(dp)
    return dp[-1][-1], lcs

#Driver Code
text1 = "qwerta"
text2 = "wrtyba"

y = longestCommonSubsequence(text1, text2)
print(y)