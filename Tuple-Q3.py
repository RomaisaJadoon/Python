
my_tuple = (10, 20, 30, 40, 50) 
# Accessing items in tuple
first_item = my_tuple[0]  
second_item = my_tuple[1]  
print("First item:", first_item) 
print("Second item:", second_item) 

cars = ('BMW', 'Mclaren', 'Audi', 'Dodge') 
# Looping through a tuple 
for car in cars: 
    print(car) 
    tuple1 = (1, 2, 3) 
tuple2 = (4, 5, 6) 

# Concatenating tuples 
concatenated_tuple = tuple1 + tuple2 
print("Concatenated Tuple:", concatenated_tuple) 
maintuple = (1, 2, 3, 4, 5) 

# modifying the tuple
tlist = list(maintuple)
tlist[1] = 20 
newtuple = tuple(tlist) 
print("Original Tuple:", maintuple) 
print("Modified Tuple:", newtuple) 
countryinfo = ("Pakistan", "255.5million" , "$411Billion") 

# Unpacking the tuple 
countryname, population, gdp = countryinfo 
print("Country:", countryname) 
print("Population:", population) 
print("GDP:", gdp) 

my_tuple = (1, 2, 3, 4, 2, 5, 2) 
# Count() method
count_of_twos = my_tuple.count(2) 
print("The number 2 appears", count_of_twos, "times in the tuple.") 

mytuple = (10, 20, 30, 40, 50, 20) 
# index() method 
index_of_50 = mytuple.index(50) 
print("The index of occurrence of 50 in the tuple is:", index_of_50) 

 