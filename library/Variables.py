import json
class variables:
    def __init__(self,variable_name):
        self.path= "D:\DWBI\config\config.cfg"
        self.name= variable_name

    def get_variable(self):
        with open(self.path,"r") as file:
            file_content=json.loads(file.read())
            return file_content[self.name]

var=variables("DATABASE_NAME")
print(var.get_variable())

