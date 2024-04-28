class Box:
    def __init__(self,name,rollnumber,dbmsmarks,pythonmarks,cmarks,osmarks,cnmarks):
        self.name=name
        self.rollnumber=rollnumber
        self.dbmsmarks=dbmsmarks
        self.pythonmarks=pythonmarks
        self.cmarks=cmarks
        self.osmarks=osmarks
        self.cnmarks=cnmarks
        
student1 = Box("Harika","5A1",78,67,77,89,46)
student2 = Box("Swapna","5A2",38,65,97,59,41)
student3 = Box("Sushma","5A3",88,95,47,89,31)

print(student1.name,
student1.rollnumber,
student1.dbmsmarks,
student1.pythonmarks,
student1.cmarks,
student1.osmarks,
student1.cnmarks,
end='\n')      
print(student2.name,
student2.rollnumber,
student2.dbmsmarks,
student2.pythonmarks,
student2.cmarks,
student2.osmarks,
student2.cnmarks,
end='\n')
print(student3.name,
student3.rollnumber,
student3.dbmsmarks,
student3.pythonmarks,
student3.cmarks,
student3.osmarks,
student3.cnmarks,
end='\n')      
