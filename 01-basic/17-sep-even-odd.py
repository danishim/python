def sort_numbers():
  numbers = [10, 15, 20, 25, 30, 35, 40, 45]
  evens = []
  odds = []
  esum = 0
  osum = 0

  for num in numbers:
    if num%2 == 0:
      evens.append(num)
      esum += num
    else:
      odds.append(num)
      osum += num

  print(f"Even numbers: {evens}")
  print(f"Odd numbers: {odds}")
  print(f"Sum of Even numbers: {esum}")
  print(f"Sum of Odd numbers: {osum}")

sort_numbers()