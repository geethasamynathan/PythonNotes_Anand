class PublicExample:
    def __init__(self, name):
        self.name = name  # Public variable

    def display(self):
        print("Name:", self.name)  # Public method
    
publicExample=PublicExample('CMR')
print(publicExample.name)
publicExample.display()