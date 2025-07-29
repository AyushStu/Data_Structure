# Problem: Search for an element using linear search

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Example
print(linear_search([5, 8, 2, 9], 2))  # Output: 2