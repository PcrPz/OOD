original_list = [1, 2, 3]
subsets = [[]]

for num in original_list:
    new_subsets = [subset + [num] for subset in subsets]
    subsets.extend(new_subsets)

# Filter out the empty subset (the first one)
subsets = subsets[1:]

print(subsets)