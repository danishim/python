# Write a Python program that:
# 1. Creates a list of 10 numbers.
# 2. Uses a for loop to iterate through the list.
# 3. Prints only the even numbers.
# 4. Counts how many even numbers are present.
# 5. Prints the total count.

def main():
  numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
  count_even=0
  for num in numbers:
    if num % 2 == 0:
      print(num)
      count_even += 1

  print(f"Total even numbers: {count_even}")

if __name__=="__main__":
  main()