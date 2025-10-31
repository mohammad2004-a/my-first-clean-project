class Book:
    def __init__(self, title, author):
        # بررسی عنوان معتبر
        if Book.is_valid_title(title):
            self.title = title
        else:
            self.title = "نامعتبر"
        self.author = author
        self.available = True

    def borrow(self):
        # اگر کتاب در دسترس بود، وضعیت را تغییر بده
        if self.available:
            self.__mark_borrowed()

    def return_book(self):
        # وضعیت را به در دسترس تغییر بده
        # (تکمیل شود)
        pass

    def __mark_borrowed(self):
        # وضعیت را به امانت داده شده تغییر بده
        # (تکمیل شود)
        pass

    @staticmethod
    def is_valid_title(title):
        # بررسی کند که فقط شامل حروف، اعداد یا فاصله باشد
        # (تکمیل شود)
        pass

    def __str__(self):
        if self.available:
            status = "موجود"
        else:
            status = "امانت داده شده"
        return "کتاب: " + self.title + " | نویسنده: " + self.author + " | وضعیت: " + status


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        # اگر تعداد کتاب‌ها کمتر از ۳ بود و کتاب در دسترس بود:
        # کتاب را امانت بگیر و به لیست اضافه کن
        # (تکمیل شود)
        pass

    def return_book(self, book):
        # کتاب را در لیست پیدا کن و حذف کن
        # وضعیت آن را برگردان
        # (تکمیل شود)
        pass

    def __add_to_list(self, book):
        # کتاب را به borrowed_books اضافه کن
        # (تکمیل شود)
        pass

    def __str__(self):
        result = "عضو: " + self.name + "\nکتاب‌های امانتی:\n"
        i = 0
        while i < len(self.borrowed_books):
            result += " - " + self.borrowed_books[i].title + "\n"
            i += 1
        return result


class PremiumMember(Member):
    def borrow_book(self, book):
        # همانند کلاس Member، فقط به جای ۳، تا ۵ کتاب مجاز است
        # (تکمیل شود)
        pass
