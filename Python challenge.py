# Display all the prime numbers between 1 to 250.
# Store the results in a results.txt file.

# Initialize an empty list to store prime numbers
prime_numbers = []

# Iterate through numbers from 2 to 250
for num in range(2, 251):
    is_prime = True  # Assume the current number is prime
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False  # If a factor is found, mark the number as not prime
            break  # No need to continue checking for factors

    # If the number is still marked as prime, add it to the list
    if is_prime:
        prime_numbers.append(num)

'''        
for prime in prime_numbers:
    print (prime)
'''

# Open a file for writing and store the prime numbers in it
with open("prime_nums.txt", "w") as file:
    for prime in prime_numbers:
        file.write(f"{prime}\n")  # Write each prime number to a new line in the file


lower = 0
upper = 250
 
prime_nums = [];
 
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime_nums.append(num)
 
f = open('results.txt', 'w')
print((prime_nums), file = f)
 
print("List of prime numbers within range", lower, "to", upper, "are:", prime_nums)
