def remove_duplicates(arr):
    # Convert array elements to keys in a dictionary (keys are unique)
    no_duplicates_dict = {x: True for x in arr}
    print(no_duplicates_dict)
    # Get the keys back as a list to retrieve unique values
    unique_values = list(no_duplicates_dict.keys())

    return unique_values


# Example usage:

my_array = [1, 2, 2, 3, 4, 4, 5,6,6,7,7,8,8,88,9,9,9,9,9]
result = remove_duplicates(my_array)
print(result)  # Output: [1, 2, 3, 4, 5]

