class User:
    """Crash Course page 162"""
    def __init__(self, first, last, id, gender, level):
        self.first_name = first
        self.last_name = last 
        self.user_id = id
        self.sex = gender
        self.student_level = level
    
    def describe_user(self):
        for attribute, value in self.__dict__.items():
            print(f"{attribute} : {value}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

# CrashCourse p173, ex9.8
class Privileges:
    def __init__(self, privs= "default"):
        self.privileges = privs
    
    def show_privileges(self):
        print(f"Current privileges: {self.privileges}")
    
    def update_privileges(self,privs):
        self.privileges=privs
    
            
#Crash Course p173 9-8
class Admin(User):
    def __init__(self,first,last,id,gender,level):
        self.first_name = first
        self.last_name = last 
        self.user_id = id
        self.sex = gender
        self.student_level = level
                
        # super.__init__()
        self.privileges = Privileges()
    
       
    
        
