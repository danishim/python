# Write a program that:
# 1. Creates a list of 8 numbers.
# 2. Calculates the sum of all numbers.
# 3. Calculates the average.
# 4. Prints both results.

def main():
  numbers = [10, 20, 30, 40, 50, 60, 70, 80]
  total_sum = 0
  total_num = 0
  for num in numbers:
    total_sum += num 
    total_num += 1

  average = total_sum/total_num

  print(f"Total sum: {total_sum}")
  print(f"Average: {average}")

if __name__=="__main__":
  main()
