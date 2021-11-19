def fizz_buzz(range_of_numbers=101):
    for num in range(1,range_of_numbers):
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        else:
            print(str(num))


range_of_numbers = input("Range of numbers for fizz-buzz?: ")
fizz_buzz(int(range_of_numbers))