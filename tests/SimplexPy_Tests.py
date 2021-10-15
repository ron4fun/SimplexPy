"""
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
    
    3. This notice must not be removed or altered from any source distribution.
"""

import unittest
from SimplexPy import *

class SimplexPyTests(unittest.TestCase):

    def test_2ProblemVariables_and_2SlackVariables(self):
        # problem setup
        problem = [
            ['w1',-1,2,1,0,6],
            ['w2',5,4,0,1,40],
            ['P',-1,-4,0,0,0]
        ]

        result = SimplexPy.SolveEq(problem, 2)

        #
        self.assertEqual(4, int(result['x1']))
        self.assertEqual(5, int(result['x2']))
        self.assertEqual(24, int(result['Pmax']))

    def test_2ProblemVariables_and_3SlackVariables(self):
        # 1 - problem setup
        problem = [
            ['w1',0,1,1,0,0,3],
            ['w2',1,1,0,1,0,5],
            ['w3',1,-2,0,0,1,2],
            ['P',-1,-2,0,0,0,0]
        ]

        result = SimplexPy.SolveEq(problem, 2)

        #
        self.assertEqual(2, int(result['x1']))
        self.assertEqual(3, int(result['x2']))
        self.assertEqual(6, int(result['w3']))
        self.assertEqual(8, int(result['Pmax']))
    
        # 2 - problem setup
        problem = [
            ['w1',-1,1,1,0,0,4],
            ['w2',1,2,0,1,0,14],
            ['w3',2,1,0,0,1,16],
            ['P',-4,-3,0,0,0,0]
        ]

        result = SimplexPy.SolveEq(problem, 2)

        #
        self.assertEqual(6, int(result['x1']))
        self.assertEqual(4, int(result['x2']))
        self.assertEqual(6, int(result['w1']))
        self.assertEqual(36, int(result['Pmax']))
        
        # 3 - problem setup
        problem = [
            ['w1',2,1,1,0,0,150],
            ['w2',4,3,0,1,0,350],
            ['w3',1,1,0,0,-1,80],
            ['P',-7,-4,0,0,0,0]
        ]

        result = SimplexPy.SolveEq(problem, 2)

        #
        self.assertEqual(50, int(result['x1']))
        self.assertEqual(50, int(result['x2']))
        self.assertEqual(20, int(result['w3']))
        self.assertEqual(550, int(result['Pmax']))

    def test_3ProblemVariables_and_3SlackVariables(self):
        # 1 - problem setup
        problem = [
            ['w1',2,5,2,1,0,0,38],
            ['w2',4,2,3,0,1,0,57],
            ['w3',1,3,5,0,0,1,57],
            ['P',-2,-6,-4,0,0,0,0]
        ]

        result = SimplexPy.SolveEq(problem, 3)
        print result
        #
        self.assertEqual(0, int(result['x1']))
        self.assertEqual(4, int(result['x2']))
        self.assertEqual(9, int(result['x3']))
        self.assertEqual(60, int(result['Pmax']))
    
        # 2 - problem setup
        problem = [
            ['w1',2,3,1,0,0,0,120],
            ['w2',1,1,0,1,0,0,45],
            ['w3',-3,5,0,0,-1,1,25],
            ['P',-8,-4,0,0,0,1,0]
        ]


        result = SimplexPy.SolveEq(problem, 3)

        #
        self.assertEqual(25, int(result['x1']))
        self.assertEqual(20, int(result['x2']))
        self.assertEqual(10, int(result['x3']))
        self.assertEqual(280, int(result['Pmax']))


    def test_3ProblemVariables_and_4SlackVariables(self):
        # problem setup
        problem = [
            ['w1',2,1,2,1,0,0,0,98],
            ['w2',1,1,1,0,1,0,0,60],
            ['w3',3,4,2,0,0,1,0,145],
            ['w4',4,3,2,0,0,0,1,160],
            ['P',-84,-72,-52,0,0,0,0,0],
        ]

        result = SimplexPy.SolveEq(problem, 3)

        #
        self.assertEqual(23, int(result['x1']))
        self.assertEqual(8, int(result['x2']))
        self.assertEqual(22, int(result['x3']))
        self.assertEqual(7, int(result['w2']))
        self.assertEqual(3652, int(result['Pmax']))

if __name__ ==  '__main__':
    unittest.main()
