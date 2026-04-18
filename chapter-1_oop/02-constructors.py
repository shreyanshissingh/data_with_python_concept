class MyConsClass:
    c_var = "Class Variable"
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        
    def func1(self):
        print(f"Welcome to func1 : {self.var1}")
        

    def func2(self):
        print(f"Welcome to func2 : {self.var2}")
        print(f"Class Variable printing : {self.c_var}")


obj_1 = MyConsClass(var1= "variable 1",var2= "variable 2")
obj_1.func1()
obj_1.func2()
