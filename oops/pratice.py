
# --------explaination----------


# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"My Name is {self.name} and my age is {self.age}")

#     def show(self):
#         print(f" {self.name}{self.age}")


# obj1=Student('Lucky',26)
# # print(obj1)

# obj1.show()


# ----------------------practice-----------------

# class teacher():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"my name is {self.name},my age is {self.age}")

#     def subject(self):
#         print(f"{self.name},{self.age}")

# obja = teacher("kannalu",26)
# # print(obja)
# obja.subject()












# class TTT():
#     def student(self,name,batch):
#         self.name = name
#         self.batch = batch
#         print(f"my name is {self.name} from batch {self.batch}")

#     def employee(self,month,year):
#         self.month = month
#         self.year = year
#         print(f"i joined on {self.month}th month of {self.year}")

#     def HR(self,name,year):
#         self.name = name
#         self.year = year
#         print(f"i am {self.name} wroking as HR,joined on {self.year}")

# obj1 = TTT()
# obj1.student("kushulu",25)
# obj1.employee(8,2026)
# obj1.HR("kuchulu",2026)



# class Mobile:
#     def __init__(self, model, camera):
#         self.model = model        
#         self.camera= camera
#     def make_call(self,number):        
#         print("calling..{}".format(number)) 
# mobile_obj = Mobile("iPhone 12 Pro", "12 MP") 
# mobile_obj.make_call(9876543210)


    





    
    
    
        
        
        





class override():
    def method1(self,name):
        return f"my name is {name} "

    def method1(self,name):
            return f"my  is {name} "



obj1=override()
# obj1.method1('kushi')
print(obj1.method1('kushi'))
# print(obj1.method1)
