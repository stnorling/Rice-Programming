n = 1000

numbers = [i for i in range(2, n)]

results = []

while numbers:
    i = numbers[0]
    results.append(i)
    for j in numbers:
        if j % i == 0:
            numbers.remove(j)

print len(results)