# List comprehension can be thought of as having two operations: 
#		Computation (e.g. calculations/functions on the elements)
#		Filtering (e.g. if statements to filter out elements)
#
# These two operations can be performed individually or together.

def square_list1(numbers):
    """Returns a list of the squares of the numbers in the input."""
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

def square_list2(numbers):
    """Returns a list of the squares of the numbers in the input."""
    
    # below is our first example of list comprehension. computation is used per
    # element in the list. a temporary list is created and then returned.
    return [n ** 2 for n in numbers]

print square_list1([4, 5, -2])
print square_list2([4, 5, -2])



def is_in_range(ball):
    """Returns whether the ball is in the desired range.  """
    
    # below our function returns True for each argument (ball) that satisfies the
    # conditions (returns True), otherwise returns False.
    return ball[0] >= 0 and ball[0] <= 100 and ball[1] >= 0 and ball[1] <= 100


def balls_in_range1(balls):
    """Returns a list of those input balls that are within the desired range."""
    # Below is the long way of returning a list containing the filtered out balls.
    # List comprehension reduces this to one line of code.
    result = []
    for ball in balls:
        if is_in_range(ball):
            result.append(ball)
    return result

def balls_in_range2(balls):
    # Here is our list comprehension that utilizes filtering. The filter is
    # performed via our is_in_range() function, which returns either True or False.
    # The function is performed for each element in the balls argument. If True is
    # returned, the element is appeneded to the temporary list
    return [ball for ball in balls if is_in_range(ball)]

print balls_in_range1([[-5,40], [30,20], [70,140], [60,50]])
print balls_in_range2([[-5,40], [30,20], [70,140], [60,50]])
