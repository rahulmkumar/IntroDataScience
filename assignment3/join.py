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
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    tcount = {}
    joined = []
    table1 = []
    table2 = []
    #print 'list_of_values type: ',type(list_of_values[0])

    for c in range(0,len(list_of_values)):
        tab = list_of_values[c][0]
        #tab.encode('utf-8')
        if tcount.has_key(tab):
            tcount[tab] = tcount[tab] + 1
        else:
            tcount[tab] = 1
    
    keys = tcount.keys()
    
    if tcount[keys[0]] > tcount[keys[1]]:
        min = keys[1]
        max = keys[0]
    else:
        min = keys[0]
        max = keys[1]
        
    tab1 = keys[1]
    tab2 = keys[0]
    
    for v in range(0, len(list_of_values)):
        if list_of_values[v][0] == tab1:
            table1.append(list_of_values[v])
        elif list_of_values[v][0] == tab2:
            table2.append(list_of_values[v])
    
    for fir in range(0,len(table1)):
        for sec in range(0,len(table2)):
            #mr.emit((table1[fir],table2[sec]))
            joined = []
            for first in range(0,len(table1[fir])):
                joined.append(table1[fir][first])
            
            for second in range(0,len(table2[sec])):
                joined.append(table2[sec][second])

            mr.emit((joined))

def reducer1(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    tcount = {}
    joined = []
    #print 'list_of_values type: ',type(list_of_values[0])

    for c in range(0,len(list_of_values)):
        tab = list_of_values[c][0]
        #tab.encode('utf-8')
        if tcount.has_key(tab):
            tcount[tab] = tcount[tab] + 1
        else:
            tcount[tab] = 1
    
    keys = tcount.keys()
    if tcount[keys[0]] > tcount[keys[1]]:
        min = keys[1]
    else:
        min = keys[0]
        
    #print 'max:', max  

    for v in range(0,len(list_of_values)):
        for y in range(0,len(list_of_values)):

            joined = []
            #print 'v:',v
            #print 'y:',y
            #print list_of_values[v][0],list_of_values[y][0]
            if str(list_of_values[v][0]) != str(list_of_values[y][0]) and str(list_of_values[v][0]) == str(min):
                
                #complete = list_of_values[v],list_of_values[y]
                
                #print list_of_values[v]
                #print list_of_values[y]
                
                print list_of_values[v][0]
                print min
                print '---------'
                for first in range(0,len(list_of_values[v])):
                    joined.append(list_of_values[v][first])
                    
                for second in range(0,len(list_of_values[y])):
                    joined.append(list_of_values[y][second])
                    

                #print joined
                
                    
                mr.emit((joined))
                #print joined
            
                    
            

    #mr.emit((key, joined))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
