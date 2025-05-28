# Accessing items in a list 
books = ["The Hobbit", "To Kill a Mockingbird", "The Great Gatsby", "Harry Potter"] 
first_book = books[0]  
print("First book:", first_book) 

# Using loops with lists 
for book in books: 
    print("Book title:", book) 

# Adding item to a list
books.append("Pride and Prejudice")  
print("Books after addition:", books) 

# Removing item from a list 
books.remove("Harry Potter")  
print("Books after removal:", books) 

# Sorting a list 
books.sort()   
print("Sorted books:", books) 

# Copying a list 
books_copy = books.copy()   
print("Copied books:", books_copy) 

# Using list comprehension 
book_lengths = [len(book) for book in books]  
print("Length of book titles:", book_lengths) 
