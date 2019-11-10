# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:24:40 2019

@author: Ramez Moussa
"""
from collections import defaultdict
from liberty.parser import parse_liberty
from liberty.types import select_timing_table
from parseLibertyAndNetlist import *
import scipy.interpolate
from scipy.interpolate import UnivariateSpline
from extractDelay import *


def fixByCloning(instanceName, instancesDict, currentFanOut, maxFanOut, newWireCounter, wires, graph):
    if(currentFanOut%maxFanOut == 0):
        nClones = (int(currentFanOut/maxFanOut) - 1)
    else:
        nClones = (int(currentFanOut/maxFanOut))
        
    newWires = []
    
    for currentWire in wires[graph[instanceName][0][0]]:
        if(currentWire[2] == 'input'):
            #wires[graph[instanceName][0][0]].remove(currentWire)
            newWires.append(currentWire)
   
    removeCounter = 0
    for currentWire in newWires:
        if(removeCounter >= maxFanOut):
            wires[graph[instanceName][0][0]].remove(currentWire)
        removeCounter += 1
    
    counter = maxFanOut #counter for the number of clones considered
    for i in range(nClones):
        clonedInstanceName = instanceName + '_clone_' + str(i+1)
        myCurrentInstance = instancesDict[instanceName].copy()
        myCurrentWire = "new_wire_" + str(newWireCounter[0])
        newWireCounter[0] += 1
        
        if(myCurrentInstance['cellType'][0:3] == "DFF"):
            myCurrentInstance['Q'] = myCurrentWire
            instancesDict[clonedInstanceName] = myCurrentInstance
            wires[myCurrentWire].append([clonedInstanceName, 'Q', 'output'])
        else:
            myCurrentInstance['Y'] = myCurrentWire
            instancesDict[clonedInstanceName] = myCurrentInstance
            wires[myCurrentWire].append([clonedInstanceName, 'Y', 'output'])
            
        for key,value in myCurrentInstance.items():
            if(key == 'cellType') | (key == 'Y') | (key == 'Q'):
                continue
            else:
                wires[value].append([clonedInstanceName, key, 'input'])
        
        
        
        for j in range(min(maxFanOut,currentFanOut-counter)):
            wires[myCurrentWire].append([newWires[counter][0], newWires[counter][1], 'input'])
            instancesDict[newWires[counter][0]][newWires[counter][1]] = myCurrentWire
            counter += 1
        

    
    #check if we need further cloning levels
    for key,value in instancesDict[instanceName].items():
        if(key == 'cellType') | (key == 'Y') | (key == 'Q'):
            continue
        else:
            prevFanOut = len(wires[value]) - 1
            prevCell = -1
            for item in wires[value]:
                if(item[2] == 'output'):
                    prevCell = item[0]
            if((prevFanOut > maxFanOut) & (prevCell != -1)) :
                fixByCloning(prevCell, instancesDict, prevFanOut, maxFanOut, newWireCounter, wires, graph)


        
def fixByBuffering(instanceName, currentFanOut, maxFanOut, size, newWireCounter, newBufferCounter, instancesDict, wires, graph):
    if(currentFanOut%maxFanOut == 0):
        nBuffers = (int(currentFanOut/maxFanOut))
    else:
        nBuffers = (int(currentFanOut/maxFanOut)) + 1
    newWires = []
    for currentWire in wires[graph[instanceName][0][0]]:
        if(currentWire[2] == 'input'):
            #wires[graph[instanceName][0][0]].remove(currentWire)
            newWires.append(currentWire)
   
    for currentWire in newWires:
        wires[graph[instanceName][0][0]].remove(currentWire)
            
            
    counter = 0 #counter for the number of fanout considered
    
    for i in range(nBuffers):
        bufferInstanceName = "new_buffer_" + str(newBufferCounter[0])
        wires[graph[instanceName][0][0]].append([bufferInstanceName, 'A', 'input'])
        
        myCurrentInstance = {}
        instanceType = "BUFX" + str(size)
        myCurrentInstance["cellType"] = instanceType
        myCurrentInstance['A'] = graph[instanceName][0][0]
        myCurrentWire = "new_wire_" + str(newWireCounter[0])
        myCurrentInstance['Y'] = myCurrentWire
       
        instancesDict[bufferInstanceName] = myCurrentInstance
        #displayAsAnInstantiation(bufferInstanceName, instancesDict)
        wires[myCurrentWire].append([bufferInstanceName, 'Y', 'output'])
        for j in range(min(maxFanOut,currentFanOut-counter)):
            
            wires[myCurrentWire].append([newWires[counter][0], newWires[counter][1], 'input'])
            instancesDict[newWires[counter][0]][newWires[counter][1]] = myCurrentWire
            counter += 1
        newWireCounter[0] += 1
        newBufferCounter[0] += 1
    
    #check if we need further buffering levels
    if(nBuffers > maxFanOut):
        fixByBuffering(instanceName, nBuffers, maxFanOut, 2, newWireCounter, newBufferCounter, instancesDict, wires, graph)  

def removeViolationsByBuffering(maxFanOut, graph, wires, instancesDict, newWireCounter, newBufferCounter, library):
    copyOfGraph = graph.copy()
    for key in copyOfGraph:
        if(len(graph[key]) > maxFanOut):
            fixByBuffering(key, len(graph[key]), maxFanOut, 2, newWireCounter, newBufferCounter, instancesDict, wires, graph)
            constructGraph(wires,instancesDict, graph, library)


def constructGraph(wires,instancesDict, graph, library):
    graph.clear()
    for key,value in wires.items():
        capacitance = 0
        outputCell = []
        for currentWire in value:
            if(currentWire[2] == 'output'):
                outputCell = currentWire
            else:
                capacitance += getPinCapacitance(currentWire[0], currentWire[1], instancesDict, library)
        delayColumn = []
        capacitanceColumn = []
        if(len(outputCell) > 0):
            getColumnDelay(outputCell[0], outputCell[1], instancesDict, delayColumn, capacitanceColumn, library)
            delay = getDelay(capacitanceColumn,delayColumn, capacitance)
            for currentWire in value:
                if(currentWire != outputCell):
                    graph[outputCell[0]].append([key, outputCell[1], currentWire[0], currentWire[1], delay])
                elif ((currentWire == outputCell) & (len(value) == 1)):
                    graph[outputCell[0]].append([key, outputCell[1], 'output cload', 'output pin', delay])


def getTotalDelay(graph):
    totalDelay = 0
    for key, value in graph.items():
        maxCurrentEdge = 0
        for edge in value:
            #get the weight with the maximum value to represent the delay of the cell
            maxCurrentEdge = max(maxCurrentEdge, edge[4])
        totalDelay += maxCurrentEdge
    return totalDelay


def printNumberOfCellsOfEachType(instancesDict):
    cellsCount = defaultdict(list)
    
    for key,value in instancesDict.items():
        cellsCount[value['cellType']] = cellsCount.get(value['cellType'], 0) + 1
          
    for key, value in cellsCount.items():
        print("Cell: ", key, "- count:",value)
        
#fixByBuffering('INVX8_1', 10, 3, 2, newWireCounter, newBufferCounter)   
#constructGraph(wires,instancesDict, graph, library)
"""
for key,value in graph.items():
    currentFanOut = len(value)
    if(currentFanOut > maxFanOut):
        fixByBuffering(key, currentFanOut,maxFanOut)
        
for key,value in graph.items():
    for edge in value:
        print ("Source:", key, "wire:", edge[0], "from pin:", edge[1], "to cell", edge[2], "to pin", edge[3], "with weight = ", edge[4])
"""

#print(getTotalDelay(graph))
#printNumberOfCellsOfEachType(instancesDict)