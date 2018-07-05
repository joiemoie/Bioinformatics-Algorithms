# Turnpike Problem Modification

import profile
import sys

def differences(a): #O(n^2)
    lst = []
    for x in range(len(a)):
        for y in range(x+1, len(a)):
            lst.append(a[y] - a[x])

    lst.sort()
    return lst

def subset(a, b): #O(n)
    if (len(a) > len(b)):
        return False
    if (0 == len(a)):
        return True
    x = 0
    for y in range(len(b)):
        if (a[x] < b[y]):
            return False
        if (a[x] == b[y]):
            x = x + 1
            if (x == len(a)):
                return True
    return False

def extend(cand, lst, depth, debug):
    return extendHelper(cand,lst,depth,debug,differences(cand))
    
#this helper method keeps track of the differences. I'll need this so i can build on the differences later
def extendHelper(cand, lst, depth, debug,diffs):
    if (debug):
        print depth * "    ", "Extend", 
        print cand, diffs, "vs", lst

# changed subset(lst,differences(cand)) to lst==differences(cand)
# it's a very minor tweak    
    if (lst==diffs):
        print "Cand:     ", cand
        print "Generates:", lst
        print
        return True

    failures = [] # this keeps track of numbers that won't work
    for x in reversed(lst): # i reversed the list cutting time by a lot
        if ((x > 0) and (not (x in cand)) and (not (x in failures))):
            nwLst = cand[:]  

            nwLst.append(x)   
            nwLst.sort()       
            if (debug):
                print depth * "    ", "Try to add ", x, "to get", nwLst
            
            #this builds the differences from the old
            nwDiffs = diffs[:]
            for y in cand:
                nwDiffs.append(abs(x-y))
            nwDiffs.sort()
            
            if (subset(nwDiffs, lst)):   
                if (extendHelper(nwLst, lst, depth+1, debug,nwDiffs)):
                    return True
            else: failures.append(x)
    return False

if (len(sys.argv) > 1):
    debug = True
else:
    debug = False


profile.run('extend([0], [1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 8, 8, 8,9, 9, 10, 10, 11, 11, 12, 12, 12, 13, 14, 15, 15, 16, 16, 18, 19, 20, 23], 0, debug)')