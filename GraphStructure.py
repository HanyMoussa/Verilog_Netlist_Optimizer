#@author: Ramez Moussa

# Creating the Graph Structure that will represent the circuit
# A node represents a cell and all the outgoing edges represent the delay of that cell

from collections import defaultdict

graph = defaultdict(list);

# the key is the source node
# ('YS', u5, 'A', 2.64):
#   We go from pin YS in u7 to pin A in u5 and the delay is 2.64
graph['u7'].append(('YS', 'u5', 'A', 2.64))
graph['u7'].append(('YC', 'u8', 'B', 2.5))
graph['u5'].append(('Y', 'u8', 'C', 1))



# Construct the Graph from the wires dictionary:    

#print(graph['u7'][0][1])

for key,value in graph.items():
    for edge in value:
        print ("Source:", key, "from pin",  edge[0], "to cell", edge[1], "pin", edge[2], "with weight = ", edge[3])