# Rod Cutting Problem with Dynamic Programming

# Returns the best obtainable value for a rod of length n and
# value[] as max values of different lengths
def cutRod(value, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        maxVal = -999
        for j in range(i):
            maxVal = max(maxVal, value[j] + val[i - j - 1])
        val[i] = maxVal

    return val[n]


# Driver code
rodVal = [1, 5, 8, 9, 10, 17, 17, 20]
length = len(rodVal)
print("Maximum Obtainable Value is " + str(cutRod(rodVal, length)))
