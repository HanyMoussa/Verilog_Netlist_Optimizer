
from FullConstructedGraph import *
 
# a function that updates a wire by replacing the old instance name by the new one  
def updateWire(wires, wireName, instance, newInstanceName):
    for connection in wires[wireName]:
        if(connection[0] == instance):
            connection[0] = newInstanceName

# a function that replaces a specific instance with a different size. It is used to replace the
# small cells with larger sizes.
def replaceCell(wires,instancesDict, graph, library, instance, newCellType, cload):
    myCurrentInstance = {}
    
    # Create new instance where the only difference is the cell type
    for attribute in instancesDict[instance]:
        if(attribute == "cellType"):
            myCurrentInstance["cellType"]= newCellType
        else:
            myCurrentInstance[attribute] = instancesDict[instance][attribute]
    del instancesDict[instance]
    newInstanceName = instance + "_s"
    instancesDict[newInstanceName] = myCurrentInstance
    
    # update the wires dictionary
    for attribute in instancesDict[newInstanceName]:
        if(attribute != "cellType"):
            updateWire(wires, instancesDict[newInstanceName][attribute], instance, newInstanceName)
    #construct graph with updates
    constructGraph(wires,instancesDict, graph, library, cload)
        

# A function that uses a bruteforce algorithm to try to size every single cell and check the
# new delay. If it gets improved, then keep the new size. Else, return the cell to its original size.
def updateSizing(wires,instancesDict, graph, library, cload, fanout):
    for instance in graph:
        if(len(graph[instance]) > fanout):
            cellType = instancesDict[instance]["cellType"];
            currentSize = cellType[-1]
            if(cellType != 'DFFSR'):
                newCellType = cellType[:-1] #remove last character(which is usually the size) then replace it by twice its value
                newSize = 2*int(currentSize) 
                newCellType += (str(newSize))
                currentInstance = instance
                if(newSize > 9):
                    twoDigits = 1
                else:
                    twoDigits = 0
                while(len(library.get_groups('cell', newCellType)) == 1): # check if double this size exists in the library
                    oldDelay = getTotalDelay(graph)
                    replaceCell(wires,instancesDict, graph, library, currentInstance, newCellType, cload) #we construct the new graph inside the function
                    newDelay = getTotalDelay(graph)
                    currentInstance = currentInstance + "_s"
                    
                     # check for the delay before and after sizing the cell. If it gets improved then keep the new cell.
                    if(newDelay > oldDelay):
                        newCellType = newCellType[:-1]
                        if(twoDigits == 0):
                            newCellType += (str(int(newSize/2)))
                            replaceCell(wires,instancesDict, graph, library, currentInstance, newCellType, cload)
                            break
                        else:
                            newCellType = newCellType[:-1]
                            newCellType += (str(int(newSize/2)))
                            replaceCell(wires,instancesDict, graph, library, currentInstance, newCellType, cload)
                            break
                    else: 
                        newCellType = newCellType[:-1]
                        newSize = newSize * 2
                        newCellType +=(str(newSize))
                        if(newSize > 9):
                            twoDigits = 1;
                        else:
                            twoDigits = 0;
                    