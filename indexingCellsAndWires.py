from collections import defaultdict
from liberty.parser import parse_liberty
from liberty.types import select_timing_table

library = parse_liberty(open("gscl45nm.lib").read())

wires = defaultdict(list);
instancesDict = {}

#display a cell as an instantiation
def displayAsAnInstantiation(instanceName, instancesDict):
    myCounter = 0
    myInstance = instancesDict[instanceName]
    for key, value in myInstance.items(): 
        if(myCounter == 0):
            print (value, " ", instanceName, " ( ", sep='',end='') 
        elif (myCounter != (len(myInstance.items()) - 1)):
            print (".", key, "(", value, "), ", sep='',end='')
        else:
             print (".", key, "(", value, ")", sep='', end='')
        myCounter += 1
    print (" );")
                
def parseNetlist(fileName, wires, instancesDict):
    f = open(fileName, "r")
    for line in f:
       # print('\n')
       # print(line)
        data = line.split()
        count = 0
        myCurrentInstance = {}
        for x in data:
            if(count == 0):
                cellType = x;
                myCurrentInstance["cellType"] = cellType
               # print("Cell type: ", cellType)
            elif(count == 1):
                instanceName = x;
              #  print("Instance name: ", instanceName)
            elif((count > 2) & (count <= len(data) - 2)): #ignore data[2] entry as it is an empty bracket
                if(x != data[len(data)-2]):
                    if(x[1:4] == "CLK"):
                        currentWire = x[5:len(x)-2]
                        currentPin = x[1:4]
                    elif((x[1:3] == "YS") | (x[1:3] == "YC")):
                        currentWire = x[4:len(x)-2]
                        currentPin = x[1:3]
                    else:
                        currentWire = x[3:len(x)-2]
                        currentPin = x[1]
                    myCurrentInstance[currentPin] = currentWire
                   # print("the", currentPin, "pin", currentWire)
                    
                    cell = library.get_group('cell', cellType)
                    pin = cell.get_group('pin', currentPin)
                    PINDIRECTION = pin['direction']
                    
                    wires[currentWire].append([instanceName, currentPin, PINDIRECTION])
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
                   # print("the", currentPin, "pin", currentWire)
                    
                    cell = library.get_group('cell', cellType)
                    pin = cell.get_group('pin', currentPin)
                    PINDIRECTION = pin['direction']
                    
                    wires[currentWire].append([instanceName, currentPin, PINDIRECTION])
            count += 1;
        instancesDict[instanceName] = myCurrentInstance
        #print(instancesDict[instanceName])
        #instancesDict[instanceName]["Q"] = "TRY MODIFY DATA"
    f.close()
    
def getPinCapacitance(instanceName, inPin, instancesDict):
    cell = library.get_group('cell', instancesDict[instanceName]["cellType"])
    pin = cell.get_group('pin', inPin)
    PINCAPACITANCE = pin['capacitance']
    return PINCAPACITANCE

def getColumnDelay(instanceName, outPin, instancesDict, delayColumn, capacitanceColumn):
    cellType = instancesDict[instanceName]["cellType"]
    cell = library.get_group('cell', cellType)
    pin = cell.get_group('pin', outPin)
    
    if(cellType[0:3] == "DFF"): #for simplicity, assume input is D in any FF
        
        time_table_rise=select_timing_table(pin,"CLK","cell_rise").get_array("values")
        time_table_fall=select_timing_table(pin,"CLK","cell_fall").get_array("values")
        for i in range(4):
            delayColumn.append(max(time_table_rise[i][2],time_table_fall[i][2]))
            
        cellCapacitanceArray=select_timing_table(pin,"CLK","cell_fall").get_array("index_1")
        for i in range(4):
            capacitanceColumn.append(cellCapacitanceArray[0][i])
        """
        timing = pin.get_groups('timing')
        timing_D = [g for g in timing if g['related_pin'] == 'CLK'][0]
        assert timing_D['related_pin'] == 'CLK'
        cellFallArray = timing_D.get_group('cell_fall').get_array('values')
        cellRiseArray = timing_D.get_group('cell_rise').get_array('values')
        cellCapacitanceArray = timing_D.get_group('cell_rise').get_array('index_1')
        assert cellCapacitanceArray.shape == (1,6)
        assert cellRiseArray.shape == (6, 6)
        assert cellFallArray.shape == (6, 6)
        for i in range(6):
            delayRow.append(max(cellFallArray[2][i],cellRiseArray[2][i]))
            
        for i in range(6):
            capacitanceRow.append(cellCapacitanceArray[0][i])
        """
    else:
        #for simplicity assume related pin is always A
        time_table_rise=select_timing_table(pin,"A","cell_rise").get_array("values")
        time_table_fall=select_timing_table(pin,"A","cell_fall").get_array("values")
        for i in range(4):
            delayColumn.append(max(time_table_rise[i][2],time_table_fall[i][2]))
            
        cellCapacitanceArray=select_timing_table(pin,"A","cell_fall").get_array("index_1")
        for i in range(4):
            capacitanceColumn.append(cellCapacitanceArray[0][i])
        """
        timing = pin.get_groups('timing')
        timing_A = [g for g in timing if g['related_pin'] == 'A'][0]
        assert timing_A['related_pin'] == 'A'
        cellFallArray = timing_A.get_group('cell_fall').get_array('values')
        cellRiseArray = timing_A.get_group('cell_rise').get_array('values')
        cellCapacitanceArray = timing_A.get_group('cell_rise').get_array('index_1')
        assert cellCapacitanceArray.shape == (1,6)
        assert cellRiseArray.shape == (6, 6)
        assert cellFallArray.shape == (6, 6)
        for i in range(6):
            delayRow.append(max(cellFallArray[2][i],cellRiseArray[2][i]))
                
        for i in range(6):
            capacitanceRow.append(cellCapacitanceArray[0][i]) """
"""print(instancesDict["OAI21X1_10"])
for key in instancesDict["OAI21X1_10"]:
    print(key, instancesDict["OAI21X1_10"][key])"""

"""
for instanceName in instancesDict.values():
    for attr in instanceName:
        print(attr, instanceName[attr])
"""

parseNetlist("netlist.v", wires, instancesDict)

for key,value in wires.items():
    if(len(value) == 1):
        for wire in value:
            pass
     #       print ("wire name:", key, "instance connected to:",  wire[0], "pin connected to =", wire[1], "direction:", wire[2])

#displayAsAnInstantiation("NOR2X1_1", instancesDict)

#print (getPinCapacitance("DFFPOSX1_1", "D", instancesDict))

#delayColumn = []
#capacitanceColumn = []
#getColumnDelay("NOR2X1_9", 'Y', instancesDict, delayColumn, capacitanceColumn)

#print(delayColumn)
#print(capacitanceColumn)