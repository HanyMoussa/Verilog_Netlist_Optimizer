from collections import defaultdict
from liberty.parser import parse_liberty


library = parse_liberty(open("gscl45nm.lib").read())

wires = defaultdict(list);
instancesDict = {}
myCurrentInstance = {}
f = open("netlist.v", "r")


for line in f:
    print('\n')
   # print(line)
    data = line.split()
    count = 0
    for x in data:
        if(count == 0):
            cellType = x;
            myCurrentInstance["cellType"] = cellType
            print("Cell type: ", cellType)
        elif(count == 1):
            instanceName = x;
            print("Instance name: ", instanceName)
        elif((count > 2) & (count <= len(data) - 2)): #ignore data[2] entry as it is an empty bracket
            if(x != data[len(data)-2]):
                if(x[1:4] == "CLK"):
                    currentWire = x[5:len(x)-2]
                    currentPin = x[1:4]
                elif((x[1:3] == "YS") | (x[1:3] == "YC")):
                    currentWire = x[4:len(x)-1]
                    currentPin = x[1:3]
                else:
                    currentWire = x[3:len(x)-2]
                    currentPin = x[1]
                myCurrentInstance[currentPin] = currentWire
                print("the", currentPin, "pin", currentWire)
                
                cell = library.get_group('cell', 'XOR2X1')
                pin = cell.get_group('pin', 'Y')
                PINDIRECTION = pin['direction']
                
                wires[currentWire].append((instanceName, currentPin, PINDIRECTION))
            else:
                if(x[1:4] == "CLK"):
                    currentWire = x[5:len(x)-1]
                    currentPin = x[1:4]
                elif((x[1:3] == "YS") | (x[1:3] == "YC")):
                    currentWire = x[4:len(x)-1]
                    currentPin = x[1:3]
                else:
                    currentWire = x[3:len(x)-1]
                    currentPin = x[1]
                myCurrentInstance[currentPin] = currentWire
                print("the", currentPin, "pin", currentWire)
                
                cell = library.get_group('cell', 'XOR2X1')
                pin = cell.get_group('pin', 'Y')
                PINDIRECTION = pin['direction']
                
                wires[currentWire].append((instanceName, currentPin, PINDIRECTION))
        count += 1;
    instancesDict[instanceName] = myCurrentInstance


"""print(instancesDict["OAI21X1_10"])
for key in instancesDict["OAI21X1_10"]:
    print(key, instancesDict["OAI21X1_10"][key])"""

"""
for instanceName in instancesDict.values():
    for attr in instanceName:
        print(attr, instanceName[attr])
"""

for key,value in wires.items():
    if(len(value) == 1):
        for wire in value:
            print ("wire name:", key, "instance connected to:",  wire[0], "pin connected to =", wire[1], "direction:", wire[2])

f.close()
