#this only looks for reading frames in the forward direction

import string
import sys


limit = 300    

#start codon: ATG
#stop codon: TAA, TGA, TAG
# findAllORF

    
def findAllOrfs(text, limit):
    lst = []
    stops = ["TAA", "TGA", "TAG"]
    
    i = 0
    while i < 3:
        x = i
        
        while x<len(text):
            if(text[x:x+3]=="ATG"):
                y = x + 3
                while y < len(text):
                    if (text[y:y+3] in stops):
                        if (y+3-x > limit):
                            lst.append("+" + str(x%3+1) + " "+str(x+1)+" "+str(y+3)+" "+str(y+1-x)+" "+text[x:x+45])
                            break
                        break
                    y+=3
                x = y+3
            x+=3
        i+=1

    return lst

if ((len(sys.argv) < 2) or (len(sys.argv) > 3)):
    print "Usage: python", sys.argv[0], "<filename> [<min ORF length>]"
else:
    fileName = sys.argv[1]
    if (len(sys.argv) > 2):            
        try:
            limit = int(sys.argv[2])    
        except ValueError:             
            print "\n\tExpecting an integer to define min ORF length, found",
            print sys.argv[2]
            sys.exit(0)                 # Canopy doesn't like this call

    print "ORF must be at least", limit, "Base pairs long"
    
    # Read the file   
    with open(fileName, 'r') as f:
 
        text = f.readline().strip()
        print "Saw", text

        text = f.read()
        text = text.strip()
        text = text.replace('\n','')
    
        lst = findAllOrfs(text, limit)

	print "Open Reading Frames found:"
	print lst
