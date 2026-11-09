def main():
  data = input(f"Enter a sentence: ").lower()
  vowel = 0

  for letter in data:
    if letter in ['a', 'e', 'i', 'o', 'u']:
      vowel = vowel + 1

  print(f"Number of vowels: {vowel}")

if __name__ == "__main__":
  main()