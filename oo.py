"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction allows us to consolidate shared attributes or behaviors into parent
    classes, and to use methods even without knowing quite how they work.
Encapsulation means data is well-contained and lives close to its functionality. 
Polymorphism: selective inheritance allows for interchangeable functionality.
    This keeps code adaptive, flexible, and dry.


2. What is a class?

A class is a group that can share structure, attributes, and/or behaviors. 


3. What is a method?

A method is a function that applies to a class.


4. What is an instance in object orientation?

An instance is a specific occurrence of a given class.


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute applies broadly to all members of a class unless otherwise 
specified, whereas an instance attribute applies only to a specific object.
For example, I can assign the 5th grade reader to my 5th grade students as a 
class attribute, and specifically designate a lower or higher reader to an
individual student as an instance attribute, on a case by case basis.
The instance attribute will override the assignment in the individual's
case but won't impact the default for other present and future class members. 
"""


"""2. Road Class"""


class Road:
    """ A road object."""

    num_lanes = 2
    speed_limit = 25

road_1 = Road()
road_2 = Road()

road_1.num_lanes = 4
road_1.speed_limit = 60


"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password
    
    def update_password(self, current_password, new_password):

        if current_password == self.password:
            self.password = new_password
        else:
            print('Invalid password')


"""4. Build a Library"""


class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"
    

class Library:
    """A Library object."""

    def __init__(self):
        """Create a library."""

        self.books = []

    def create_and_add_book(self, title, author):
        """Instantiate a new Book object and add to the library's book list."""

        new_book = Book(title, author)
        self.books.append(new_book)

    def find_books_by_author(self, author):
        """Search by author, returning a list of books by that author.
        
        Note: Assignment language is vague, such that "books" by the author
        can be interpreted as "book titles" or "Book objects." Because "book" 
        was not capitalized, I have chosen to interpret it as the book title.

        However, to return a list of objects instead, line 122 should read: 
                books_by_author.append(book)
        """

        books_by_author = []

        for book in self.books:
            if author == book.author:
                books_by_author.append(book.title)
        
        return books_by_author


"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width


class Square(Rectangle):
    """A Square type of Rectangle."""

    def __init__(self, side):
        """Create a square with identical length and width."""

        super().__init__(side, side)
    
    def calculate_area(self):
        """Return the area if the Square passes validation."""

        if self.length == self.width:
            return super().calculate_area()
        else:
            print("Invalid square")
            return None

