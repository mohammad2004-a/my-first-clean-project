from abc import abstractmethod

from cryptocode import decrypt, encrypt


class person:

    @abstractmethod
    def get_total_person(self):
        pass

    @abstractmethod
    def register(self, email, password):
        pass

    @abstractmethod
    def __decrypt_password(self):
        pass

    @abstractmethod
    def change_password(self, oldpassword, newpassword, newpassword2):
        pass


class Student(person):

    total_person = 0

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age
        self.country = country
        Student.total_person += 1

    @staticmethod
    def get_total_person():
        return Student.total_person

    def register(self, email, password):
        self.email = email
        self.password = encrypt(password, "1234")

    def __str__(self):
        return f"{self.first_name} {self.last_name} welcom to website !"

    # @staticmethod
    def __decrypt_password(self) -> str:
        return decrypt(self.password, "1234")

    def change_password(self, oldpassword, newpassword, newpassword2):
        if oldpassword == self.__decrypt_password():
            if newpassword == newpassword2:
                self.password = encrypt(newpassword, "1234")
            else:
                print("error pass1")
        else:
            print("error password")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


p1 = Student("mohammad mahdi", "abedinzadeh", 22, "iran")
p1.register("mohammadmahdi13831388@gmail.com", "09906419973")
print(p1.password)
# print(p1.decrypt_password())
p1.change_password(
    oldpassword="09906419973", newpassword="099064199733", newpassword2="099064199733"
)
# print(p1.decrypt_password())
print(Student.get_total_person())
print(p1.age)
