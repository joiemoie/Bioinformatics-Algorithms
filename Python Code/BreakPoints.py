def stringToList(string):
    string = string[1:len(string)-1]
    a = string.split()
    b = []
    for i in a:
        b.append(int(i))
    return b
def numberBreakpoints(perm):
    perm = stringToList(perm)
    breakpoints = 2
    i = 0
    while i < len(perm)-1:
        if (perm[i+1]) == perm[i]+1:
            while i<len(perm)-1 and (perm[i+1]) == perm[i]+1:
                i+=1
        elif (perm[i+1]) == perm[i]+1 and perm[i-1]== perm[i]+ 1:
            print perm[i]
            i+=1
            breakpoints += 1
        elif (perm[i+1]) == perm[i]-1 and perm[i-1]== perm[i]- 1:
            print perm[i]
            i+=1
            
            breakpoints += 1
        elif(perm[i+1]) == perm[i]-1:
            while i<len(perm)-1 and (perm[i+1]) == perm[i]-1:
                i+=1
        else:
            print perm[i]
            i+=1
            
            breakpoints+=1
    print breakpoints