#The main method we will be using to find the solutions.
def longestMutualSubstring(s1):
    solutions = []
    #Creates the suffix arrays
    suffixArray = createSuffixArray(s1)
    
    #once we find the answer we will break out of the coming loop
    foundAnswer = False
    
    k = len(suffixArray)
    #we make dictionaries that have prefixes of the suffixes, and if there is a prefix
    #in suffixDict1 that is not existent in suffixDict2, we add that as a solution
    while k > 0 and not foundAnswer:
        suffixDict = {}
        for i in suffixArray:
            suffixDict[i[:k]] = suffixDict.get(i[:k], 0) + 1     
        for key in suffixDict:
            if suffixDict[key] > 1:
                solutions.append(key)
                foundAnswer = True
        k-=1
    return solutions

#Helper method to create a suffix. The stringNumber will let us identify whether it's the first or second string.
def createSuffixArray(s1):
    suffixes = []
    for i in range(len(s1)):
        suffixes.append(s1[i:])
    suffixes.sort()
    return suffixes