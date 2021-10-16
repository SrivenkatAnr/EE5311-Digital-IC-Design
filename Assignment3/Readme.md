# Description
	Design the schematic and layout of the sum generation part of the Full adder.
![Full Adder Circuit](https://raw.githubusercontent.com/SrivenkatAnr/EE5311-Digital-IC-Design/main/Assignment3/assets/Given/FA%20char_1.png?raw=true) <br/>
**Note:** The sizes are relative to a unit transistor whose dimensions are: L=2λ,Wn=4λ

# Group Members:
* Member 1: 3X Gate - The transistors in the first part, highlighted in blue, is thrice the size of the sizes shown in the figure above.
* Member 2: 1X Gate - The transistors in the first part is as shown in the figure above. 
* Member 3: 2X Gate - The transistors in the first part, highlighted in blue, is twice the size of the sizes shown in the figure above.

	**Note:** Cascade the carry-out and sum generation circuit that you made and complete the Full adder. 

# Deliverables (To be shown to the TA)
* Transistor schematic of a complete Full Adder circuit 
* DRC and LVS clean layout of the Full Adder circuit 
* Sizes of the transistors in the SUM part 

# Guidelines 
* The VDD and GND lines should run in Metal-3 or Metal-2.
* The VDD − GND pitch should be the same for all cells (NAND, AND, Full adder) = 50λ 
* Use the idea of fingers effectively
* Submission (To be uploaded on Moodle)

# Report
A single PDF showing 
* The schematic and layout of FA circuit. Mark the dimensions of the layout 
* DRC and LVS results 
* Simulation in SPICE to show correct functionality of a Full Adder
* Characterize the delay (time takes from 50% input to 50% output) and output slew (time taken to go from10% − 90% of the output ) as shown in the figure below. 
* Note: Use RC extracted netlist for simulation in this experiment. 

# Additional
* Vary Cslew from 10 f F − 200 f F in steps of 10 f F to vary the input slew 
* Vary CLoad from 10 f F − 500 f F in steps of 50 f F to vary the load capacitance 
* For each step of Cslew measure input slew Sin of the input 
* Create a table of the output delay of SUM as a function of Sin of A and CLoad (Cin should be tied to the appropriate supply) 
* Create a table of the output slew of Cout as a function of Sin of Cin and CLoad (A should be tied to the appropriate supply)

![Simulation Circuit](https://github.com/SrivenkatAnr/EE5311-Digital-IC-Design/blob/main/Assignment3/assets/Given/FA-Sum.png?raw=true)