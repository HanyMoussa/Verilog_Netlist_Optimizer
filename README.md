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

# Tests
The library was tested through 8 different verilog netlists including .

# Built by:
  In order to use parse the liberty file, we used [The Python Package Index (Pypi) liberty-parser Version 0.0.4](https://pypi.org/project/liberty-parser/)
  
# Contributers:
  * Ramez Moussa - [Github Profile](https://github.com/ramezmoussa)
  * Hany Moussa - [Github Profile](https://github.com/hanymoussa)
  
