def stringToList(string):
    string = string[1:len(string)-1]
    a = string.split()
    b = []
    for i in a:
        b.append(int(i))
    return b
        
def specialPrint(lst):
    a = "("
    for i in lst:
        if i>0:
            a += "+" + str(i)
        else: a+= str(i)
        a+= " "
    a = a[0:len(a)-1]
    a += ")"

    print a

def reversePartOfArray(array,start,end):
    return array[0:start] + list(reversed(array[start:end+1])) + array[end+1:]


def GreedySorting(perm):
    perm = stringToList(perm)
    x = 0
    while x < len(perm):
        y = x
        while not (abs(perm[y]) == x+1): y+=1
        if not (y==x):
            perm = reversePartOfArray(perm,x,y)
            for i in range(x,y+1):
                perm[i] = -perm[i]
            specialPrint(perm)
        if(perm[x]<0): 
            perm[x] = - perm[x]
            specialPrint(perm)
        x+=1