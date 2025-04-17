def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap


arr = [64, 25, 12, 22, 11]
print("Unsorted array:", arr)
selection_sort(arr)
print("Sorted array:", arr)

# Output:
'''
Unsorted array: [64, 25, 12, 22, 11]
Sorted array: [11, 12, 22, 25, 64]
'''