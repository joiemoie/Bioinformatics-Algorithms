#!/usr/bin/python
#       If we make this file executable, the line above
#       allows you to run this as an executable
# Two ways to run this
#       % python match1.py
#       % ./match1.py
#
# match1.py
# Jeff Parker         Jan 2015

# How many differences are there between str1 and str2?
# The function score takes two parameters, str1 and str2
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

# Some sample calls:
print "one", "two", score("one", "two")
print "cow", "dog", score("cow", "dog")
print "dog", "cow", score("dog", "cow")

print "One", "One",
if (score("One", "One") == 0):
    print "Same"
else:
    print "Different"

print "one", "only", score("one", "only")
print "only", "one", score("only", "one")
