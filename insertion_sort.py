def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer number with space: ").split()))
    sorted_numbers = insertion_sort(numbers)
    print("Sorted number is", sorted_numbers)
