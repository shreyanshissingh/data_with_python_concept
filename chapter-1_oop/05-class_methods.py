class MyClassMethods:
    c_var = "Old Value"

    @classmethod
    def _func1(cls,new_val):    #classmethods should always be Protected Methods (start with "_"), it is naming convention for all classmethods
        cls.c_var = new_val
        return cls.c_var
    
    @staticmethod               #staticmethods  
    def dummy_func():
        print("Dummy")
        

obj = MyClassMethods()
old = obj.c_var
obj.c_var = "New Val"
new = obj.c_var

# print(f"Earlier what was {old}, now became :{new}")

obj_1  = MyClassMethods()
old_1 = obj_1.c_var 

# print(f"Earlier what was {old}, now became :{new}. Still when we create obj_1 , we can see value as {old_1}")

obj_2 = MyClassMethods()
new_1 = obj_2._func1("NV")

print(f"Value in obj earlier : {old}, now became :{new}. Value in obj_1 : {old_1}. Value in obj_2 : {new_1}")
print(f"Value overall has now become c_var = {MyClassMethods.c_var}")

obj_3 = MyClassMethods()
print(f"obj_3 = {obj_3.c_var}")

obj_4 = MyClassMethods()
obj_4.dummy_func()