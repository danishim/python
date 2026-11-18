def find_large_small_num():
    numbers = []

    for _ in range(5):
        num = int(input("Enter number: "))
        numbers.append(num)

    largest_number = numbers[0]
    smallest_number = numbers[0]

    for num in numbers:
        if num > largest_number:
            largest_number = num

        if num < smallest_number:
            smallest_number = num

    print(f"Largest number: {largest_number}")
    print(f"Smallest number: {smallest_number}")


find_large_small_num()