from collections import defaultdict
from liberty.parser import parse_liberty
from liberty.types import select_timing_table

#display a cell as an instantiation
def displayAsAnInstantiation(f, instanceName, instancesDict):
    myCounter = 0
    myInstance = instancesDict[instanceName]
    for key, value in myInstance.items(): 
        if(myCounter == 0):
            f.write ("%s %s ( " %(value,instanceName) ) 
        elif (myCounter != (len(myInstance.items()) - 1)):
            f.write (".%s(%s), " %(key,value))
        else:
             f.write (".%s(%s)" % (key, value))
        myCounter += 1
    f.write (" );\n")
                
def parseNetlist(fileName, wires, instancesDict, library, netlistUpperSection):
    wires.clear()
    instancesDict.clear()
    f = open(fileName, "r")
    wiresEncountered = 0
    for line in f:
       # print('\n')
       # print(line)
        if(line != "\n"):
            data = line.split()
            if(data[0] == 'wire'): #identify that we reached the wires section
                wiresEncountered = 1
            if(wiresEncountered == 1) & (data[0] != 'wire'): #identify that we finished the wires section
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
            else:
                netlistUpperSection[0] += line
    f.close()
    
def getPinCapacitance(instanceName, inPin, instancesDict, library):
    cell = library.get_group('cell', instancesDict[instanceName]["cellType"])
    pin = cell.get_group('pin', inPin)
    PINCAPACITANCE = pin['capacitance']
    return PINCAPACITANCE

def getColumnDelay(instanceName, outPin, instancesDict, delayColumn, capacitanceColumn, library):
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

    else:
        #for simplicity assume related pin is always A
        time_table_rise=select_timing_table(pin,"A","cell_rise").get_array("values")
        time_table_fall=select_timing_table(pin,"A","cell_fall").get_array("values")
        for i in range(4):
            delayColumn.append(max(time_table_rise[i][2],time_table_fall[i][2]))
            
        cellCapacitanceArray=select_timing_table(pin,"A","cell_fall").get_array("index_1")
        for i in range(4):
            capacitanceColumn.append(cellCapacitanceArray[0][i])