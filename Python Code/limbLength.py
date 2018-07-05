def parseString(str):
    tempRow = str.split(" ")
    row = []
    for str in tempRow:
        row.append(int(str))
    return row
    
def parseStringMult(str):
    table = []
    for row in str.split("\n"):
        table.append(parseString(row))
    return table
    
def limbDistance(input, row):
    row2 = 0
    if row%2==0:
        row2 = row+1
    else:
        row2 = row-1
    comparedSpot = max(row,row2)+1
    difference = abs(input[row][comparedSpot]-input[row2][comparedSpot])
    distance = input[row][row2]
    return (distance-difference)/2
    
with open("rosalind_ba7b.txt", 'r') as f:


    f.readline().strip()
    row = int(f.readline().strip())
    text = f.read()
    input = parseStringMult(text)
    print limbDistance(input, row)