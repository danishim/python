# Write a Python program that finds the second-largest distinct number in a list.


def main():
    numbers = [10, 25, 8, 45, 30, 45, 15]

    largest_num = float('-inf')
    sec_largest_num = float('-inf')

    for num in numbers:
        if num > largest_num:
            sec_largest_num = largest_num # First, save the previous largest number as the second largest.
            largest_num = num # Then update the largest number.

        elif num < largest_num and num > sec_largest_num:
            sec_largest_num = num # This updates the second-largest number without changing the largest.

    if sec_largest_num == float('-inf'):
        print("No second-largest distinct number exists")
    else:
        print(f"Largest number: {largest_num}")
        print(f"Second largest number: {sec_largest_num}")


if __name__ == "__main__":
    main()
