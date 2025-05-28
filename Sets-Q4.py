# add() method
numbers = {1, 2, 3} 
numbers.add(4) 
print(numbers)  

# update() method
numbers.update([5, 6]) 
print(numbers)  

# remove() method
numbers.remove(3) 
print(numbers)

# discard() method 
numbers.discard(7)  
print(numbers)  
 
 # pop() method
numbers.pop() 
print(numbers) 

# clear() method
items = {1, 2, 3} 
items.clear() 
print(items) 

# union() method
n1 = {1, 2} 
n2 = {1, 2, 3, 4} 
print(n1.union(n2))  

# intersection() method
print(n1.intersection(n2))  

# difference() method
print(n1.difference(n2))  

# issubset(), issuperset() method
print(n1.issubset(n2))   
print(n1.issuperset(n2))
 

 