# Task: Write a Python program that:
# 1. Creates a list of five numbers.
# 2. Prints the first element.
# 3. Prints the last element.
# 4. Changes the second element to 100.
# 5. Prints the updated list.

def main():
  numbers = list(range(5))
  print(numbers[0])
  print(numbers[-1])
  numbers[1]=100
  print(numbers[1])
  print(numbers)

if __name__ == "__main__":
  main()
