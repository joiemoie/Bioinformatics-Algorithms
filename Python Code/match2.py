# match2.py
#
# Jeff Parker         Jan 2015
#
# Look for a perfect match between pattern and string

# Are we debugging?
debug = False

# How many differences between str1 and str2
def score(str1, str2):
    # count holds the number of differences
    count = 0

    # Compare characters
    for x in range(len(str1)):
        # Are these two the same?
        if (str1[x] != str2[x]):
            # No: we have seen a new difference
            count = count + 1

    return count

# Look for the first exact match, if any
# Does this work correctly?
def findMatch(pattern, text):

    if (debug):
        print pattern, text
    patLen = len(pattern)
    for pos in range(len(text) - patLen):
        if (debug):
            print pattern, text[pos:pos+patLen]
        if (0 == score(pattern, text[pos:pos+patLen])):
            return pos

    # Didn't find anything: return -1
    return -1

if (findMatch("one", "onetwothree") > -1):
    print "Match between", "one", "onetwothree", findMatch("one", "onetwothree") 
else:
    print "No Match between", "one", "onetwothree"

if (findMatch("two", "onetwothree") > -1):
    print "Match between", "two", "onetwothree", findMatch("two", "onetwothree") 
else:
    print "No Match between", "two", "onetwothree"

if (findMatch("three", "onetwothree") > -1):
    print "Match between", "three", "onetwothree", findMatch("three", "onetwothree") 
else:
    print "No Match between", "three", "onetwothree"
