# Tkinter_Pizza_Vending_Machine

#### Description:
**My project i.e Pizza Vending machine is a simple GUI based program that displays an interface prompting for pizza toppings with a fixed base price that is 10 dollars, based on inputs it outputs bill in the same interface itself. (Module used for GUI is Tkinter)**

###### main
- Our main function includes onlt one function call i.e `Toppings_GUI`

###### Toppings_GUI

- First of all instanciating the Tk class to root, the basic structure of interface is created
- Some Variables are initialised globally so as to use them in different functions, and not create a mess
- The foreground image was picked up from [Pizza](https://www.freeiconspng.com/img/19313)
- All the toppings were initialised as **Intvar** and Checkbuttons for GUI with **onvalue** as 1 and **offvalue** as 0
- Finally one button using **Label** was inserted to generate the Bill amount for user using
`clear`,
`generate_Bill`


###### clear 

* The sole task of this function is to take input from the user as Checkbuttons in the interface with 
`Var.get()`
,set their value to all unckecked again for another round and generate the bill amount.
* It consists of an output Label that showcase the Bill amount in dollars

###### generate_Bill

+ This function takes 5 inputs as IntVar from checkbuttons saved earlier in **clear** function adn consists of initialised dictionary with toppings as keys and their price as values
+ If any of the toppings was checked then it's price is added to the base price(i.e 10$) accordingly
+ Unlike other Functions this function return The bill amount
