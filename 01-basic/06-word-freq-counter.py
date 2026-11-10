# Write a Python program that accepts a sentence and counts how many times each word appears.
def main():
  word_count = {}
  sentence = input("Enter sentence: ")

  for word in sentence.split():
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1

  print(word_count)


if __name__ == "__main__":
  main()