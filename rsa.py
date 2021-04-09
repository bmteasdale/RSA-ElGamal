"""
Source File: rsa.py
Author: Brendan Teasdale
"""
import math

PUBLIC_KEY = {
    "n": 31313,
    "e": 4913
}

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def openingMessage():
    """First message to the user."""
    print("=" * 55)
    print("\nNote: ")
    print("Input of an RSA Encrypted message is required.")
    print("Public parameters of the system are n=31313 and e=4913\n")
    print("=" * 55)


def gcd(x:int, y:int) -> int:
    """The largest positive integer that divides each of the params."""
    if x == 0:
        return y
    return gcd(y % x, x)


def phi(n: int) -> int:
    """Euler's Totient Function, returns number of totatives of n"""
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


def decryptMessage():
    """Translates the plaintext back into ordinary English text"""
    exponents = [2, 1, 0]
    encryptedMessage = input("Please enter the RSA encrypted message: \n")
    messageSplit = encryptedMessage.split(" ")
    print("")
    for c in messageSplit:
        d = modInverse(PUBLIC_KEY["e"], phi(PUBLIC_KEY["n"]))
        p = (int(c) ** d) % PUBLIC_KEY["n"]
        for e in exponents:
            letter = math.trunc((p/pow(26, e)) % 26)
            print(ALPHABET[letter], end="")
        print(" ", end="")
    print("")


def modInverse(base: int, mod: int) -> int:
    """Modular multiplicative inverse"""
    return pow(base=base, exp=-1, mod=mod)


def main():
    """Execute's the program."""
    openingMessage()
    decryptMessage()


if __name__ == '__main__':
    main()
