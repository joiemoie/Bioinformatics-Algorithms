# frequency.py
# Jeff Parker      Jan 2009
#
# Count the frequency of each base in a sequence found in a Fasta File
# This uses a command line parameter to hold the file name
# 
# Bugs: no validation that the file is a Fasta DNA file.
#       Assumes contents are a, c, g, and t.
# 
# Usage: To run on the Fasta file "EcoliK12.fasta", type
#       % python frequency.py EcoliK12.fasta

import sys      # Used for Command Line Parameters

debug = False

# How frequently does each character in text appear?
def countChars(text):
    # Create an empty dictionary
    symbolCounts = {}

    # Go over each letter in the sequence
    for ch in text:
        # Increment count
        if (ch in symbolCounts):
            symbolCounts[ch] = symbolCounts[ch] + 1
        else:
            symbolCounts[ch] = 1

    # Return dictionary with the counts
    return symbolCounts

# Print the contents of a Dictionary 
# We are assuming that it holds only the bases ACGT
def printDict(dict):

    # Create a list of symbols to define the order
    symbols = ['A', 'C', 'G', 'T']

    # Iterate over the list of symbols in order
    for ch in symbols:

        # For each member, if the member is in the dictionary
        if (ch in dict):
            print ch, dict[ch]
        else:
            print ch, 0

if (len(sys.argv) != 2):
    print "Usage: python", sys.argv[0], "<filename>"
else:
    # Get the file name from the command line
    fileName = sys.argv[1]

    # Echo print the filename
    if (debug):
        print fileName

    # Open the file
    with open(fileName, 'r') as f:

        # Read the first line of the file
        # First line in Fasta Format describes the file
        text = f.readline().strip()

        # Echo print the first line 
        if (debug):
            print "Saw", text

        # Read the rest of the file in one gulp
        # This program could process one line at a time
        # Later problems are simpler if we have a single string
        text = f.read()

        # Remove whitespace
        text = text.strip()

        # Convert to Upper Case
        text = text.upper()
    
        # Call our function to count the characters
        dict = countChars(text)

        # Call our function to print the results
        printDict(dict)
