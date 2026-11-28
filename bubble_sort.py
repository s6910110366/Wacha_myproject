def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break
    return numbers     

if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer number with space: ").split()))
    sorted_numbers = bubble_sort(numbers)
    print("Sorted number is", sorted_numbers)
    