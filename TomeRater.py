# CLASSES START HERE
# create the user
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # dictionary of books and ratings
        self.books = {}
    # get user's email address
    def get_email(self):
        return self.email
    # change user's email address and confirm the new email
    def change_email(self, address):
        self.email = address
        return "This user's email has been changed to: {email}".format(email=address)
    # gives you all the users info when printing
    def __repr__(self):
        return "User: {name} \nEmail: {email} \nBooks Read: {books}\n".format(name=self.name, email=self.email, books=len(self.books))
    # compares users to see if they have matching name/email
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
    # adds book to user
    def read_book(self, book, rating=None):
        self.books[book] = rating
    # gives you the average rating by the user
    def get_average_rating(self):
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)

# create a book
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        # list of all the ratings for the book
        self.ratings = []
    # gives you all the books info
    def __repr__(self):
        return "Title: {book} \nISBN: {isbn} \n".format(book=self.title,isbn=self.isbn)
    # gets the title of the book
    def get_title(self):
        return self.title
    # gets the ISBN of the book
    def get_isbn(self):
        return self.isbn
    # changes the ISBN of the book, and confirms the new number
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been changed to: {isbn}".format(isbn=new_isbn)
    # adds a rating to the book
    # doesn't allow errors outside of 0 and 4
    def add_rating(self, rating):
        try:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                return "Invalid Rating"
        except TypeError:
            "Invalid Type"
    # compares books to see if they have the same title/isbn
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
    # gives you the average rating for the book
    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)
    # makes the book list hashable
    def __hash__(self):
        return hash((self.title, self.isbn))

# create fiction subclass
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    # gives you books info
    def __repr__(self):
        return "{title} by {author}\n".format(title=self.title, author=self.author)
    # gives you the authors name
    def get_author(self):
        return self.author

# create nonfiction subclass
class Nonfiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    # gives you the subject of the book
    def get_subject(self):
        return self.subject
    # gives you the level of the book
    def get_level(self):
        return self.level
    # gives you the books info
    def __repr__(self):
        return "{title}, a {level} manual on {subject}\n".format(title=self.title, level=self.level, subject=self.subject)

# create tomerater class
class TomeRater(object):
    def __init__(self):
        # dictionary of User and their emails
        self.users = {}
        # dictionary of Book and number of Users that have read it
        self.books = {}
    # creates a book
    def create_book(self, title, isbn):
        return Book(title, isbn)
    # creates a fiction book
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    #creates non fiction book
    def create_non_fiction(self, title, subject, level, isbn):
        return Nonfiction(title, subject, level, isbn)
    # adds a book to user
    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email {email}".format(email=email))
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            # if the book was already there, add 1 to read count
            self.books[book] = self.books.get(book, 0) + 1
    # adds a user
    def add_user(self, name, email, books=None):
        if email not in self.users:
            self.users[email] = User(name, email)
            if books is not None:
                for book in books:
                    self.add_book_to_user(book, email)
            else:
                print("This user already exists.")
    # prints all the Books
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    # prints all the Users
    def print_users(self):
        for user in self.users.values():
            print(user)
    # shows the most read book
    def most_read_book(self):
        return max(self.books, key=self.books.get)
    # shows the highest rated book
    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating() for rating in self.books.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')
    # shows the user with the heighest average rating
    def most_positive_user(self):
        most_positive = max(rating.get_average_rating() for rating in self.users.values())
        return str([user for user in self.users.values() if user.get_average_rating() == most_positive]).strip('[]')



# CLASSES END HERE
