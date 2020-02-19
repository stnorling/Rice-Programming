# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.

def smaller_root(a, b, c):
    """
    Solves for quadratic equation of given numbers a, b, c
    """
    
    # No solution exists if the discrinant part of the equation is < 0.
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print "Error: No real solutions"
        return None
    
    # Quadratic equation returns two solutions - we want to return the smallest.
    s1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    s2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    
    if s1 < s2:
        return s1
    else:
        return s2

###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    """Tests the smaller_root function."""
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None