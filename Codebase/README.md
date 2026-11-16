# Unit_Conversion

# Unit Conversion System

A simple console-based unit converter written in Python 3. The user picks a category from a menu (Length, Weight, Temperature or Time), chooses the units to convert between, enters a value, and gets the result rounded to 2 decimal places.

The program uses Python functions, dictionaries, loops, conditional statements, exception handling, and formatted output to perform conversions.

# Features

- Length Conversion: Convert between millimeters, centimeters, meters, kilometers, inches, feet, and miles.
- Weight Conversion: Convert between milligrams, grams, kilograms, tonnes, pounds, and ounces.
- Temperature Conversion: Convert between Celsius, Fahrenheit, and Kelvin.
- Time Conversion: Convert between milliseconds, seconds, minutes, hours, and days.
- Direct Unit Input: Enter the number and its source unit together (e.g., "4 km").
- Input Validation: Handles invalid numbers and unsupported units.
- Continuous Conversion: Perform multiple conversions without restarting the program.
- Formatted Results: Displays conversion results with two decimal places.

# Technologies Used

- Python 3
- Built-in Python features:
  - Functions
  - Dictionaries
  - While loops
  - Conditional statements
  - Exception handling ("try-except")
  - String methods
  - f-strings
  - 
1. Clone the Repository

git clone https://github.com/Ravik-0008/Unit_Conversion/edit/main.py

No external Python libraries are required.

How to Use

1. Run the program.
2. Select a conversion category from the main menu.
3. Enter the value along with its source unit.
4. Enter the destination unit.
5. View the converted result.
6. Choose whether to perform another conversion.

Example

========== UNIT CONVERTER ==========

1. Length
2. Weight
3. Temperature
4. Time
0. Exit

Select a conversion category: 1

Enter the value and its unit (e.g. 4 km): 4 km

Which unit would you like to convert it into? mm

4.00 km = 4000000.00 mm

Would you like to perform another conversion? (yes/no): yes

Supported Units

Category| Supported Units
Length| mm, cm, m, km, inch, foot, mile
Weight| mg, g, kg, tonne, pound, ounce
Temperature| c, f, k
Time| ms, sec, min, hour, day

How It Works

# 1. Unit Conversion Function

The "unit_conversion()" function handles Length, Weight, and Time conversions.

It uses a common base unit to calculate the conversion.

Formula:

Base Value = Input Value × Source Unit Factor

Result = Base Value ÷ Destination Unit Factor

# 2. Temperature Conversion Function

The "temperature_conversion()" function handles Celsius, Fahrenheit, and Kelvin conversions.

Temperature requires separate conversion logic because its scales have different starting points and cannot be converted using simple multiplication factors.

# 3. Dictionaries

Dictionaries store the conversion factors for each category.

The program uses these dictionaries to validate units and perform conversions.

# 4. Input Validation

The program uses "try-except" to handle invalid numeric input and checks whether the entered units belong to the selected category.

# 5. Main Loop

A "while" loop keeps the application running and allows users to perform multiple conversions until they choose to exit.


This project demonstrates practical use of Python fundamentals and how different programming concepts work together to build a functional application.

# Author
Ravi Kishan 

This project is open-source and available for learning and educational purposes.
