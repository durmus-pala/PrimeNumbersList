number = input("Please enter your number to list prime numbers: ")
prime_numbers = []
for i in range(1, int(number) + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)            
print("All Prime numbers until this number are: ", prime_numbers)
         
