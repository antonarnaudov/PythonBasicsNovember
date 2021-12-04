command = input()
prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command != 'stop':
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    number_is_prime = True
    for num in range(2, number):
        if number % num == 0:
            number_is_prime = False
            break

    if number_is_prime:
        prime_numbers_sum += number
    else:
        non_prime_numbers_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
