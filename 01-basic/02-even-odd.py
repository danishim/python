# number = int(input("Enter an integer: "))

# if number % 2 == 0:
# 	print("Even")
# else:
# 	print("Odd")



def main():
    number = int(input("Enter number: "))

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


if __name__ == "__main__":
    main()