
from sizing import *
from FullConstructedGraph import *

library = parse_liberty(open("osu035.lib").read())
wires = defaultdict(list)
instancesDict = {}
graph = defaultdict(list)
newWireCounter = [1]
newBufferCounter = [1]
netlistUpperSection = [""]
maxInstanceName = [""]
newClonesCounter = [1]

#constructs the graph and displays the number of cells of each type
def constructAndDisplay():
    constructGraph(wires,instancesDict, graph, library, cload)
    print("The current netlist:")
    print("The maximum fanout in the current netlist is:", getCurrentMaxFanOut(maxInstanceName))
    print("total cells delay =:", getTotalDelay(graph))
    printNumberOfCellsOfEachType(instancesDict)
    print("-------------------------------------------------------")

#gets the maximum fanout in a given netlist
def getCurrentMaxFanOut(maxInstanceName):
    currentMaxFanOut = 0
    for key,value in instancesDict.items():
        currentCellOutputWire = getSourceOfWire(instancesDict, key)
        if(currentMaxFanOut <  (len(wires[currentCellOutputWire]) - 1)):
            currentMaxFanOut = (len(wires[currentCellOutputWire]) - 1)
            maxInstanceName[0] = key
    return currentMaxFanOut


#writes the current netlist (potentially optimized) to a the OptimizedNetlist.v file
def writeToFile(netlist):
    writingFile = netlist[:-2] + "Optimized.v"
    f = open(writingFile,"w+")
    f.write(netlistUpperSection[0])
    for key,value in instancesDict.items():
        displayAsAnInstantiation(f, key, instancesDict)
    f.write('endmodule')
    print("The optimized netlist has been written successfully to the file:", writingFile)
    
def displayGraph():
    for key,value in graph.items():
        for edge in value:
            print ("Source:", key, "wire:", edge[0], "from pin:", edge[1], "to cell", edge[2], "to pin", edge[3], "with weight = ", edge[4])
    print("-------------------------------------------------------")
 
def displayCells():
    for key,value in instancesDict.items():
        currentCellOutputWire = getSourceOfWire(instancesDict, key)
        print("Cell:", key, "- fanout:", len(wires[currentCellOutputWire]) -1)
#display the main menu with all the options    
def displayMenu(netlist):
    
    print("-------------------------------------------------------")
    print("to end the program press 0")
    print("to reinitialize the data structure using the original netlist press r")
    print("to apply buffering to the whole netlist press 1")
    print("to apply cloning to the whole netlist press 2 (recursive version)")
    print("to apply cloning to the whole netlist press 3 (iterative version)")
    print("to apply sizing press 4")
    print("to apply cloning to a single cell press 5")
    print("to apply buffering to a single cell press 6")
    print("To display the netlist graph press 7")
    print("To display the cells and their fanouts press 8")
    print("To write the current verilog netlist to a .v file press 9")
    print("-------------------------------------------------------")
    
    choice = input()
    if(choice == '0'):
        pass
    elif(choice == 'r'):
        print("Reinitialize")
        parseNetlist(netlist, wires, instancesDict, library, netlistUpperSection)
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '1'):
        print("Please specify the max fanout for any cell in the netlist")
        userMaxFanOut = input()
        
        print("Apply buffering")
        removeViolationsByBuffering(int(userMaxFanOut), graph, wires, instancesDict, newWireCounter, newBufferCounter, library, cload)       
        constructAndDisplay()
        reopenMenu()
    
    elif(choice == '2'):
        print("Please specify the max fanout for any cell in the netlist")
        userMaxFanOut = input()
        
        print("Apply cloning")
        removeViolationsByCloning(int(userMaxFanOut), graph, wires, instancesDict, newWireCounter, newBufferCounter, library, cload, newClonesCounter)
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '3'):
        print("Please specify the max fanout for any cell in the netlist")
        userMaxFanOut = input()
        
        print("Apply cloning")
        while (getCurrentMaxFanOut(maxInstanceName) > int(userMaxFanOut)):
            fixByCloningSingle(maxInstanceName[0], instancesDict, getCurrentMaxFanOut(maxInstanceName), int(userMaxFanOut), newWireCounter, wires, graph, library, cload, newClonesCounter)
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '4'):
        print("Please specify the minimum fanout of cells to be sized")
        fanout = input()
        print("Apply sizing")
        updateSizing(wires,instancesDict, graph, library, cload, int(fanout)) 
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '5'):
        print("Please enter the name of the instance you want to clone (applied to one cell)")
        instanceName = input()
        print("Please specify its maximum fanout")
        fanout = input()
        currentCellOutputWire = getSourceOfWire(instancesDict, instanceName)
        fixByCloningSingle(instanceName, instancesDict, len(wires[currentCellOutputWire]) - 1, int(fanout), newWireCounter, wires, graph, library, cload, newClonesCounter)
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '6'):
        print("Please enter the name of the instance you want to buffer (applied to one cell)")
        instanceName = input()
        print("Please specify its maximum fanout")
        fanout = input()
        currentCellOutputWire = getSourceOfWire(instancesDict, instanceName)
        fixByBuffering(instanceName, len(wires[currentCellOutputWire]) - 1, int(fanout), 2, newWireCounter, newBufferCounter, instancesDict, wires, graph)
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '7'):
        displayGraph()
        reopenMenu()
        
    elif(choice == '8'):
        displayCells()
        print(getCurrentMaxFanOut(maxInstanceName), maxInstanceName)
        reopenMenu()
        
    elif(choice == '9'):
        writeToFile(netlist)
            
        reopenMenu()
    else:
        print("Wrong input. Please enter a correct number")
        displayMenu(netlist)

#Ask the user if they want to reopen the menu or terminate the program
def reopenMenu():
    print("\nTo end the program press 0")
    print("To reopen the menu for further operations press 1")
    
    choice = input()
    if(choice == '0'):
        pass
    elif(choice == '1'):
        displayMenu(netlist)
    else:
        print("Wrong input. Please enter a correct number")
        reopenMenu()

print("Please input the name of the gatelevel netlist file (netlist.v for exammple)")
netlist = input()
cload = 100     # we are assuming that the load capacitance is 100

parseNetlist(netlist, wires, instancesDict, library, netlistUpperSection)
constructAndDisplay()
displayMenu(netlist)