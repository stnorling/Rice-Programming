# If we want to split a list my_list into two halves, 
# which of the following uses slices to do so correctly?

# More precisely, if the length of my_list is 2n, i.e., 
# even, then the two parts should each have length n. 
# If its length is 2n+1, i.e., odd, then the two parts
# should have lengths n and n+1.

mylist = [1, 2, 3, 4, 5, 6,]

a = mylist[0:len(mylist) // 2] 
b = mylist[len(mylist)//2:len(mylist)]
           
print a
print b

a = mylist[:len(mylist) // 2] 
b = mylist[len(mylist)//2:]
           
print a
print b