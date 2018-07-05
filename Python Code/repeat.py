import profile
import sys 

debug = False

#This method takes a string "a" and checks if it can be found uniquely
#twice in string "b".

def hasString(a, b):
    final = b.rfind(a)
    initial = b.find(a)
    if(final!=-1):
        if(initial!=final):
            return True
    return False
    
#This method returns the largest repeat in the text
def getLargest(text):
        #This stores the current greatest length and string
        max = 0
        largest = ""
        
        #This stores a potential candidate
        tempLargest = ""
        
        #At every position in the text, this creates a substring
        #to be searched for
        for i in range(len(text)):
            
            tempLargest = tempLargest[1:len(tempLargest)]
            j = i+len(tempLargest)+1
            
            #This checks if the text contains the substring twice
            #and continues building on it if so
            while(hasString(tempLargest, text) and j<len(text)):
                tempLargest += text[j]
                j+=1
            tempLargest = tempLargest[0:len(tempLargest)-1]
            
            #If the length of the substring is greater than the current
            #maximum, this stores the current substring
            if len(tempLargest) > max:
                max = len(tempLargest)
                largest = tempLargest
        return largest
        
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
        
        largestRepeat = getLargest(text)
        print "Length: " + str(len(largestRepeat))
        print "Start Location: " + str(text.find(largestRepeat)+1)
        if len(largestRepeat) > 60: print largestRepeat[0:60]
        else: print largestRepeat