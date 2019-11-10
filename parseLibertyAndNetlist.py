from collections import defaultdict
from liberty.parser import parse_liberty
from liberty.types import select_timing_table

#display a cell from the instances dictionary as an instantiation
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
             

#a function that takes a file name for a gatelevel netlist and parses it
#it initializes the instances dictionary with all the instances created (accessed by instance name)
#each entry in the instantiations dictionary has all the pins of the cell and the wires connected to them
#it also initializes the wires dictionary
#the wires dictionary is accessed using the wire name and gives information about all the cells it is
#connected to and whether it is the cell's output or input
#finaly it stores the upper section of the gatelevel netlist so that it is printed later to the final .v file
def parseNetlist(fileName, wires, instancesDict, library, netlistUpperSection):
    wires.clear()
    instancesDict.clear()
    f = open(fileName, "r")
    wiresEncountered = 0
    for line in f:
       # print('\n')
       # print(line)
        if((line != "\n") & (line != 'endmodule')):
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
                    elif(count == 1):
                        instanceName = x;
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
                            
                            cell = library.get_group('cell', cellType)
                            pin = cell.get_group('pin', currentPin)
                            PINDIRECTION = pin['direction']
                            
                            wires[currentWire].append([instanceName, currentPin, PINDIRECTION])
                    count += 1;
                instancesDict[instanceName] = myCurrentInstance
            else:
                netlistUpperSection[0] += line
    f.close()
    
    
#get the capacitance of a given pin in a cell
def getPinCapacitance(instanceName, inPin, instancesDict, library):
    cell = library.get_group('cell', instancesDict[instanceName]["cellType"])
    pin = cell.get_group('pin', inPin)
    PINCAPACITANCE = pin['capacitance']
    return PINCAPACITANCE

#get the column from the characterization table containing the delay of a cell using 
#the third column (as we are assuming the input transition to have the middle value)
def getColumnDelay(instanceName, outPin, instancesDict, delayColumn, capacitanceColumn, library):
    cellType = instancesDict[instanceName]["cellType"]
    cell = library.get_group('cell', cellType)
    pin = cell.get_group('pin', outPin)
    
    if(cellType[0:3] == "DFF"): #for simplicity, assume input is D in any FF
        
        time_table_rise=select_timing_table(pin,"CLK","cell_rise").get_array("values")
        time_table_fall=select_timing_table(pin,"CLK","cell_fall").get_array("values")
        for i in range(len(time_table_rise)):
            delayColumn.append(max(time_table_rise[i][2],time_table_fall[i][2]))
            
        #the index_1 is the same for cell_rise and cell_fall so you could pick either
        cellCapacitanceArray=select_timing_table(pin,"CLK","cell_fall").get_array("index_1")
        for i in range(len(cellCapacitanceArray[0])):
            capacitanceColumn.append(cellCapacitanceArray[0][i])

    else:
        #for simplicity assume related pin is always A in cells other than FF
        time_table_rise=select_timing_table(pin,"A","cell_rise").get_array("values")
        time_table_fall=select_timing_table(pin,"A","cell_fall").get_array("values")
        for i in range(len(time_table_rise)):
            delayColumn.append(max(time_table_rise[i][2],time_table_fall[i][2]))
            
        #the index_1 is the same for cell_rise and cell_fall so you could pick either
        cellCapacitanceArray=select_timing_table(pin,"A","cell_fall").get_array("index_1")
        for i in range(len(cellCapacitanceArray[0])):
            capacitanceColumn.append(cellCapacitanceArray[0][i])