# Write a Python program that accepts a list of numbers and identifies all duplicate numbers.
def main():
  data = input("Enter numbers: ")
  numbers = data.split(",")

  seen = set()
  duplicates = set()

  for number in numbers:
    number = int(number)
    if number not in seen:
      seen.add(number)
    else:
      duplicates.add(number)

  print(f"Numbers: {numbers}")
  print(f"Seen numbers: {seen}")
  if len(duplicates) > 0:
    print(f"Duplicate numbers: {duplicates}")
  else:
    print("No duplicates found")


if __name__ == "__main__":
  main()
