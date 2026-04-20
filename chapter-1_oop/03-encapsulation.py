class MyEncapsulatedClass:
    
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1 = dyn1 #Public Variable
        self.__dyn2 = dyn2 #Private Variable
        self._dyn3 = dyn3 

    def func1(self):
        print(f"Can change dyn1 , see : {self.dyn1}")

    def func2(self):
        print(f"Can't change dyn2 , see : {self.__dyn2}")
        return self.__dyn2

    def func3(self):
        print(f"Can't change dyn2 , see : {self._dyn3}")

obj = MyEncapsulatedClass(dyn1="Dynamic1",dyn2="Dynamic2",dyn3="Dynamic3")
obj.dyn1="D1"
obj.dyn2="D2"
obj.func1()
new_val = obj.func2()
print(f"Printing dyn2 as variable will show changed value:{obj.dyn2},as it is not the same dyn2 as needed by func2(), but not via function:{new_val}")
print(f"Protected variable can be accessed , unlike __dyn2 , see : {obj._dyn3} ")
