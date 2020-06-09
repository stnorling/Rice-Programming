"""
Functions to enumerate sequences of outcomes
"""

# Enumeration - the action of mentioning a number of things one by one.
#				e.g. "the complete enumeration of all possible genetic states"


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    Number of sequences = outcomes (items) ^ length (of returned sequences)
    Repetition of outcomes is allowed
    """    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

# example for digits
def run_example1():
    """
    Example of all sequences
    """
    outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #outcomes = set(["Red", "Green", "Blue"])
    #outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    
    length = 2
    seq_outcomes = gen_all_sequences(outcomes, length)
    print "Computed", len(seq_outcomes), "sequences of", str(length), "outcomes"
    print "Sequences were", seq_outcomes


#run_example1()


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    This set will always have number of sequences: (n + m - 1)! / n! (m - 1)!
    """    
    all_sequences = gen_all_sequences(outcomes, length)
    # Below sorts the sequences, so that identical sequences are created, and then adds them 
    # to a set, so that only one sequence remains for each different handful of outcomes.
    # The sequences are made in to tuples, since the members of a set must be immutable.
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)


def run_example2():
    """
    Examples of sorted sequences of outcomes
    """
    # example for digits
    outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #outcomes = set(["Red", "Green", "Blue"])
    #outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    
    length = 2
    seq_outcomes = gen_sorted_sequences(outcomes, length)
    print "Computed", len(seq_outcomes), "sorted sequences of", str(length) ,"outcomes"
    print "Sequences were", seq_outcomes
    
run_example2()