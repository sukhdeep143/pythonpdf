class Employee:
    def __init__(self):  # Constructor
        self.__id = 0
        self.__name = ""
        self.__gender = ""
        self.__city = ""
        self.__salary = 0
        print("Object Initialized.")

    # def __del__(self):  # Destructor
    #     print("Object Destroyed.")

    def setData(self):
        self.__id = int(input("Enter Id\t:"))
        self.__name = input("Enter Name\t:")
        self.__gender = input("Enter Gender:")
        self.__city = input("Enter City\t:")
        self.__salary = int(input("Enter Salary:"))

    def showData(self):
        print("Id\t\t:", self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)


def main():
    # Employee Object
    emp = Employee()
    emp.setData()
    mani = Employee()
    mani.setData()
    emp.showData()
    mani.showData()



if __name__ == "__main__":
    main()
