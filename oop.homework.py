class Book:

    def __init__(self, title, author):
        if Book.is_valid_title(title):
            self.title = title
        else:
            self.title = "is not valid title"
        self.author = author
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


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
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

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            self.__total_borrowed_book -= 1
            print(f"{book.title} returned")

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


book1 = Book("reyazi", "kharazmi")
book2 = Book("fizik", "neyoton")
book3 = Book("tarikh", "tabari")
book4 = Book("farsi", "parvin")


m1 = Member("ali ahmadi")
m2 = Member("reza rezaii")
vm3 = PremiumMember("nima")
vm4 = PremiumMember("sara")


m1.borrow_book(book1)
m1.borrow_book(book2)
vm3.borrow_book(book3)
vm3.borrow_book(book4)

print(f"{m1} \n {m2} \n {vm3} \n {vm4}")


m1.return_book(book2)
vm4.borrow_book(book2)
print(m1)
