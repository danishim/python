# Write a program that:
# 1. Creates a list of five fruits.
# 2. Adds "mango" to the end.
# 3. Inserts "orange" at index 1.
# 4. Removes "apple" from the list.
# 5. Prints the final list.

def main():
  fruits = ["apple", "banana", "grapes", "cherry", "kiwi"]
  fruits.append("mango")
  fruits.insert(1, "orange")
  # fruits.pop(0) removes an element using its index.
  fruits.remove("apple") # removes an element using its value.

  print(fruits)

if __name__=="__main__":
  main()