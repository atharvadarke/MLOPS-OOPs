class Employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = 'SDE'

    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

# create an object for the class employee 
sam = Employee()
# print(sam.salary)

'''A function within a class is called as a method'''
# calling a method
# sam.travel('New York City')

print(type(sam))