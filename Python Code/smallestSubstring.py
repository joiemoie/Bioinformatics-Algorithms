#The main method we will be using to find the solutions.
def smallestNonMutualSubstring(s1,s2):
    solutions = []
    #Creates the suffix arrays
    suffixArray1 = createSuffixArray(s1,1)
    suffixArray2 = createSuffixArray(s2,2)
    
    #once we find the answer we will break out of the coming loop
    foundAnswer = False
    
    k = 0
    #we make dictionaries that have prefixes of the suffixes, and if there is a prefix
    #in suffixDict1 that is not existent in suffixDict2, we add that as a solution
    while k < len(suffixArray1) and not foundAnswer:
        suffixDict1 = {}
        for i in suffixArray1:
            if len(i) > k:
                suffixDict1[i[:k]+i[len(i)-1]] = suffixDict1.get(i[:k]+i[len(i)-1], 0) + 1
        suffixDict2 = {}
        for i in suffixArray2:
            if len(i) > k:
                suffixDict2[i[:k]+i[len(i)-1]] = suffixDict2.get(i[:k]+i[len(i)-1], 0) + 1        
        for key in suffixDict1:
            if key[len(key)-1] ==str(1):
                if key[:len(key)-1]+str(2) not in suffixDict2:
                    solutions.append(key[:len(key)-1])
                    foundAnswer = True
        k+=1
    return solutions

#Helper method to create a suffix. The stringNumber will let us identify whether it's the first or second string.
def createSuffixArray(s1,stringNumber):
    suffixes = []
    for i in range(len(s1)):
        suffixes.append(s1[i:]+str(stringNumber))
    suffixes.sort()
    return suffixes