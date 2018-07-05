# match3.py
#
# Jeff Parker         Jan 2015
#
# Look for match between pattern and stirng
#     Fixes bug the left outer loop too soon

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

# Report the score
def reportScore(pat, text):
    if (findMatch(pat, text) > -1):
        print "Found pattern", pat, "in text", text, findMatch(pat, text)
    else:
        print "No match between pattern", pat, "and text", text

# Find the position of an exact match
def findMatch(pattern, text):

    if (debug):
        print pattern, text
    patLen = len(pattern)
    for pos in range(len(text) - patLen + 1):
        if (debug):
            print pattern, text[pos:pos+patLen]
        if (0 == score(pattern, text[pos:pos+patLen])):
            return pos

    # Didn't find anything: return -1
    return -1

# Simplify the testing: define function reportScore()
reportScore("one",   "onetwothree") 
reportScore("two",   "onetwothree") 
reportScore("three", "onetwothree") 
