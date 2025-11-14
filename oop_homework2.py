import logging

logging.basicConfig(
    filename="library.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class Book:
    logging.info("start project")
    World_book_list = []

    def __init__(self, title, author, isbn):
        if not Book.is_valid_title(title):
            raise ValueError("namotabar")
        self.title = title

        try:
            valid_isbn = int(isbn)
            logging.debug("the isbn book is valid")
        except ValueError:
            logging.error("the isbn book is not valid")
            print("Enter valid numeric values ​​for the book ID.")
            return
        self.__isbn = valid_isbn
        self.author = author
        self.available = True
        Book.World_book_list.append(self)
        logging.debug(f"add the {self.title} book")

    def borrow(self):
        if self.available:
            self.__mark_borrowed()
            logging.debug(f"the {self.title} book borrowed")
        else:
            logging.debug(f"the {self.title} book is not available")

    def return_book(self):
        self.available = True
        logging.debug(f"the {self.title} book returned")

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
        logging.debug(f"The string {title} was valid.")
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


class IsNotValidName(Exception):
    pass


class Member:
    world_member_list = []

    def __init__(self, name, member_id):
        if not Book.is_valid_title(name):
            logging.error("the user name is not valid")
            raise IsNotValidName("Please enter the correct values.")
        self.name = name
        try:
            valid_member_id = int(member_id)
            logging.debug("the member id is valid")
        except ValueError:
            logging.error("the member id is not valid")
            print("Please enter the correct values.")
            return
        self.__member_id = valid_member_id
        self.borrowed_books = []
        self.__total_borrowed_book = 0
        Member.world_member_list.append(self)
        logging.debug(f"user {self.name} added")

    def borrow_book(self, book):
        if book.available:
            logging.debug(f"the {book.title} is available")
            if self.__total_borrowed_book < 3:
                book.borrow()
                self.__add_to_list(book)
                self.__total_borrowed_book += 1
                logging.debug(f"{self.name} borrowed the {book.title}")
                logging.debug(
                    f"Number of books borrowed by {self.name} : {self.__total_borrowed_book}"
                )
                if self.__total_borrowed_book == 2:
                    logging.warning(
                        f"User {self.name} cannot borrow more than one book."
                    )
            else:
                logging.error(
                    f"The number of books borrowed by user {self.name} exceeds the allowed limit."
                )
                print("You can borrow another book by returning one book.")
                raise OverTheLimit(
                    f"The number of books borrowed by user {self.name} exceeds the allowed limit."
                )
        else:
            logging.warning(
                f"The book {book.title} that user {self.name} wanted had been loaned to someone else."
            )

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            self.__total_borrowed_book -= 1
            logging.debug(f"{self.name} returned the {book.title} book")
            logging.debug(
                f"Number of books borrowed by {self.name} : {self.__total_borrowed_book}"
            )
        else:
            print("The book is not in the user's list of borrowed books.")
            logging.warning(
                f"{self.name} tried to return a book that was not borrowed."
            )

    def __add_to_list(self, book):
        self.borrowed_books.append(book)
        logging.debug(f"{book.title} book added to user {self.name}'s list")

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

    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.__total_borrowed_book = 0

    def borrow_book(self, book):
        if book.available:
            logging.debug(f"the {book.title} is available")
            if self.__total_borrowed_book < 5:
                book.borrow()
                self.__add_to_list(book)
                self.__total_borrowed_book += 1
                logging.debug(f"{self.name} borrowed the {book.title}")
                logging.debug(
                    f"Number of books borrowed by {self.name} : {self.__total_borrowed_book}"
                )
                if self.__total_borrowed_book == 4:
                    logging.warning(
                        f"User {self.name} cannot borrow more than one book."
                    )
            else:
                logging.error(
                    f"The number of books borrowed by user {self.name} exceeds the allowed limit."
                )
                print("You can borrow another book by returning one book.")
                raise OverTheLimit(
                    f"The number of books borrowed by user {self.name} exceeds the allowed limit."
                )
        else:
            logging.warning(
                f"The book {book.title} that user {self.name} wanted had been loaned to someone else."
            )

    def __add_to_list(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            self.__total_borrowed_book -= 1
            logging.debug(f"{self.name} returned the {book.title} book")
        else:
            print("The book is not in the user's list of borrowed books.")
            logging.warning(
                f"{self.name} tried to return a book that was not borrowed."
            )


class NonExistence(Exception):
    pass


class Library:
    def __init__(self, name):
        logging.info(f"Library {name} created")
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book=None):
        if book in Book.World_book_list:
            if book not in self.books:
                self.books.append(book)
                logging.debug(f"{book.title} books donated to the library")
            else:
                logging.warning(f"The library already has the {book.tiltle} book.")
        else:
            logging.warning(
                f"The library did not accept the {book} book due to its non-existence."
            )
            print(
                f"The library did not accept the {book} book due to its non-existence."
            )

    def register_member(self, member=None):
        if member in Member.world_member_list:
            if member not in self.members:
                self.members.append(member)
                logging.debug(f"User {member.name} registered.")
            else:
                logging.warning(f"The user {member.name} is already registered.")
                print(f"User {member.name} failed to register.")
        else:
            logging.warning(f"User {member} not found")
            print(f"user {member} not found")

    def borrow_book(self, isbn, member_id):
        logging.debug(
            f"User by id number {member_id} wants to borrow book number {isbn}."
        )
        int_isbn = None
        int_member_id = None
        try:
            int_isbn = int(isbn)
            int_member_id = int(member_id)
        except ValueError:
            logging.error("The user entered incorrect numeric identifiers.")
            print("Please enter the correct values.")
            return

        target_member = None
        target_book = None

        for book in self.books:
            if book.isbn == int_isbn:
                target_book = book
                logging.debug(f"The book number {isbn} is available in the library.")
        for member in self.members:
            if member.member_id == int_member_id:
                target_member = member
                logging.debug(f"User has registered with number {member_id}")
        if target_member and target_book:
            target_member.borrow_book(target_book)
        if not target_member:
            logging.warning("user is not registered")
        if not target_book:
            logging.warning("The book is not available in the library list.")

    def return_book(self, isbn, member_id):
        logging.debug(f"Member with ID {member_id} wants to return book {isbn}.")

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
                logging.debug(f"The book is available under number {isbn}.")
        for member in self.members:
            if member.member_id == int_member_id:
                target_member = member
                logging.debug(f"User has registered with number {member_id}")
        if target_member and target_book:
            target_member.return_book(target_book)
        if not target_member:
            logging.warning(f"user {member_id} is not registered")
        if not target_book:
            logging.warning(f"The book {isbn} is not available in the library list.")

    def list_available_books_show(self):
        result = "the book available : \n"
        for book in self.books:
            if book.available:
                result += " - " + book.title + "\n"
        return result


book1 = Book(title="python101", author="baba", isbn=4355)
book2 = Book(title="fizik", author="nioton", isbn=4356)
book3 = Book(title="ryazi", author="khayyam", isbn=4357)
book4 = Book(title="arabi", author="abolghasem", isbn=4358)
book5 = Book(title="shimi", author="dsa", isbn=4359)
book6 = Book(title="hendese", author="www", isbn=4360)

member1 = Member(name="ali", member_id="1111")
member2 = Member(name="reza", member_id="1112")
member3 = Member(name="javad", member_id=1113)
member4 = Member(name="mamad", member_id=1114)
member5 = Member(name="asghar", member_id=1115)
member6 = Member(name="nima", member_id=1116)
member7 = Member(name="baran", member_id=1117)

library = Library(name="library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)

library.register_member(member1)
library.register_member(member2)

library.borrow_book(isbn=4355, member_id=1111)
library.borrow_book(isbn=4355, member_id=1112)
library.return_book(isbn=4355, member_id=1111)
library.borrow_book(isbn=4355, member_id=1111)
print(library.list_available_books_show())
