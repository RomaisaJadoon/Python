
studentmarks = (70, 82, 65, 90, 78) 
# printing first and last elements of tuple
print("First mark:", studentmarks[0])     
print("Last mark:", studentmarks[-1])  

# unpacking tuple elements
m1, m2, m3, m4, m5 = studentmarks 

print("Marks unpacked:") 
print("marks1 =", m1) 
print("marks2 =", m2) 
print("marks3 =", m3) 
print("marks4 =", m4) 
print("marks5 =", m5) 

# creating new tuple
newmarks = tuple(mark + 5 for mark in studentmarks) 

# printing original and new tuple
print("Original marks:", studentmarks) 
print("Updated marks (+5 each):", newmarks) 