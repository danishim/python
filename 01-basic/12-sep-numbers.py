# Write a Python program that:
# 1. Creates a list containing positive, negative, and zero values.
# 2. Creates two empty lists: positive_numbers and negative_numbers.
# 3. Uses a for loop to separate positive and negative numbers.
# 4. Prints both lists.
# 5. Counts how many zeros are present.

def main():
  numbers = [10, -5, 20, 0, -15, 30, 0, -8, 12]
  positive_numbers=[]
  negative_numbers=[]
  zero_count =0
  
  for num in numbers:
    if num>0:
      positive_numbers.append(num)
    elif num<0:
      negative_numbers.append(num)
    else:
      zero_count += 1

  print(f"Positive numbers: {positive_numbers}")
  print(f"Negative numbers: {negative_numbers}")
  print(f"Zero count:  {zero_count}")

if __name__=="__main__":
  main()