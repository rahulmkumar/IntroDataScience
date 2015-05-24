import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    
    
    if record[0] =='a':
        for k in range(0,5):
            #print 'i,k,value:',record[1],k, ('a',record[2],record[3])
            mr.emit_intermediate((record[1],k), ('a',record[2],record[3]))
    
    if record[0]=='b':
        for i in range(0,5):
            #print 'i,k,value:',i,record[2], ('b',record[1],record[3])
            mr.emit_intermediate((i,record[2]), ('b',record[1],record[3]))
        

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
   
    multcount = {}
    
    for tup in range(0,len(list_of_values)):
        idx = str(list_of_values[tup][1])
        if multcount.has_key(idx):
            multcount[idx] = multcount[idx] + 1
        else:
            multcount[idx] = 1
        
   
    for x in range(0,len(list_of_values)):
        for y in range(0,len(list_of_values)):
            if list_of_values[x][0] != list_of_values[y][0] and list_of_values[x][1] == list_of_values[y][1]:
                if multcount[str(list_of_values[x][1])] > 0:
                    total = total + (list_of_values[x][2]*list_of_values[y][2])
                    multcount[str(list_of_values[x][1])] = multcount[str(list_of_values[x][1])] - 2 
        
    
    totout = (key[0],key[1],total)

    mr.emit((totout))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
