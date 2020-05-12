# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            # return statemenet in a loop stops the loop from iterating further.
            return True
    return False

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            # Below results in error. You can not remove items from a list
            # while iterating through the list. (the list changes in size
            # as it iterates).
            numbers.remove(num)

def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        # Again we have an issue here, trying to remove items from a list
        # as we iterate through it.
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
    # Same issue as above.            
    for num in remove:
        numbers.remove(num)
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        # Smart way of dealing with the problem. Rather than accumulating
        # a list of the odd numbers we want to remove and removing them after,
        # we simply take the opposite (even numbers) and append these to
        # a new list.
        if num % 2 == 0:
            newnums.append(num)
    return newnums
   
def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = num
            
    if has_odd:
        # The below works, however it will remove the first instance of 
        # last_odd if last_odd occurs twice in the list. E.g. if last_odd
        # is the number 7, but 7 occurs earlier in the list, it will remove
        # the first instance of the number 7 rather than the last odd 
        # number in the list.
        numbers.remove(last_odd)
        
        
def remove_last_odd2(numbers):
    has_odd = False
    last_odd = 0
    # For cases where the last odd number occurs multiple times in the list,
    # to ensure the actual last odd number is removed, rather than its first
    # instance, we iterate through the length of the list (len(list)) and use
    # slice indexing of the list to ensure last_odd is the actual index 
    # of the last odd number. We then use the list pop method to remove the
    # corresponding index of the this number.
    for num in range(len(numbers)):
        if numbers[num] % 2 == 1:
            has_odd = True
            last_odd = num
            
    if has_odd:
        numbers.pop(last_odd)        
        

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd2(numbers)
    print numbers
    
run()