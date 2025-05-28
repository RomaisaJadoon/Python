numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11] 

divisible_by_3 = 0 
even = 0 
odd = 0

# looping through each number

for num in numbers:
    if num % 3 == 0: 
        print(num, "is divisible by 3") 
        divisible_by_3 += 1 

    elif num % 2 == 0: 
        print(num, "is even but not divisible by 3") 
        even += 1 

    else: 
        print(num, "is odd and not divisible by 3") 
        odd += 1
        

print("Results:") 

print("Numbers divisible by 3:", divisible_by_3) 
print("Even numbers (not divisible by 3):", even) 
print("Odd numbers (not divisible by 3):", odd) 

 