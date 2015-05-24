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

    perA = record[0]
    perB = record[1]
    
    value1 = (perA, perB, 1)
    value2 = (perB, perA, 0)
        
    mr.emit_intermediate(0, value1)
    mr.emit_intermediate(0, value2)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    friendship = {}
    #relation = []
    list_of_relations = []
    
    for lst in range(0,len(list_of_values)):
        relation=list_of_values[lst][0],list_of_values[lst][1]

        if list_of_values[lst][2] == 1:
            list_of_relations.append(relation)
        if friendship.has_key(relation):
            friendship[relation] = friendship[relation] + list_of_values[lst][2]
        else:
            friendship[relation] = list_of_values[lst][2]
             
        relation = ''
    
    for tup in list_of_relations:
        rtup = (tup[1],tup[0])
        if friendship[rtup] == 0:
            mr.emit(tup)
            mr.emit(rtup)
        
        
    #mr.emit((list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
