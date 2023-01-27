def LCS(m,n,s,t):
    #creating a DP table
    dp = [[0 in range(m+1)] for j in range(2)]
    res = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (s[i-1] == t[j-1]):
                dp[i%2][j] = dp[(i-1)%2][j-1]+1
                if(dp[i%2][j]>res):
                    res = dp[i%2][j]
                else:
                    dp[i%2][j] = 0
    return res

x = "SAYHELLO"
y = "SAYLO"
m = len(x)
n = len(y)
print(LCS(m,n,x,y))
