This code is designed to take in 2 binary codes as well as an operation such as +, -, *. or /.

the code takes in those three inputs and puts the sign between the two binary codes, and an answer is returned in a single binary code.

When the two binary codes are calculated using the sign its given, a number output will come out. 

the output is then checked.

if the inputs works and both numbers using the sign outputs a number between 0 and 255, then the code would turn that number into binary code and return that, outputs like "10011010"

If the output is greater than 255 or less than 0, the code will return the word "Overflow", this is beause 8-bit binary can only support numbers between 0 and 255. 

Any numbers greater than or less than those boundries cannot be represented by a single binary code.

If the second binary code that is input is equal to 0, than the code will return the word "NaN" meaning "not a number"

If the either of the two binary codes that are input have any characters that aren't a 1 or 0, then the code returns the word "Error"

To run the code one would go to the terminal and type "python3 calculator.py" and hit enter, this would run the code and one of the previous answers would be output.

We made this code to learn how binary code turns into numbers into binary code and vis versa.


[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17648297)
# Binary Calculator

<!--

The following requirements must be met to receive full credit on this assignment. The calculator must handle binary arithmetic operations accurately while following proper error handling procedures and output formatting guidelines.

- Your solution must have a well-written and thorough README file.
Good - The solution must be implemented as a function called `binary_calculator()` with three parameters:
Good     - `bin1` - A string parameter representing the first binary number to be used in the calculation. Must contain only 0s and 1s.
Good     - `bin2` - A string parameter representing the second binary number to be used in the calculation. Must contain only 0s and 1s.
Good     - `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`
Good - Do not use Python's built-in `bin()` function.
Good - Implement your own binary-to-decimal and decimal-to-binary conversion logic.
Good - All binary inputs and outputs should be strings.
Good - Handle division by zero by returning `"NaN"`
Good - Handle decimal numbers by rounding down to the nearest whole number (flooring).
Good - Return `"Error"` for invalid binary inputs (containing characters other than `0` and `1`)
Good - Return `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).
Good - Outputs must be returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Your solution will be tested against various test cases including edge cases, invalid inputs, and all four arithmetic operations.

 -->