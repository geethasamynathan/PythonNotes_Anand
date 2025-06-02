from abc import ABC, abstractmethod

class Father(ABC):
	@abstractmethod
	def disp1(self):
		pass
	@abstractmethod
	def disp2(self):
		pass

class Child(Father):
	def disp1(self):
		print("Child Class")
		print("Disp 1 Abstract Method")	


class GrandChild(Child):
    def disp2(self):
        print('Grandchild Class')		
        print("defined in Grandchild")		
		
gc = Granchild()
#gc=Child()
gc.disp1()
gc.disp2()
		