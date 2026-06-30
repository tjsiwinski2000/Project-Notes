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
        
test_user = User("TJ", "Siwinski", "00001", "male", "freshman")
test_user.describe_user()