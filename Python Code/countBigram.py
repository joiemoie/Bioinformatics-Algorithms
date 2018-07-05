import sys 

debug = False

# counts the number of TATAATs
def countBigram(text):
    data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    data[0] = text.count('AA')
    data[1] = text.count('AC')
    data[2] = text.count('AG')
    data[3] = text.count('AT')
    data[4] = text.count('CA')
    data[5] = text.count('CC')
    data[6] = text.count('CG')
    data[7] = text.count('CT')
    data[8] = text.count('GA')
    data[9] = text.count('GC')
    data[10] = text.count('GG')
    data[11] = text.count('GT')
    data[12] = text.count('TA')
    data[13] = text.count('TC')
    data[14] = text.count('TG')
    data[15] = text.count('TT')
    return data
    
# prints the data
def printData(data):
    print "   A  C  G  T"
    print "A ",
    for x in range(4):
        print str(data[x])+" ",
    print
    print "C ",
    for x in range(4,8):
        print str(data[x])+" ",
    print
    print "G ",
    for x in range(8,12):
        print str(data[x])+" ",
    print
    print "T ",
    for x in range(12,16):
        print str(data[x])+" ",

if (len(sys.argv) != 2):
    print "Usage: python", sys.argv[0], "<filename>"
else:
    fileName = sys.argv[1]
    
    if (debug):
        print fileName

    with open(fileName, 'r') as f:

        text = f.readline().strip()

        if (debug):
            print "Saw", text

        text = f.read()
        text = text.strip()
        text = text.upper()
    
        # Call our function to gather the data
        data = countBigram(text)

        # Call our function to print the data
        printData(data)
