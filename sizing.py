# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:24:40 2019

@author: Ramez Moussa
"""
from FullConstructedGraph import *
        
def updateWire(wires, wireName, instance, newInstanceName):
    for connection in wires[wireName]:
        if(connection[0] == instance):
            connection[0] = newInstanceName


def replaceCell(wires,instancesDict, graph, library, instance, newCellType):
    myCurrentInstance = {}
    
    # Create new instance where the only difference is the cell type
    for attribute in instancesDict[instance]:
        if(attribute == "cellType"):
            myCurrentInstance["cellType"]= newCellType
        else:
            myCurrentInstance[attribute] = instancesDict[instance][attribute]
    del instancesDict[instance]
    newInstanceName = instance + "_sized"
    instancesDict[newInstanceName] = myCurrentInstance
    
    # update the wires dictionary
    for attribute in instancesDict[newInstanceName]:
        if(attribute != "cellType"):
            updateWire(wires, instancesDict[newInstanceName][attribute], instance, newInstanceName)
    #construct graph with updates
    constructGraph(wires,instancesDict, graph, library)
        

def updateSizing(wires,instancesDict, graph, library):
    for instance in graph:
        cellType = instancesDict[instance]["cellType"];
        currentSize = cellType[-1]
        newCellType = cellType[:-1] #remove last character then replace it by twice its value
        newSize = 2*int(currentSize)
        newCellType += (str(newSize))
        currentInstance = instance
        if(newSize > 9):
            twoDigits = 1
        else:
            twoDigits = 0
        while(len(library.get_groups('cell', newCellType)) == 1):
            oldDelay = getTotalDelay(graph)
            replaceCell(wires,instancesDict, graph, library, currentInstance, newCellType) #we construct the new graph inside the function
            newDelay = getTotalDelay(graph)
            currentInstance = currentInstance + "_sized"
            if(newDelay > oldDelay):
                newCellType = newCellType[:-1]
                if(twoDigits == 0):
                    newCellType += (str(int(newSize/2)))
                    replaceCell(wires,instancesDict, graph, library, currentInstance, newCellType)
                    break
                else:
                    newCellType = newCellType[:-1]
                    newCellType += (str(int(newSize/2)))
                    replaceCell(wires,instancesDict, graph, library, currentInstance, newCellType)
                    break
            else: 
                newCellType = newCellType[:-1]
                newSize = newSize * 2
                newCellType +=(str(newSize))
                if(newSize > 9):
                    twoDigits = 1;
                else:
                    twoDigits = 0;
            
   


#print(getTotalDelay(graph))
#printNumberOfCellsOfEachType(instancesDict)
#print(len(library.get_groups('cell', "OR2X2")))

constructGraph(wires,instancesDict, graph, library)
print("The Original Graph:")
print("total cells delay =:", getTotalDelay(graph))
printNumberOfCellsOfEachType(instancesDict)
print("-------------------------------------------------------")

"""
#max fanout is 2
removeViolationsByBuffering(2, graph, wires, instancesDict, library)
print("The Graph after fixing Fan Out by Buffering:")
print("total cells delay =:", getTotalDelay(graph))
printNumberOfCellsOfEachType(instancesDict)
print("-------------------------------------------------------")


updateSizing(wires,instancesDict, graph, library) 

print("The Graph after Fixing Fanouts by Buffering and Sizing:")
print("total cells delay =:", getTotalDelay(graph))
printNumberOfCellsOfEachType(instancesDict)
print("-------------------------------------------------------")

for key,value in instancesDict.items():
    pass#displayAsAnInstantiation(key, instancesDict)

"""
fixByCloning('DFFPOSX1_1', instancesDict, len(graph['DFFPOSX1_1']), 2, newWireCounter, wires, graph)


constructGraph(wires,instancesDict, graph, library)
print("The Original Graph after Cloning:")
print("total cells delay =:", getTotalDelay(graph))
printNumberOfCellsOfEachType(instancesDict)
print("-------------------------------------------------------")


updateSizing(wires,instancesDict, graph, library) 

print("The Graph after Fixing Fanouts by Cloning and Sizing:")
print("total cells delay =:", getTotalDelay(graph))
printNumberOfCellsOfEachType(instancesDict)
print("-------------------------------------------------------")