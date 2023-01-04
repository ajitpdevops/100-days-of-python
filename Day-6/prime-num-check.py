n = int(input("Check this number: "))

def prime_checker(number):
    is_prime = True
    for num in range(2, n):
        if number % num == 0:
            is_prime = False
            
    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")

prime_checker(number=n)