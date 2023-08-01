def is_three_dimensional_array(arr):
    if isinstance(arr, list) and len(arr) > 0:
        if all(isinstance(level, list) for level in arr):
            if all(isinstance(row, list) for level in arr for row in level):
                # Additional check: Ensure that all levels have the same number of rows and columns
                level_shape = set((len(level), len(level[0])) for level in arr)
                if len(level_shape) == 1:
                    return True
    return False


three_dim_array = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
two_dim_array = [[1, 2, 3], [4, 5, 6]]
not_array = 42


print(is_three_dimensional_array(two_dim_array))
print()
print(is_three_dimensional_array(three_dim_array))
print()
print(is_three_dimensional_array(not_array))