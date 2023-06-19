def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Get input from the user
arr = list(map(int, input("Enter the elements of the array (separated by spaces): ").split()))

# Sort the array
arr.sort()

# Print the sorted array
print("Sorted array:", arr)

# Ask the user for the element to search
target = int(input("Enter the element to search: "))

# Perform binary search
index = binary_search(arr, target)

if index == -1:
    print("Element not found.")
else:
    count = 1
    # Count the number of occurrences of the element to the left
    left = index - 1
    while left >= 0 and arr[left] == target:
        count += 1
        left -= 1

    # Count the number of occurrences of the element to the right
    right = index + 1
    while right < len(arr) and arr[right] == target:
        count += 1
        right += 1

    print("Number of occurrences of element", target, "is:", count)
