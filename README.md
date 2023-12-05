
The given code is for a tkinter GUI application that simulates a Mealy machine. It allows the user to input a string and a starting state, and then calculates the output string based on the transition and output tables of the Mealy machine.

> Note! I used a universal algorithm using an associative array (dict in Python) that will iterate over any table you want to write over the table

The application creates a Tkinter window with input fields for the input string and the starting state. It also creates buttons for each possible input symbol (X1, X2, X3) and each possible state (Q1, Q2, Q3, Q4, Q5, Q6). The user can click on the buttons to insert the corresponding symbols or states into the input field.

The application also creates a "Start!" button, which, when clicked, calculates the output string based on the input string and starting state. The output string is then displayed in a label on the window.

The code uses two dictionaries, "transition_table" and "output_table", to simulate the Mealy machine. The "transition_table" stores the next state for each combination of current state and input symbol, and the "output_table" stores the output symbol for each combination of current state and input symbol.

Overall, the code provides a graphical interface for interacting with a ***Mealy machine*** and getting the corresponding output for a given input string and starting state.

> In the future, I would like to implement graphical transitions from one state to another

## Examples of my machine in tabular 
  <img src="https://github.com/collinearen/Milli_Machine/blob/main/images/table.png" width="500" height="350" alt="telegram group" />
  
## and graphical form

  <img src="https://github.com/collinearen/Milli_Machine/blob/main/images/Mealy_machine.png" width="500" height="400" alt="telegram group" />


# ***Installation***
[(Back to top)](#table-of-contents)

> **Note**: For longer README files, I usually add a "Back to top" buttton as shown above. It makes it easy to navigate.

### <p align="center">you need to download the project to your local computer</p>
```shell
git clone https://github.com/collinearen/share-this-project.git
```
### <p align="center">Next you need to create a virtual environment in Python and activate it</p>
```shell
python -m venv venv
```
### <p align="center">and activate her</p>

```shell
source venv/bin/activate
```
### <p align="center">Enter the following commands to upgrade pip and download all modules and libraries that were used (they are located in the ***reqi.txt*** folder)</p>
```shell
pip install --upgrade pip
```
```shell
pip install -r reqiurements.txt
```

## and run the code)
