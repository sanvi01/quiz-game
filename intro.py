# #prompt_1
# class Student:
#
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grade: {self.grade}")
#
#
# stu_1 = Student("Sanvi", 19, "SY")
# stu_1.display()
#
#
# #prompt_2
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         a = self.length * self.width
#         print(f"Area of this rectangle is {a}.")
#
#     def perimeter(self):
#         p = 2 * (self.width + self.length)
#         print(f"Perimeter of this rectangle is {p}.")
#
#
# rect = Rectangle(5, 10)
# rect.area()
# rect.perimeter()


#prompt_3
class BankAccount:
    def __init__(self, account_number, holder_name):
        self.number = account_number
        self.name = holder_name
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} has been deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful!")
        else:
            print("Sorry, insufficient amount for withdrawal")

    def display_details(self):
        print(f"Account Number: {self.number}")
        print(f"Holder Name: {self.name}")
        print(f"Balance: {self.balance}")
        print("----")


holder1 = BankAccount(201032005, "Sanvi Verma")
holder1.display_details()
holder1.deposit(40000)
holder1.display_details()
holder1.withdraw(56450)
holder1.display_details()

