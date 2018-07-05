import sys 

debug = False

# counts the number of TATAATs
def countTATAAT(text):
    data = []
    count = text.count('TATAAT')
    positionOne = text.find('TATAAT')
    positionTwo = text.rfind('TATAAT')
    
    data.append(count)
    data.append(positionOne)
    data.append(positionTwo)
    return data


# prints the data
def printData(data):
    print "Total TATAATs: " + data[0]
    print "Position for first TATAAT: " + data[1]
    print "Position for final TATAAT: " + data[2]
    
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
        data = countTATAAT(text)

        # Call our function to print the data
        printData(data)
