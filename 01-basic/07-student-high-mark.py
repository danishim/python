# Write a Python program that:
# 1. Creates a dictionary containing three students and their marks.
# 2. Finds the student who scored the highest marks.
# 3. Prints the student's name and marks.

def main():
  dict_student = {
    "ali": 85,
    "sarah": 92,
    "jon":78
  }

  for student in dict_student:
    print(student)
    print(student[1])

  # print(f"Top student: {top_student}")
  # print(f"Highest marks: {highest_mark}")

if __name__ == "__main__":
  main()