# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath


c = complex(input())
r, phi = cmath.polar(c)
# r = c.real
# phi = c.imag

print(r, phi, sep='\n')
