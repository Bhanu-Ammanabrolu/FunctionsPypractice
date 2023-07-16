def prime_checker(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
    if is_prime:
        print("It is Prime Number")
    else:
        print("It is a NOT Prime Number")


num = int(input("Enter a number: "))

prime_checker(num)