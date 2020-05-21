"""
Merge function for 2048 game.
"""

def slide(line):
    """
    Function that slides across numbers from right to left if there are zeroes
    """
    for num in range(len(line) -1):
        if line[num] == 0:
            for tile in range(num, len(line)):
                if line[tile] > 0:
                    line[num] += line[tile]
                    line[tile] = 0
                    break
    return line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """    
    new_line = slide(list(line))
    for num in range(len(new_line) - 1):
        if new_line[num] == new_line[num + 1]:
            new_line[num] += new_line[num + 1]
            new_line[num + 1] = 0
            slide(new_line)     
    return new_line


print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])
print merge([8, 0, 0, 8])