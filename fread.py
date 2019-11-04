
f = open("netlist.v", "r")
for line in f:
    print('\n')
   # print(line)
    data = line.split()
    count = 0
    for x in data:
        if(count == 0):
            cellName = x;
            print("Cell name: ", cellName)
        elif(count == 1):
            instanceName = x;
            print("Instance name: ", instanceName)
        elif((count > 2) & (count <= len(data) - 2)): #ignore data[2] entry as it is an empty bracket
            if(x != data[len(data)-2]):
                print("the", x[1], "pin", x[3:len(x)-2])
            else:
                print("the", x[1], "pin", x[3:len(x)-1])
        count += 1;
f.close()
