def calculate_pairs(arr):
    # Iterate through the array by steps of 2
    for i in range(0, len(arr), 2):
        # Check if the pair is complete
        if i + 1 < len(arr):
            print(f"Index {i} + Index {i+1}:", arr[i] + arr[i+1])
        else:
            # If the last element doesn't have a pair, print it as it is
            print(f"Index {i}:", arr[i])

# Example usage:
arr = [1, 2, 3, 4, 5]
calculate_pairs(arr)
