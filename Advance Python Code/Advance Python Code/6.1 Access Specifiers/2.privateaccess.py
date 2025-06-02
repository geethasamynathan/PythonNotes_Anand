class PrivateExample:
    def __init__(self, salary):
        self.__salary = salary  # Private variable

    def __display(self):  # Private method
        print("Salary:", self.__salary)

    def access_private(self):
        self.__display()  # ✅ Allowed inside class

# Accessing private members
obj = PrivateExample(50000)

# Direct access (❌ Not allowed)
# print(obj.__salary)  # AttributeError

# # Name mangling (✅ Allowed)
# print(obj._PrivateExample__salary)  # Works, but not recommended

# Private method call (❌ Not allowed)
# obj.__display()  # AttributeError

# Private method accessed via another method (✅ Allowed)
obj.access_private()