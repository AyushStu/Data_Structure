# Problem: Return indices of the two numbers that add up to target

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i

# Example
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]