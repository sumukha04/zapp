class Employee:
    def __init__(self):
        self.name=name=""
        self.empId=""
        self.dept=""
        self.salary=""

        def getEmpDetails(self):
            self.name=input("Enter employee name: ")
            self.empid=input("Enter employee ID: ")
            self.dept=input("Enter the department: ")
            self.salary=input("Enter the salary: ")

            def showEmpDetails(self):
                print("Employee details")
                print("name", self.name)
                print("EmpID", self.empId)
                print("Department", self.dept)
                print("Salary", self.salary)

                def updateSalary(self):
                    self.salary=int(input("Enter new salary"))
                    print("Updated salary", self.salary)
                    e1=Employee()
                    e1=getEmpDetails()
                    e1=showEmpDetails()
                    e1=updateSalary()
