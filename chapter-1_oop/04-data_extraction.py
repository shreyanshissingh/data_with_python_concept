import pandas as pd
import json

class MyDataExtractionClass:
    def __init__(self,file_path:str):     # dunder methods - when we use "__str__" or "__init__"
        self.file_path = file_path

    def f_extraction_json(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        df = pd.json_normalize(data)
        print(df.to_string())

    def f_extraction_csv(self):
        df = pd.read_csv(self.file_path)
        print(df.head())

obj = MyDataExtractionClass(file_path="/Users/shreyanshsingh/Documents/PersonalProjects/data_with_python_concept/chapter-1_oop/files/simulated_data.json")
obj.f_extraction_json()