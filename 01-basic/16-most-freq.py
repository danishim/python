def most_freq_number():
  numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20]
  frequency = {}
  for num in numbers:
    if num in frequency:
      frequency[num] += 1
    else:
      frequency[num] = 1

  print(frequency)
  count = 0
  for k,v in frequency.items():
    if v > count:
      count = v
      key_count = k

  print(f"Most frequent number: {key_count}")
  print(f"Frequency: {frequency[key_count]}")

most_freq_number()