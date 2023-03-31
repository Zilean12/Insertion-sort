# Insertion sort
arr = list(map(int, input("Enter the array elements: ").split()))

# Checking if the array is already sorted
if arr == sorted(arr):
    print("Sorted Array:", arr)
    print("Best Case: O(n)")
elif arr == sorted(arr, reverse=True):
    print("Sorted Array:", arr)
    print("Worst Case: O(n^2)")
else:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Sorted Array:", arr)
    print("Average Case: O(n^2)")
