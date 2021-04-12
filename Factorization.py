

def isprime(number, primes):
    flag = True
    for i in range(len(primes)):
        if number % primes[i] == 0:
            flag = False
            break
    if flag:
        primes.append(number)


factors = []
primes = [2]
number_input = int(input("Input the number you want to factorize: "))
number_used = number_input + 0
flag2 = True
for number in range(3, number_input, 2):
    isprime(number, primes)

while flag2:
    for j in primes:
        if number_used % j == 0:
            factors.append(j)
            number_used = number_used // j
            break
        if number_used == 1:
            flag2 = False
print(number_input, "can be factorized into", factors)
input()
