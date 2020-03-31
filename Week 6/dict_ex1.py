# Day to number dictionary problem

###################################################
# Student should enter code below

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_to_number = {}

for k in days:
    day_to_number[k] = days.index(k)

#print day_to_number
###################################################
# Test data

print day_to_number["Sunday"]
print day_to_number["Monday"]
print day_to_number["Tuesday"]
print day_to_number["Wednesday"]
print day_to_number["Thursday"]
print day_to_number["Friday"]
print day_to_number["Saturday"]

###################################################
# Sample output

#0
#1
#2
#3
#4
#5
#6
