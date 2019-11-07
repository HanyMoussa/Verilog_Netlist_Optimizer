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
wires = defaultdict(list);
instancesDict = {}
graph = defaultdict(list);
parseNetlist("netlist.v", wires, instancesDict)


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
            
            
maxFanOut = 3;
newWireCounter = 1;
newBufferCounter = 1
   
for key,value in graph.items():
    currentFanOut = len(value)
    if(currentFanOut > maxFanOut):
        fixByBuffering(key, currentFanOut,maxFanOut)
        
        
"""        
for key,value in graph.items():
    for edge in value:
        print ("Source:", key, "wire:", edge[0], "from pin:", edge[1], "to cell", edge[2], "to pin", edge[3], "with weight = ", edge[4])
"""



def fixByBuffering(key, currentFanOut, maxFanOut):
    if(currentFanOut % maxFanOut == 0):
        newBuffers = currentFanOut/maxFanOut
    else:
        newBuffers = (currentFanOut/maxFanOut)+1
    
    # Create the new buffers
    for i in range(newBuffers):
        # Initially update the wire so that it does not make a conflict when writing the
        # verilog netlsit at the end
        
        for currentWire in wire[graph[key][0]]:
            if(currentWire[2] == 'input'):
                wire[graph[key][0]].remove(currentWire)
        bufferInstanceName = "new_buffer_" + newBufferCounter++
        #delayOfBuffers = getDelay(bufferCapacitance,bufferDelay, 3 * bufferPinCapacitance)
        #wire[graph[key][0]].append(graph[key][0], graph[key][1], bufferInstanceName, 'A', delayOfBuffers)
        wire[graph[key][0]].append(bufferInstanceName, 'A', 'input)
        
        
        for j in range(maxFanOut):
            newWire = "new_wire_" + newWireCounter++
            
            if(i * newBuffers + j < currentFanOut):
                wire[newWire].append(bufferInstanceName, 'A', 'input)