class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructer called")
def create_employee():
     print("creating employee")
     obj=employee()
     print("function end")
obj=create_employee()

