# Verilog_Netlist_Optimizer
A Python library that parses a gate-level netlist and checks for any fanout violations. It provides 2 solutions to solve this issue:<br />
  1- Through adding Buffers<br />
  2- Through cloning the cell<br />
Additionally, the library provides the functionality to size up cells accordingly to reduce the total delay.

## Installing The Library
   ```
   Clone the Verilog_Netlist_Optimizer Github repository
   Download the library to your machine
   ```
## Using the library
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

## Tests
The project was tested through 11 tests on 5 different netlists ranging from modules with 2 cells to modules with over 2000 cells. 

## Files

| Module        | Description  |
| :------------- |:-------------|
| main.py   | This is the interface of project throughwhich the user accesses the different functions |
| parseLibertyAndNetlist.py | This script is responsible for parsing both the liberty library and the gate-level netlist|
| FullConstructedGraph.py | This class has functions to construct a graph from the netlist. Additionally, it also has the functions responsible for Buffering and Cloning |
|sizing.py | This includes the Sizing Function |
| extractDelay.py | This has a function that interpolates/exterolates the delay for a given capactiance. It must be given the capacitance row and its corresponding delay from the timing table|

## Assumptions
During our development, we had to make some assumptions to for the sake of simplicity:

  1. We are assuming that the gate-level netlist would include cells with only 1 output port
  2. It is assumed that for all cells, the input transision is always the third value in the None Linear Delay Model (NLDM) table. 
  3. Whenever the load capacitance is outside the provided range in NLDM table, linear extrapolation is utilized.
  4. We are assuming that the total delays of all cells are representative of the worst-case delay which might not be the case all the time.
  5. Another assumption we made was that the output delay of any cell was relative to the first input pin.

## Limitations
Unforunately, our assumptions and the algorithms we utilized have few limitations:
  1. As mentioned in the asssumptions, our project might not operate correctly if cells with multiple output ports are used.
  2. The sizing algorithm utilized has an exponential complexity. Consequently, it requires a lot of time and memory to provide the results. This is just a naive approach for sizing just to show its effect on the total delay.
  3. The cloning algorithm can reach the maximum recursion depth if the maximum fan out is small and there is a large number of cells. To solve this, we added an iterative version of the algorithm.

## Acknowledgement:
  This was created for the Digital Design 2 Course CSCE3304 at the American University in Cairo.
  
  In order to parse the liberty file, we used [The Python Package Index (Pypi) liberty-parser Version 0.0.4](https://pypi.org/project/liberty-parser/)
  
## Authors:
  * Ramez Moussa - [Github Profile](https://github.com/ramezmoussa)
  * Hany Moussa - [Github Profile](https://github.com/hanymoussa)
  
