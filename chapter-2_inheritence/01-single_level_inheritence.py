class Company:
    title:str = "Data Engineer"

    def __init__(self,company_name:str , company_loc:str):
        self.company_name = company_name
        self.loc = company_loc

    def info(self):
        print(f"Company Location Info : {self.loc}")
        return self.loc
    

class Employee(Company):

    def __init__(self,employee_name,company_name,loc):  #Dunder functions get called automatically and creates "self"
        self.employee_name = employee_name
        self.company_name = company_name
        self.loc = loc
        

    def emp_info(self):
        response = Company.info(self)
        title = Company.title
        print(f"Emp Info: {self.employee_name} , company name: {self.company_name} , company loc: {response}, title:{title}")


emp_obj = Employee(company_name="SS Inc",employee_name="SS",loc="UP")
emp_obj.emp_info()