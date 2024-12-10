import unittest
from library_system import LibraryManagementSystem, Book, User

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library_system = LibraryManagementSystem()

    def test_add_book(self):
        self.library_system.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        book = self.library_system.library.find_book("The Great Gatsby")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "The Great Gatsby")

    def test_add_user(self):
        self.library_system.add_user("john_doe", "John Doe", "john@example.com")
        user = self.library_system.library.find_user("john_doe")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "john_doe")
    
    def test_borrow_book(self):
        self.library_system.add_book("1984", "George Orwell", "Dystopian", 1949)
        self.library_system.add_user("alice_smith", "Alice Smith", "alice@example.com")
        self.assertTrue(self.library_system.borrow_book("alice_smith", "1984"))
    
    def test_return_book(self):
        self.library_system.add_book("1984", "George Orwell", "Dystopian", 1949)
        self.library_system.add_user("alice_smith", "Alice Smith", "alice@example.com")
        self.library_system.borrow_book("alice_smith", "1984")
        self.assertTrue(self.library_system.return_book("alice_smith", "1984"))
    
    def test_average_book_age(self):
        self.library_system.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        self.library_system.add_book("1984", "George Orwell", "Dystopian", 1949)
        self.assertEqual(self.library_system.average_book_age(), 87.0)
        # Test with no books
        self.library_system.library.books.clear()
        self.assertEqual(self.library_system.average_book_age(), 0)

    def test_most_popular_genre(self):
        self.library_system.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        self.library_system.add_book("1984", "George Orwell", "Dystopian", 1949)
        self.library_system.add_book("Brave New World", "Aldous Huxley", "Dystopian", 1932)
        self.assertEqual(self.library_system.most_popular_genre(), "Dystopian")
        # Test with no books
        self.library_system.library.books.clear()
        self.assertIsNone(self.library_system.most_popular_genre())
    
    def test_remove_book(self):
        self.library_system.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        self.assertTrue(self.library_system.remove_book("The Great Gatsby"))
        self.assertIsNone(self.library_system.library.find_book("The Great Gatsby"))
    
    def test_remove_user(self):
        self.library_system.add_user("john_doe", "John Doe", "john@example.com")
        self.assertTrue(self.library_system.remove_user("john_doe"))
        self.assertIsNone(self.library_system.library.find_user("john_doe"))
    
    def test_find_oldest_book(self):
        self.library_system.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        self.library_system.add_book("1984", "George Orwell", "Dystopian", 1949)
        self.assertEqual(self.library_system.find_oldest_book(), "The Great Gatsby by F. Scott Fitzgerald (1925)")
    
    def test_sort_books_by_year(self):
        self.library_system.add_book("1984", "George Orwell", "Dystopian", 1949)
        self.library_system.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        sorted_books = self.library_system.sort_books_by_year()
        self.assertEqual(sorted_books[0].year, 1925)
        self.assertEqual(sorted_books[1].year, 1949)

if __name__ == "__main__":
    unittest.main()
