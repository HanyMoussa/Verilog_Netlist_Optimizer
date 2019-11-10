# Verilog_Netlist_Optimizer
A Python library that parses a gate-level netlist and checks for any fanout violations. It provides 2 solutions to solve this issue:<br />
  1- Through adding Buffers<br />
  2- Through cloning the cell<br />
Additionally, the library provides the functionality to size up cells accordingly to reduce the total delay.

# Installing The Library
   ```
   Clone the Verilog_Netlist_Optimizer Github repository
   Download the library to your machine
   ```
# Using the library
In order to use the optimizer, run the `main.py` script. Essentially, the library has a command line user interface where the user can access all functions.

After parsing the netlist, the user is promted to do one of the following:
```
  1- Apply Buffering and specify the maximum fanout
  2- Apply cloning and specify the maximum fanout
  3- Apply sizing to optimize the total delay.
  4- Display the netlist as a graph
  5- Write the optimized gate-level netlist to a textfile
```
After applying any of the aforementioned functions, the maximum delay is displayed as well as the number of instances of each cell type. Moreover, the user gets to either return to the main menu or exit the program.

# Tests
The library was tested through 8 different ranging from modules with 10 cells to modules with over 350 cells. 

# Files

| Module        | Description  |
| :------------- |:-------------|
| main.py   | This is the interface of project throughwhich the user accesses the different functions |
| parseLibertyAndNetlist.py | This script is responsible for parsing both the liberty library and the gate-level netlist|
| FullConstructedGraph.py | This class has functions to construct a graph from the netlist. Additionally, it also has the functions responsible for Buffering and Cloning |
|sizing.py | This includes the Sizing Function |
| extractDelay.py | This has a function that interpolates/exterolates the delay for a given capactiance. It must be given the capacitance row and its corresponding delay from the timing table|

# Built by:
  In order to use parse the liberty file, we used [The Python Package Index (Pypi) liberty-parser Version 0.0.4](https://pypi.org/project/liberty-parser/)
  
# Authors:
  * Ramez Moussa - [Github Profile](https://github.com/ramezmoussa)
  * Hany Moussa - [Github Profile](https://github.com/hanymoussa)
  
