/**
 * Source File: RSA Cipher
 * Author: Brendan Teasdale
 */

#include <iostream>

//Prototypes
int gcd(int, int);
int phi();

/*!
 * @function    main
 * @abstract    Driver code to execute the program.
 * @discussion  main() function is the entry point for any C++ program.
 *              It is the point at which execution of program is started.
 *
 * @result      The integer exit code of the program.
*/
int main() {
    std::cout << "RSA Cipher" <<std::endl;
    return 0;
}

/*!
 * @function    gcd
 * @abstract    The largest positive integer that divides each of the params.
 * @discussion
 * @param       x    The first integer number.
 * @param       y    The second integer number.
 *
 * @result      The greatest common divisor of the two parameters.
*/
int gcd(int x, int y) {
    
}

/*!
 * @function    phi
 * @abstract    Euler's Totient Function
 * @discussion  Number of integers 'k' in the range 1 ≤ k ≤ n for which the greatest common divisor 'gcd(n, k)' is equal to 1.
 * @param       n    positive integer parameter of φ.
 *
 * @result      Number of totatives of n
*/
int phi(unsigned int n) {
    
}
