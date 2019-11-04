#@author: Ramez Moussa

# Creating the Graph Structure that will represent the circuit
# A node represents a cell and all the outgoing edges represent the delay of that cell

from collections import defaultdict

graph = defaultdict(list);
graph['u7'].append(('u5', 2.64))
graph['u7'].append(('u8', 2.64));
graph['u5'].append(('u8', 1))

#print(graph)

#print(graph['u7'][0][1])

for key,value in graph.items():
    for edge in value:
        print ("Vertex:", key, "to",  edge[0], "weight = ", edge[1])