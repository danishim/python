def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a == b and b == c:
        print(f"All numbers are equal: {a}")
        return
    
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print(f"The largest number is {largest}")

if __name__ == "__main__":
    main()