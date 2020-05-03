# Examples of Sets 2

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

# when iterating through a set and removing items, you do not
# want to remove items as you iterate - this will get messy.
# instead, add the items to a new 'remove' set which you can later
# perform operations with. 

def get_rid_of(inst_set, starting_letter):
    remove_set = set([])
    for inst in inst_set:
        if inst[0] == starting_letter:
            remove_set.add(inst)
    # the set method a_set.difference_update(an_iter) mutates a_set to be 
    # the set difference of set a_set and the set of elements in iterable 
    # an_iter. Returns None.
    inst_set.difference_update(remove_set)

get_rid_of(instructors, 'W')
print instructors
