# Section: 5. Building Balanced Binary Search Trees

# Task 1
# Write a function that outputs an array containing the structure of a balanced BST

# Method: def GenerateBBSTArray(a: list) -> list:
# Computational complexity: O(n log n) - where n is the number of nodes in the tree

# Solution:
# First, I sort the array in O(n log n).
# The position in the tree does not depend on the value itself, but on its position in the sorted array.
# Then I generate an array of positions from which to take values in order to fill the array that represents
# the structure of the balanced BST.
# Finally, I form the result.
# Constructing the final result and generating the array of positions to take values from has a computational complexity of O(n),
# where n is the number of keys in the tree.


# Task 2
# Evaluate whether searching for a node in a tree represented as an array is more efficient
# (or less efficient) than searching for a node in a classical tree with pointers.
#
# They are the same. O(log n). In one case we move to the next array cell, 
# in the other case to the next node object.
# The number of steps is the same.


def _GenerateBBSTIndexOrder(count: int):
    if count == 0:
        return []
    
    index_order_result = [None] * count

    ranges = [(0,count-1,0)]
    while len(ranges) > 0:
        next_ranges = []
        for left_index, right_index, position in ranges:
            if position >= len(index_order_result):
                index_order_result.extend([None] * (position+1-len(index_order_result)))


            if left_index == right_index:
                index_order_result[position] = left_index
                continue

            mid_index = (left_index + right_index +1)//2
            index_order_result[position] = mid_index

            next_ranges.append((left_index,mid_index-1,2*position+1))
            if right_index-left_index > 1:
                next_ranges.append((mid_index+1,right_index,2*position+2))

        ranges = next_ranges
    
    return index_order_result


def GenerateBBSTArray(a: list) -> list:
    idxs = _GenerateBBSTIndexOrder(len(a))
    sorted_a = sorted(a)
    result = []
    for idx in idxs:
        if idx is None:
            result.append(None)
            continue
        result.append(sorted_a[idx])
    return result



