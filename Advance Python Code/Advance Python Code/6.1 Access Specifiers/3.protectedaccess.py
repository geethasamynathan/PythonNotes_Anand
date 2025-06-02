class ProtectedExample:
    def __init__(self,age):
        self._age=age
    
    def _display(self):
        print(f'Age : {self._age}')
        
class SubClass(ProtectedExample):
    def show(self):
        print(f' Accessing protected {self._age} ')
        self._display()

subclass=SubClass(34)
print(f'accessing age from protected variable {subclass._age}')
subclass._display();

protectedExample=ProtectedExample(45)
print(f'Age from base through base class obj {protectedExample._age}')