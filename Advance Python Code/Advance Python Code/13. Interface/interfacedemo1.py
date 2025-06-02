from abc import ABC,abstractmethod

class Security(ABC):
    
    @abstractmethod
    def place_applied():
        pass
    
    @abstractmethod
    def material_used():
        pass
       #print('Just to test without @abstractmethod')
    
#security=Security()
#security.material_used()
class Police(Security):
    
    def place_applied(self):
        print('local Municipal')    

    def material_used(self):
        print('Announcing about protet reg some activity')
        
class Navy(Security):
    def visit(self):
        print('Just to check the borderlines')
    def place_applied(self):
        print('coastal line')    

    def material_used(self):
        print('Announcing about crossing the border')
    
def main():
    police1=Police()
    police1.place_applied() 
    police1.material_used()
    
    # navy1=Navy()
    # navy1.place_applied()
    # navy1.material_used()
    # navy1.visit()   
    
main()