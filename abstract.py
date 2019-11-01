# abstract class in python
from abc import ABC, abstractmethod
#abstract class
class Polygon(ABC):
    #abstract method
    def noofsides(self):
        pass
    
class Triangle(Polygon):
    #overridding abstract method
    def noofsides(self):
        print("3 sides")
        
T = Triangle()
T.noofsides()
