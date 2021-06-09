# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath
import math

if __name__ == '__main__':
    
    z = complex(input())
    r,phase = cmath.polar(z)
    phase = cmath.phase(z)
    print(r)
    print(phase)   
    