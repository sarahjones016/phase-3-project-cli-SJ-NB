class Fan:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

def create_new_fan():
    print("Let's get started!")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    new_fan = Fan(first_name, last_name)
    return f"Hey {new_fan.first_name} {new_fan.last_name}! We'll ask you some quick questions to help you find a new genre"