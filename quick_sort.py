# Problem: Implement Quick Sort algorithm

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example
print(quick_sort([10, 3, 5, 1, 7]))  # Output: [1, 3, 5, 7, 10]