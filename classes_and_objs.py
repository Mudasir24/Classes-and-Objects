# A class named Book with attributes: title, author, and genre
class Book:

    # Initializing object attributes
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre

    # Method to display information about book
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

# Creating instances of the Book class
my_book1 = Book("The Great Gatsby","F. Scott Fitzgerald","Fiction")
my_book2 = Book("Atomic Habits","James Clear","Nonfiction")

# Displaying the info of book1
print("Book:1 ")
my_book1.display_info()

# Displaying the info of book2
print("\nBook:2")
my_book2.display_info()
