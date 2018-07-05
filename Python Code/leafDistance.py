def parseString(str):
    pair = []
    pair.append(int(str.split("->")[0]))
    pair.append(int(str.split("->")[1].split(":")[0]))
    pair.append(int(str.split("->")[1].split(":")[1]))
    return pair

def parseStringMult(str):
    pairs = []
    for pair in str.split("\n"):
        pairs.append(parseString(pair))
    return pairs 
    
def findDist(input, leaf1, leaf2):
    if(leaf1 == leaf2):
        return 0
    newLeaf1 = leaf1
    newLeaf2 = leaf2
    distance = 0
    if(leaf1<leaf2):
        index = 0
        for x in range(0,len(input)):
            if(input[x][0]==leaf1 and input[x][1]>leaf1):
                index = x
                distance = input[x][2]
                break
        newLeaf1 = input[index][1]
    else:
        index = 0
        for x in range(0,len(input)):
            if(input[x][0]==leaf2 and input[x][1]>leaf2):
                index = x
                distance = input[x][2]
                break
        newLeaf2 = input[index][1]
    
    return findDist(input,newLeaf1,newLeaf2)+distance 

# Open the file
with open("sampleInput.txt", 'r') as f:


    first = int(f.readline().strip())
    text = f.read()
    input = parseStringMult(text)
    for y in range(first):
        for x in range(first):
            print findDist(input,x,y),
        print
