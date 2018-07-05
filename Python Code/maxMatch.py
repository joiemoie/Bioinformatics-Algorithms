#!/usr/bin/python
#
# maxMatch.py
# Jeff Parker         Jan 2009
#
# Find the best match
#       % python maxMatch.py pat text1 

import sys      # Used for Command Line Parameters

debug = True

# How many characters match in this position?
def score(str1, str2):
    # Sanity check
    assert(len(str1) == len(str2))
    count = 0;

    for x in xrange(len(str1)):
        if (str1[x] == str2[x]):
            count = count + 1

    return count

# Find the best match for pattern pat in text 
#     Takes pattern and text
#     Returns [spot, score]
def  maxMatch(pat, text):
    best = -1
    spot = -1
    ln = len(pat)
    # Try each possible starting spot in text
    for pos in xrange(len(text) - ln + 1):
        result = score(text[pos:pos+ln], pat);
        if (result > best):
            best = result
            if (debug):
                print "New best score", best, "position", pos, "string", text[pos:pos+ln]
            spot = pos

    return [spot, best]

if (len(sys.argv) != 3):
    print "Usage:   python", sys.argv[0], "<pattern> <text>"
else:
    pattern = sys.argv[1]
    text    = sys.argv[2]
    lst =  maxMatch(pattern, text)
    print "Score:", lst[1], " Position:", lst[0]
    
