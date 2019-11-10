
from sizing import *
from FullConstructedGraph import *

library = parse_liberty(open("gscl45nm.lib").read())
wires = defaultdict(list)
instancesDict = {}
graph = defaultdict(list)
newWireCounter = [1]
newBufferCounter = [1]
netlistUpperSection = [""]

def constructAndDisplay():
    constructGraph(wires,instancesDict, graph, library)
    print("The current netlist:")
    print("The maximum fanout in the current netlist is:", getCurrentMaxFanOut())
    print("total cells delay =:", getTotalDelay(graph))
    printNumberOfCellsOfEachType(instancesDict)
    print("-------------------------------------------------------")

def getCurrentMaxFanOut():
    currentMaxFanOut = 0
    for key,value in graph.items():
        currentMaxFanOut = max(currentMaxFanOut, len(graph[key]))
    return currentMaxFanOut


def writeToFile():
    f = open("OptimizedNetlist.v","w+")
    f.write(netlistUpperSection[0])
    for key,value in instancesDict.items():
        displayAsAnInstantiation(f, key, instancesDict)
    print("The optimized netlist has been written successfully to the file: OptimizedNetlist.v")
    
def displayMenu():
    
    print("-------------------------------------------------------")
    print("to end the program press -1")
    print("to reinitialize the data structure using the original netlist press 0")
    print("to apply buffering press 1")
    print("to apply cloning press 2")
    print("to apply sizing press 3")
    print("(Note that you sizing is applied automatically after buffering and cloning to improve the total delay)")
    print("To display the netlist graph press 4")
    print("To write the current verilog netlist to a .v file press 5")
    print("-------------------------------------------------------")
    
    choice = input()
    if(choice == '-1'):
        pass
    elif(choice == '0'):
        print("Reinitialize")
        parseNetlist(netlist, wires, instancesDict, library, netlistUpperSection)
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '1'):
        print("Please specify the max fanout for any cell in the netlist")
        userMaxFanOut = input()
        
        print("Apply buffering")
        removeViolationsByBuffering(int(userMaxFanOut), graph, wires, instancesDict, newWireCounter, newBufferCounter, library)       
        constructAndDisplay()
    
        print("Apply sizing")
        updateSizing(wires,instancesDict, graph, library) 
        constructAndDisplay()
        reopenMenu()
    
    elif(choice == '2'):
        print("Please specify the max fanout for any cell in the netlist")
        userMaxFanOut = input()
        
        print("Apply cloning")
        fixByCloning('DFFPOSX1_1', instancesDict, len(graph['DFFPOSX1_1']), 2, newWireCounter, wires, graph)
        constructAndDisplay()
        
        print("Apply sizing")
        updateSizing(wires,instancesDict, graph, library) 
        constructAndDisplay()
        reopenMenu()

    elif(choice == '3'):
        print("Apply sizing")
        updateSizing(wires,instancesDict, graph, library) 
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '4'):
        constructAndDisplay()
        reopenMenu()
        
    elif(choice == '5'):
        writeToFile()
            
        reopenMenu()
    else:
        print("Wrong input. Please enter a correct number")
        displayMenu()
  
def reopenMenu():
    print("\nTo end the program press -1")
    print("To reopen the menu for further operations press 1")
    
    choice = input()
    if(choice == '-1'):
        pass
    elif(choice == '1'):
        displayMenu()
    else:
        print("Wrong input. Please enter a correct number")
        reopenMenu()

print("Please input the name of the gatelevel netlist file (netlist.v for exammple)")
netlist = input()
parseNetlist(netlist, wires, instancesDict, library, netlistUpperSection)
constructAndDisplay()
displayMenu()