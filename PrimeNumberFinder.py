def isprime(number, primes):
    flag = True
    for i in range(len(primes)):
        if number % primes[i] == 0:
            flag = False
            break
    if flag:
        primes.append(number)


primes = [2]
number_input = int(input("Input your search range"))
for number in range(3, number_input, 2):
    isprime(number, primes)
    print(primes[len(primes)-1])
print(primes)
input()
