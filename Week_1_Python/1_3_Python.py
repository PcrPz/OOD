print("*** Fun with permute ***")
numbers = [int(x) for x in input('input : ').split(',')]
print("Original Cofllection: ", numbers)

data = [[]]
for i in numbers:
    new_data = []
    for j in data:
        for k in range(len(j) + 1):
            new_data.append(j[:k] + [i] + j[k:])
            data = new_data
print("Collection of distinct numbers:\n", data)

