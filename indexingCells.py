
f = open("netlist.v", "r")

instancesDict = {}
myCurrentInstance = {}
for line in f:
    print('\n')
   # print(line)
    data = line.split()
    count = 0
    for x in data:
        if(count == 0):
            cellType = x;
            myCurrentInstance["cellType"] = cellType
            print("Cell type: ", cellType)
        elif(count == 1):
            instanceName = x;
            print("Instance name: ", instanceName)
        elif((count > 2) & (count <= len(data) - 2)): #ignore data[2] entry as it is an empty bracket
            if(x != data[len(data)-2]):
                myCurrentInstance[x[1]] = x[3:len(x)-2]
                print("the", x[1], "pin", x[3:len(x)-2])
            else:
                myCurrentInstance[x[1]] = x[3:len(x)-1]
                print("the", x[1], "pin", x[3:len(x)-1])
                
        count += 1;
    instancesDict[instanceName] = myCurrentInstance


"""print(instancesDict["OAI21X1_10"])
for key in instancesDict["OAI21X1_10"]:
    print(key, instancesDict["OAI21X1_10"][key])"""
        
for instanceName in instancesDict.values():
    for attr in instanceName:
        print(attr, instanceName[attr])
f.close()
