def find_second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements."

    # Set initial values to None
    largest = None
    second_largest = None

    for num in arr:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num != largest):
            second_largest = num

    if second_largest is None:
        return "No second largest element."
    
    return second_largest

# Get input from user
user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.split()))

# Output the result
print("Second largest element:", find_second_largest(arr))


















