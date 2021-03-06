-   This approach is based on observing that the right-hand bit value is
    easily identified (the remainder of the decimal number when divided by 2
    will be 1 i.e. it's an odd number).
    The number can then be divided by 2, which moves all the digits one place
    to the right, and so the next bit becomes the right-hand bit.
-   Make variables called "decimal number", which is number that user enters
    as the input, “binary number”, which is type string and it will be used
    to store 0’s and 1’s that represent the binary number as the output,
    and “remainder”, which stores the remainders of values for “decimal
    number” divided by 2.
-   Divide “decimal number” by 2.
    Round down the result to the nearest integer by using the floor function
    (choose the “floor” option from the drop down menu
    `scratch:([sqrt v] of [9])` under the “Operators”) and set “decimal
    number” to this value.
    For example using “floor” function if you divide 11 by 2 would give
    you ‘5’.
-   Store the remainder in variable “remainder” (use the `scratch:() mod ()`
    operation under “Operators” which reports the remainder from division of
    first number by second number).
    Combine “remainder” values using the `scratch:join [] []` block under the
    “Operators” and store the result in the “binary number” variable.
-   Repeat these blocks until “decimal number” is equal to ‘1’ (Use the
    `scratch:repeat until <>` block under the “Control”.
-   Add “decimal number” (which is now ‘1’) to “binary number” and display it
    as the output.
