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

from fraction import fraction

class SimplexPy(object):
    @staticmethod
    def _SimplexEngine(arr, optimal  = True, optimal_col = 0):
        key_col = 0 # starts from index 1 and 0 means null
        key_row = 0 # starts from index 1 and 0 means null
        main_row = None
        pivot = {'row':0,'col':0}

        # get the key row
        count = 0
        for row in arr:
            if row[0] == 'P':
                key_row = count + 1
                break
            count += 1

        # get the key column
        if optimal:
            min_value = 0
            count = 0
            for col in arr[key_row-1]:
                if type(col) is not str:
                    if col < min_value:
                        min_value = col
                        key_col = count + 1
                count += 1
        else:
            key_col = optimal_col + 1
            
        # get the pivot
        smallest_postive_no = 0
        count = 0
        for row in arr:
            divisor = row[key_col - 1]
            if row[0] != 'P' and divisor != 0: 
                val = fraction(row[-1]) / divisor
                if val > 0 and smallest_postive_no == 0:
                    smallest_postive_no = val
                    pivot = {'row': count + 1,'col': key_col} 
                elif val > 0 and val < smallest_postive_no:
                    smallest_postive_no = val
                    pivot = {'row': count + 1,'col': key_col}
            count += 1
            
        # sanitize the key row
        val = arr[pivot['row'] - 1][pivot['col'] - 1]
        for i in range(1, len(arr[pivot['row'] - 1])):
            arr[pivot['row'] - 1][i] = fraction(arr[pivot['row'] - 1][i]) / val

        # sanitize the key col
        main_row = arr[pivot['row'] - 1]
        count = 0
        for row in arr:
            divisor = row[key_col - 1]
            if row[0] != arr[pivot['row'] - 1][0] and divisor != 0:                
                for i in range(1, len(row)):
                    arr[count][i] -= (main_row[i] * divisor)
            count += 1
            
        return arr

    @staticmethod
    def _IsOptimal(arr, no_variables):
        is_optimal = True
        col = 0
        for row in arr:
            if row[0] == 'P':
                for i in range(1, no_variables + 1):
                    if row[i] > 0:
                        col = i
                        is_optimal = False
                        break
        return is_optimal, col

    @staticmethod
    def _ShouldIterate(arr):
        iterate = False
        for row in arr:
            if row[0] == 'P':
                for i in range(1, len(row)):
                    if row[i] < 0:
                        iterate = True
                        break
        return iterate

    @staticmethod
    def _HasArtificialVariable(arr, no_variables):
        pos = no_variables
        for row in arr:
            if row[0] != 'P':
                for i in range(1, len(row) - 1): # without the constant `b`
                    if row[i] < 0:
                        return True
        return False
        
    @staticmethod
    def _ResolveResult(row, no_variables):
        if row[0] == 'P':
            return 'Pmax', row[-1]
        
        pos = 0
        for i in range(1, len(row) - 1): # without the constant `b`
            if row[i] == 1:
                pos = i
                break
            
        if pos > 0 and pos <= no_variables:
            return 'x{}'.format(pos), row[-1]
        if pos > 0 and pos > no_variables:
            return 'w{}'.format(pos - no_variables), row[-1]

        return ''

    @staticmethod
    def SolveEq(arr, no_variables):

        artificial_var = SimplexPy._HasArtificialVariable(arr, no_variables)
        
        arr = SimplexPy._SimplexEngine(arr)
        
        while SimplexPy._ShouldIterate(arr):
            arr = SimplexPy._SimplexEngine(arr)

        if artificial_var:
            optimal, col = SimplexPy._IsOptimal(arr, no_variables)
            while not optimal:
                arr = SimplexPy._SimplexEngine(arr, optimal, col)
                optimal, col = SimplexPy._IsOptimal(arr, no_variables)

        ans = {}
        for row in arr:
            res = SimplexPy._ResolveResult(row, no_variables)
            if res:
                ans[res[0]] = res[1]
                
        # clean result
        for n in range(1, no_variables + 1):
            try:
                ans['x{}'.format(n)]
            except:
                ans['x{}'.format(n)] = fraction(0)

        for n in range(1, len(arr) + 1):
            try:
                ans['w{}'.format(n)]
            except:
                ans['w{}'.format(n)] = fraction(0)
                
        return ans

if __name__ ==  '__main__':
    # problem setup
    problem = [
        ['w1',2,1,1,0,0,18],
        ['w2',2,3,0,1,0,42],
        ['w3',3,1,0,0,1,24],
        ['P',-3,-2,0,0,0,0]
    ]

    result = SimplexPy.SolveEq(problem, 2) # where 2 is the total number of variables

    print(result)
