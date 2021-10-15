#SimplexPy#



`SimplexPy` is a compact python library that automatically solves `Linear Programming Equations` i.e Maximization problems, easily and quickly while giving you neat results. To run unittest check in the test folder.



Example
---------

```python

"""
Solve using the Simplex method the following problem:
Maximize 	Z = f(x,y) = 3x + 2y
subject to: 	2x + y ≤ 18
                2x + 3y ≤ 42
                3x + y ≤ 24
                x ≥ 0 , y ≥ 0
"""
def main():
	
    # problem setup
    problem = [
        ['w1',2,1,1,0,0,18],
        ['w2',2,3,0,1,0,42],
	['w3',3,1,0,0,1,24],
        ['P',-3,-2,0,0,0,0]
    ]

    result = SimplexPy.SolveEq(problem, 2) # where 2 is the total number of variables

    """
    {'w4': Fraction(0, 1), 'w3': Fraction(3, 1), 'w2': Fraction(0, 1), 
	'w1': Fraction(0, 1), 'x2': Fraction(12, 1), 'x1': Fraction(3, 1),
	'Pmax': Fraction(33, 1)}
"""
```


License
----------
    Copyright (c) 2021 Mbadiwe Nnaemeka Ronald ron2tele@gmail.com

    This software is provided 'as-is', without any express or implied
    warranty. In no event will the author be held liable for any damages
    arising from the use of this software.
    Permission is granted to anyone to use this software for any purpose,
    including commercial applications, and to alter it and redistribute it
    freely, subject to the following restrictions:
    
    1. The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software
    in a product, an acknowledgment in the product documentation must be
    specified.
    
    2. Altered source versions must be plainly marked as such, and must not be
    misrepresented as being the original software.
    
    3. This notice may not be removed or altered from any source distribution.
        
        