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
    if(len(outputCell) > 1):
        getColumnDelay(outputCell[0], outputCell[1], instancesDict, delayColumn, capacitanceColumn)
        delay = getCapacitance(capacitanceColumn,delayColumn, capacitance)
        for currentWire in value:
            if(currentWire != outputCell):
                graph[outputCell[0]].append([key, outputCell[1], currentWire[0], currentWire[1], delay])
            
            
            
for key,value in graph.items():
    for edge in value:
        print ("Source:", key, "wire:", edge[0], "from pin:", edge[1], "to cell", edge[2], "to pin", edge[3], "with weight = ", edge[4])