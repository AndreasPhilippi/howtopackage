

class Chair:
    """Create a chair

        Parameters
        ----------
        chair_name : str
            The name of the chair
        professor: str
            The name of the professor
        employees : {array-like of shape (n,), []}, default=[]
            List of all employees of the chair

        See Also
        --------
        Employee

        Notes
        -----
        Here you can add some notes

        References
        ----------
        .. [1] Add references here

        Examples
        --------
        >>> from MyPackage.base import Employee, Chair
        >>> andreas = Employee("Andreas","100")
        >>> bwl11 = Chair("BWL11", "Richard", [andreas])
        >>> bwl11.displayEmployees()
        >>> niko = Employee("Niko",300)
        >>> bwl11.hire_employee(niko)
        >>> bwl11.displayEmployees()
        """

    def __init__(self,
                 chair_name,
                 professor,
                 employees=[]):
        self.chair_name = chair_name
        self.professor = professor
        self.employees = employees

    def fire_employee(self, employee):
        """Fire employee

            Parameters:
            -----------
            employee: employee
                The employee to fire
        """
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("There is not such a employee ")

    def hire_employee(self, employee):
        """Hire employee

            Parameters:
            -----------
            employee: employee
                The employee to hire
        """
        self.employees.append(employee)

    def displayEmployees(self):
        """Display all employees"""
        for employee in self.employees:
            employee.displayEmployee()


class Employee:
    """Create a chair

        Parameters
        ----------
        name : str
            The name of the employee
        salary: int
            The salary of the employee

        See Also
        --------
        Chair

        Notes
        -----
        Here you can add some notes

        References
        ----------
        .. [1] Add references here

        Examples
        --------
        >>> from MyPackage.base import Employee
        >>> andreas = Employee("Andreas","100")
        >>> andreas.displayEmployee()
        """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        """Display employee"""
        print("Name : ", self.name, ", Salary: ", self.salary)



