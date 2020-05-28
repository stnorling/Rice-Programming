"""
Example of testing, comparing a bug function to the correct function.
The test runs through all possible iterations and returns any mismatches.

For any returned errors, the given index should be used as a test case for the function.
"""

# Bad time format (erroneous method.. could be any erroneous method) below

def bad_format(t):
    a = (t // 600)
    b = (((t % 600) / 10) / 10)
    c = '0'
    if (t > 10):
        c = str(t)[(-2)]
    d = str(t)[(-1)]
    formatedTime = (((((str(a) + ':') + str(b)) + c) + '.') + d)
    return formatedTime

# Correct time format below

def good_format(t):
    a = t / 600
    b = t / 100 % 6
    c = t / 10 % 10
    d = t % 10
    return str(int(a)) + ":" + str(int(b)) + str(int(c)) + "." + str(int(d))

# TEST_CASES - testing for bad format using all possible cases (0 -> 6,000)
# Comparing correct format to incorrect format and displaying errors if there are any

def Checker():
    TEST_CASES = list(range(6000))
    for item in TEST_CASES:
        bad_result = bad_format(item)
        good_result = good_format(item)
        for str_idx in range(6):
            if bad_result[str_idx] != good_result[str_idx]:
                print 'wrong: '+str(item)
                return 'Mistake at list index ' + str(item) + '\n' + 'Returned ' + bad_result + '\n' + 'Expected ' + good_result
    return 'No errors'

print Checker()

