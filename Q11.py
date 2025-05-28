def classify_numbers(number_list): 

    positive_number = 0 
    zero = 0 
    negative_number = 0 

    for num in number_list: 
        if num > 0: 
            print(num, "is positive") 
            positive_number += 1 

        elif num == 0: 
            print(num, "is zero") 
            zero += 1 

        else: 
            print(num, "is negative") 
            negative_number += 1 

 

    result = { 

        "positive": positive_number, 
        "zero": zero, 
        "negative": negative_number 

    } 
    return result 

  
userinput = input("Enter numbers separated by spaces: ") 

number_list = list(map(int, userinput.split())) 
result = classify_numbers(number_list) 

print("\nResult:") 
print(result) 