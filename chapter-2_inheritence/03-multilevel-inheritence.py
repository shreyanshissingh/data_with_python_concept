class Company:
    title:str = "Data Engineer"

    def __init__(self,company_name:str , company_loc:str):
        self.company_name = company_name
        self.loc = company_loc

    def info(self):
        print(f"Company Info : {self.company_name} , Lvl-1 :{self.loc}")
        return f"Company Info :{self.company_name} , Lvl-1 :{self.loc}"
    
class Manager(Company):
    def __init__(self,mgr_name:str, company_name:str, loc:str):
        self.mgr_name = mgr_name
        self.company_name = company_name
        self.loc = loc

    def info(self):
        response = Company.info(self)
        print(f"Manager Name : {self.mgr_name}, Lvl-2 : {response}")
        return f"Manager Name : {self.mgr_name} , Lvl-2 : {response}"


class Employee(Manager):
    def __init__(self,emp_name:str,mgr_name:str, company_name:str, loc:str):
        self.emp_name = emp_name
        self.mgr_name = mgr_name
        self.company_name = company_name
        self.loc = loc

    def info(self):
        response = Manager.info(self)
        print(f"Employee Name : {self.emp_name}, Lvl-3 : {response}")
        return f"Employee Name : {self.emp_name} , Lvl-3 : {response}"
    
emp_obj = Employee(emp_name="Shreyansh",mgr_name="Shrey",company_name="SS Inc",loc="IND")
emp_obj.info()