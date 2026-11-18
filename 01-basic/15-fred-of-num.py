# Write a Python program that counts how many times each number appears in a list.
def count_numbers():
  numbers = [50, 10, 20, 10, 30, 20, 10, 40, 30, 20, 50, 50, 50, 50, 50]
  count = {}
  for num in numbers:
    # if count.get(num):
    #   count[num] += 1
    # else:
    #   count[num] = 1
    if num in count:
      count[num] += 1
    else:
      count[num] = 1
    
  print(count)

count_numbers()