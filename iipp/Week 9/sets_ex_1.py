# Examples of Sets 

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

# duplicate items do not get appened to the set multiple times.
# can not have duplidates in a set.

inst2 = set(['Rixner', 'Rixner', 'Warren', 'Warren', 'Greiner', 'Wong'])
print inst2

# can compare sets
print instructors == inst2

# can iterate through a set
for inst in instructors:
    print inst

# can add items to sets using the add method. (if item already exists, will
# not add a duplicate. no error is thrown. 
instructors.add('Colbert')
print instructors
instructors.add('Rixner')
print instructors

# can remove items in a set using the remove method.
instructors.remove('Wong')
print instructors

# can check if an element is in a given set (returns True or False).
print 'Rixner' in instructors
print 'Wong' in instructors
