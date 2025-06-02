from abc import ABC,abstractmethod

class interface1(ABC):
    @abstractmethod
    def show1():
        pass

class interface2(ABC):
    @abstractmethod
    def show2():
        pass

class DerivedClass(interface1,interface2):
    def show1(self):
        print('Show method of an interface1 invoked')
    def show2(self):
        print('Show method of an interface2 invoked')


derivedclass=DerivedClass()
derivedclass.show1()
derivedclass.show2()
