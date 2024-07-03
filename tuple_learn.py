# Creating Nested Tuple
tuple1 = (4, 2, 3)
tuple2 = ('banana', 'mango', 'apple')

nested_tuple = (tuple1, tuple2)
print(nested_tuple)

# Sort Tuple

# When sorting tuple it return as list
sorted_tuple = tuple(sorted(tuple1))
print(sorted_tuple)

# Sort Reverse
sorted_reverse = tuple(sorted(tuple1, reverse=True))
print(sorted_reverse)

print('')


# Find Shortest word
def shortest(obj):
    words_length = []
    for item in obj:
        words_length.append(len(item))

    # Following method (min) returns that minimum number that stored in this list
    shortest_word_length = min(words_length)

    # Find index from the item
    shortest_word_index = words_length.index(shortest_word_length)

    # Return the shortest word
    return obj[shortest_word_index]


print(f'Shortest word is {shortest(['java', 'javascript', 'python'])}')
