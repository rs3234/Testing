class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    def age(self, current_year=2024):
        return current_year - self.year

# Added more library methods coverage, handling empty cases, and edge cases.
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_user(self, user):
        self.users.append(user)
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def borrow_book(self, username, title):
        book = self.find_book(title)
        user = self.find_user(username)
        if book and user:
            if book not in user.borrowed_books:
                user.borrowed_books.append(book)
                return True
        return False
    
    def return_book(self, username, title):
        user = self.find_user(username)
        if user:
            for book in user.borrowed_books:
                if book.title == title:
                    user.borrowed_books.remove(book)
                    return True
        return False
    
    def average_book_age(self):
        current_year = 2024
        total_age = 0
        if not self.books:
            return 0  # Return 0 if there are no books
        for book in self.books:
            total_age += book.age(current_year)
        return total_age / len(self.books)
    
    def most_popular_genre(self):
        if not self.books:
            return None  # No genre if no books
        genre_count = {}
        for book in self.books:
            if book.genre not in genre_count:
                genre_count[book.genre] = 1
            else:
                genre_count[book.genre] += 1
        return max(genre_count, key=genre_count.get, default=None)
    
    def user_borrowed_books(self, username):
        user = self.find_user(username)
        if user:
            return [str(book) for book in user.borrowed_books]
        return []
    
    def remove_book(self, title):
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            return True
        return False

    def remove_user(self, username):
        user = self.find_user(username)
        if user:
            self.users.remove(user)
            return True
        return False
    
    def all_books(self):
        return [str(book) for book in self.books]
    
    def all_users(self):
        return [str(user) for user in self.users]
    
    def count_books(self):
        return len(self.books)
    
    def count_users(self):
        return len(self.users)
    
    def filter_books_by_genre(self, genre):
        return [str(book) for book in self.books if book.genre == genre]
    
    def filter_books_by_author(self, author):
        return [str(book) for book in self.books if book.author == author]
    
    def find_oldest_book(self):
        if not self.books:
            return None
        oldest_book = min(self.books, key=lambda book: book.year)
        return str(oldest_book)
    
    def find_newest_book(self):
        if not self.books:
            return None
        newest_book = max(self.books, key=lambda book: book.year)
        return str(newest_book)
    
    def sort_books_by_year(self):
        return sorted(self.books, key=lambda book: book.year)

# User class remains the same.
class User:
    def __init__(self, username, full_name, email):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.borrowed_books = []
    
    def __str__(self):
        return f"{self.full_name} ({self.username})"
    
    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def borrowed_books_titles(self):
        return [book.title for book in self.borrowed_books]

# LibraryManagementSystem remains the same.
class LibraryManagementSystem:
    def __init__(self):
        self.library = Library()

    def add_book(self, title, author, genre, year):
        book = Book(title, author, genre, year)
        self.library.add_book(book)

    def add_user(self, username, full_name, email):
        user = User(username, full_name, email)
        self.library.add_user(user)
    
    def borrow_book(self, username, title):
        return self.library.borrow_book(username, title)
    
    def return_book(self, username, title):
        return self.library.return_book(username, title)

    def average_book_age(self):
        return self.library.average_book_age()

    def most_popular_genre(self):
        return self.library.most_popular_genre()

    def user_borrowed_books(self, username):
        return self.library.user_borrowed_books(username)
    
    def remove_book(self, title):
        return self.library.remove_book(title)
    
    def remove_user(self, username):
        return self.library.remove_user(username)
    
    def all_books(self):
        return self.library.all_books()
    
    def all_users(self):
        return self.library.all_users()
    
    def count_books(self):
        return self.library.count_books()
    
    def count_users(self):
        return self.library.count_users()
    
    def filter_books_by_genre(self, genre):
        return self.library.filter_books_by_genre(genre)
    
    def filter_books_by_author(self, author):
        return self.library.filter_books_by_author(author)
    
    def find_oldest_book(self):
        return self.library.find_oldest_book()
    
    def find_newest_book(self):
        return self.library.find_newest_book()
    
    def sort_books_by_year(self):
        return self.library.sort_books_by_year()
