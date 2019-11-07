# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:24:40 2019

@author: Ramez Moussa
"""
from collections import defaultdict
from liberty.parser import parse_liberty
from liberty.types import select_timing_table
from indexingCellsAndWires import *
import scipy.interpolate
from scipy.interpolate import UnivariateSpline
from extractCapacitance import *

library = parse_liberty(open("gscl45nm.lib").read())
wires = defaultdict(list)
instancesDict = {}
graph = defaultdict(list)
maxFanOut = 3
newWireCounter = 1
newBufferCounter = 1
parseNetlist("netlist.v", wires, instancesDict)

def fixByBuffering(key, currentFanOut, nBuffers, size, newWireCounter, newBufferCounter):
    newWires = []
    for currentWire in wires[graph[key][0][0]]:
        if(currentWire[2] == 'input'):
            #wires[graph[key][0][0]].remove(currentWire)
            newWires.append(currentWire)
   
    for currentWire in newWires:
        wires[graph[key][0][0]].remove(currentWire)
            
            
    counter = 0 #counter for the number of fanout considered
    
    for i in range(nBuffers):
        bufferInstanceName = "new_buffer_" + str(newBufferCounter)
        wires[graph[key][0][0]].append([bufferInstanceName, 'A', 'input'])
        
        myCurrentInstance = {}
        instanceType = "BUFX" + str(size)
        myCurrentInstance["cellType"] = instanceType
        myCurrentInstance['A'] = graph[key][0][0]
        myCurrentWire = "new_wire_" + str(newWireCounter)
        myCurrentInstance['Y'] = myCurrentWire
        
        instancesDict[bufferInstanceName] = myCurrentInstance
        #displayAsAnInstantiation(bufferInstanceName, instancesDict)
        wires[myCurrentWire].append([bufferInstanceName, 'Y', 'output'])
        for j in range(int(currentFanOut/nBuffers)):
            
            wires[myCurrentWire].append([newWires[counter][0], newWires[counter][1], 'input'])
            counter += 1
        newWireCounter += 1
        newBufferCounter += 1
    



def constructGraph(wires,instancesDict, graph, library):
    graph.clear()
    for key,value in wires.items():
        capacitance = 0
        outputCell = []
        for currentWire in value:
            if(currentWire[2] == 'output'):
                outputCell = currentWire
            else:
                capacitance += getPinCapacitance(currentWire[0], currentWire[1], instancesDict)
        delayColumn = []
        capacitanceColumn = []
        if(len(outputCell) > 0):
            getColumnDelay(outputCell[0], outputCell[1], instancesDict, delayColumn, capacitanceColumn)
            delay = getDelay(capacitanceColumn,delayColumn, capacitance)
            for currentWire in value:
                if((currentWire != outputCell) | (len(value) == 1)):
                    graph[outputCell[0]].append([key, outputCell[1], currentWire[0], currentWire[1], delay])
            
            
constructGraph(wires,instancesDict, graph, library)
fixByBuffering('BUFX4_1', 4,2,2, newWireCounter, newBufferCounter)   
constructGraph(wires,instancesDict, graph, library)
"""
for key,value in graph.items():
    currentFanOut = len(value)
    if(currentFanOut > maxFanOut):
        fixByBuffering(key, currentFanOut,maxFanOut)
        """
for key,value in graph.items():
    for edge in value:
        print ("Source:", key, "wire:", edge[0], "from pin:", edge[1], "to cell", edge[2], "to pin", edge[3], "with weight = ", edge[4])



