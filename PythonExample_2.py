# Find the minimum number of deletions and insertions
# to make two strings match

# Longest Common Subsequence
def lcs(X, Y):
    # Get the length of each string
    m = len(X)
    n = len(Y)

    # L[m][n] contains the length of LCS of X[0..m-1] & Y[0..n-1]
    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):

        for j in range(n + 1):

            if i == 0 or j == 0:
                L[i][j] = 0

            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1

            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]
# end of function


# Function to find minimum number of deletions and insertions
# to transform the first string into the second
def printMinDelAndIns(X, Y):
    m = len(X)
    n = len(Y)
    lcsLength = lcs(X, Y)

    print("Minimum number of deletions  = ", m - lcsLength)
    print("Minimum number of insertions = ", n - lcsLength)


# Driver Code
X = "algorithm"
Y = "arithmetic"
print ("Longest Common Subsequence   = ", lcs(X, Y))
printMinDelAndIns(X, Y)
