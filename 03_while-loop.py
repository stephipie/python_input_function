while True:
    number = int(input("Please enter a number: \n"))
    if number % 2 == 0:
        print(f"{number} is even.")
        break
    else:
        print("The number is odd. Please enter an even number.")