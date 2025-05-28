# function to check if number is even or odd 

def check_even_odd(number):  

    if number % 2 == 0: 
        print("The number is even") 

    else: 
        print("The number is odd") 

 
userinput = int(input("Enter a number: ")) 
check_even_odd(userinput) 