"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    abet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    passWs = []
    for chars1 in range(1,n+1):

        for chars2 in range(1,n+1):

            for chars3_find in range(l):
                chars3 = abet[chars3_find]

                for chars4_find in range(l):
                    chars4 = abet[chars4_find]

                    for chars5 in range(1,n+1):
                        if chars5 > chars1 and chars5 > chars2:
                            passWs.append(f"{chars1}{chars2}{chars3}{chars4}{chars5}")
    return passWs
stupidPassword(2,4)