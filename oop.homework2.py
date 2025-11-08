class Book:

    def __init__(self, title, author, isbn):
        if not Book.is_valid_title(title):
            raise ValueError("namotabar")
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = True

    def borrow(self):
        if self.available:
            self.__mark_borrowed()
            print(f"{self.title} borrowed ")
        else:
            print("namojood")

    def return_book(self):
        self.available = True

    def __mark_borrowed(self):
        self.available = False

    @staticmethod
    def is_valid_title(title):
        i = 0
        while i < len(title):
            c = title[i]
            if not (
                (c >= "a" and c <= "z")
                or (c >= "A" and c <= "Z")
                or (c >= "0" and c <= "9")
                or (c == " ")
            ):
                return False
            i += 1
        return True

    def __str__(self):
        if self.available:
            status = "موجود"
        else:
            status = "امانت داده شده"

        return (
            "کتاب: " + self.title + " | نویسنده: " + self.author + " | وضعیت: " + status
        )

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value


class OverTheLimit(Exception):
    pass


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.__member_id = member_id
        self.borrowed_books = []
        self.__total_borrowed_book = 0

    def borrow_book(self, book):
        if book.available == True:
            if self.__total_borrowed_book < 5:
                book.borrow()
                self.__add_to_list(book)
                self.__total_borrowed_book += 1
                print(f"{self.name} borrowed the {book.title}")
            else:
                raise OverTheLimit("bish az hade mojaz")
        else:
            print("The book has been loaned.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            self.__total_borrowed_book -= 1
            print(f"{self.name} returned the {book.title} book")

    def __add_to_list(self, book):
        self.borrowed_books.append(book)

    def __str__(self):
        result = "member : " + self.name + "\nborrowed book : \n"
        for book in self.borrowed_books:
            result += " - " + book.title + "\n"
        return result

    @property
    def total_borrowed_book(self):
        return self.__total_borrowed_book

    @total_borrowed_book.setter
    def total_borrowed_book(self, value):
        self.__total_borrowed_book = value

    @property
    def member_id(self):
        return self.__member_id

    @member_id.setter
    def member_id(self, value):
        self.__member_id = value


class PremiumMember(Member):

    def __init__(self, name):
        super().__init__(name)
        self.__total_borrowed_book = 0

    def borrow_book(self, book):
        if book.available == True:
            if self.__total_borrowed_book < 5:
                book.borrow()
                self.__add_to_list(book)
                self.__total_borrowed_book += 1
            else:
                print("zarfiyat mojaz nist")
        else:
            print("ketab dar dastres nist")

    def __add_to_list(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            self.__total_borrowed_book -= 1
            print(f"{book.name} returned")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, isbn, member_id):
        print(f"User number {member_id} wants to borrow book number {isbn}.")
        int_isbn = None
        int_member_id = None
        try:
            int_isbn = int(isbn)
            int_member_id = int(member_id)
        except ValueError:
            print("The book isbn or member ID must be a valid number.")
            return

        target_member = None
        target_book = None

        for book in self.books:
            if book.isbn == int_isbn:
                target_book = book
                print(f"The book is available under number {isbn}.")
        for member in self.members:
            if member.member_id == int_member_id:
                target_member = member
                print(f"User has registered with number {member_id}")
        if target_member and target_book:
            target_member.borrow_book(target_book)
        if not target_member:
            print(f"user is not registered")
        if not target_book:
            print(f"The book is not available in the library list.")

    def return_book(self, isbn, member_id):
        print(f"Member with ID {member_id} wants to return book {isbn}.")

        int_isbn = None
        int_member_id = None

        try:
            int_isbn = int(isbn)
            int_member_id = int(member_id)
        except ValueError:
            print("The book isbn or member ID must be a valid number.")
            return

        target_member = None
        target_book = None

        for book in self.books:
            if book.isbn == int_isbn:
                target_book = book
                print(f"The book is available under number {isbn}.")
        for member in self.members:
            if member.member_id == int_member_id:
                target_member = member
                print(f"User has registered with number {member_id}")
        if target_member and target_book:
            target_member.return_book(target_book)
        if not target_member:
            print(f"user is not registered")
        if not target_book:
            print(f"The book is not available in the library list.")

    def list_available_books_show(self):
        result = "the book available : \n"
        for book in self.books:
            if book.available == True:
                result += " - " + book.title + "\n"
        return result


book1 = Book(title="python101", author="baba", isbn=4355)
book2 = Book(title="fizik", author="nioton", isbn=4356)
book3 = Book(title="ryazi", author="khayyam", isbn=4357)
book4 = Book(title="arabi", author="abolghasem", isbn=4358)
book5 = Book(title="shimi", author="dsa", isbn=4359)
book6 = Book(title="hendese", author="www", isbn=4360)
# book7 = Book()
# book8 = Book()
# book9 = Book()


member1 = Member(name="ali", member_id=1111)
member2 = Member(name="reza", member_id=1112)

l = Library(name="l")
l.add_book(book1)
l.add_book(book2)
l.add_book(book3)
l.add_book(book4)
l.add_book(book5)
l.add_book(book6)

l.register_member(member1)
l.register_member(member2)

l.borrow_book(isbn=4355, member_id=1111)
l.borrow_book(isbn=4356, member_id=1111)
l.borrow_book(isbn=4357, member_id=1111)
l.borrow_book(isbn=4358, member_id=1111)
l.borrow_book(isbn=4359, member_id=1111)
l.borrow_book(isbn=4360, member_id=1111)

# l.borrow_book(isbn=4355,member_id=1112)
# l.return_book(isbn=4355,member_id=1111)
# l.borrow_book(isbn=4355,member_id=1112)
