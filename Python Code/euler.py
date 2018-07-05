#This creates the dictionary
def createDict(str):
    genome = {}
    kmers = str.split("\n")
    for kmer in kmers:
        genome[kmer[:2]] = []
    for kmer in kmers:
        genome[kmer[:2]].append(kmer[1:3])
    return genome

#This calls the helper method
def assembly(genome,firstKmer):
    nextKmer = genome[firstKmer[:2]].pop(0)
    results = []
    assemblyHelper(genome,nextKmer,firstKmer[0],results)
    return results
    
def assemblyHelper(genome, kmer, string, results):
    
    #Once it gets to the end, it adds the string to the results list
    if len(genome)==0:
        results.append(string)
        return
    
    #If the path leads you to a dead end, this ends the recursion for that path.
    if kmer not in genome:
        return
        
    #This cuts out the repeats of values when accessing a key in the dictionary
    kmers = []    
    for value in genome[kmer]:
        if value not in kmers:
            kmers.append(value)
    
    #If the dictionary key has only one value, this removes the key        
    if len(genome[kmer])==1:
        nextKmer = genome[kmer].pop(0)
        genome.pop(kmer)
        assemblyHelper(genome,nextKmer,string+kmer[0],results)
        #This adds a key back to the dictionary after finishing a previous recursion.
        genome[kmer] = [nextKmer]
    else:
        for i in range(len(kmers)):
            nextKmer = kmers[i]
            genome[kmer].remove(nextKmer)
            assemblyHelper(genome,nextKmer,string+kmer[0],results)
            #This adds a value back to a key after finishing a previous recursion.
            genome[kmer].append(nextKmer)
    
#change the file name as appropriate
with open("sampleKmers.txt", 'r') as f:
    text = f.read()
    kmerDict = createDict(text)
    #prints the dictionary
    for keys in kmerDict:
        print keys + " " + str(kmerDict[keys])
    results = assembly(kmerDict,text[:3])
    #prints the results
    for result in results:
        print result
    
    