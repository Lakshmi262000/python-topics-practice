# single inheritance

# class Parent():
#     # a=10 # variable or arugments in class
#     def parentMethod(self):
#         print("Iam Parent Class")


# class Child(Parent):
#     def childMethod(self):
#         print("Iam Child Class")

# obj1=Parent()
# obj2=Child()
# obj2.parentMethod()
# obj2.childMethod()
# ------------------practice------------------
# class nanna():
#     def function1(self):
#         print("I am nanna method")

# class pillar(nanna):
#     def function2(self):
#         print("I am pillar method")
# obj1 = nanna()
# obj2 = pillar()
# obj2.function1()
# obj2.function2()








# Multiple Inheritance


# class Father():
#     def fatherMethod(self):
#         print("I am Father class")


# class Mother():
#     def motherMethod(self):
#         print("Iam Mother class")

# class Child(Father,Mother):
#     def childMethod(self):
#         print("Iam child Class")

# obj1 = Child()

# obj1.fatherMethod()
# obj1.motherMethod()
# obj1.childMethod()

# --------------practice-----------------------------------
# class amma():
#     def method1(self):
#         print("i am amma method")
# class nanna():
#     def method2(self):
#         print("i am nanna method")
# class pillar(amma,nanna):
#     def method3(self):
#         print("i am pillar method")
    
# obj1 = amma()
# obj2 = nanna()
# obj3 = pillar()
# obj3.method1()
# obj3.method2()
# obj3.method3()











# Mutilevel Inheritance


# class GrandFather():
#     def grand_method(self):
#         print('I am Grandfather Class')


# class Father(GrandFather):
#     def father_method(self):
#         print('I am Father Class')


# class Child(Father):
#     def child_method(self):
#         print('Iam child class')

# class SubChild(Child):
#     def sub_child_method(self):
#         print('Iam Sub Class Method')



# obj1=Child()

# obj1.grand_method()
# obj1.father_method()
# obj1.child_method()

# print("--"*50)
# obj2=SubChild()
# obj2.grand_method()
# obj2.father_method()
# obj2.child_method()
# obj2.sub_child_method()



# ----------------------practice--------------------------------
# class thatha():
#     def method1(self):
#         print("i am thatha method")
# class amma(thatha):
#     def method2(self):
#         print("i am amma method")
# class bidda(amma):
#     def method3(self):
#         print("i am bidda method")
# class chinna(bidda):
#     def method4(self):
#         print("i am chinna method")

# obj1 = chinna()
# obj1.method1()
# obj1.method2()
# obj1.method3()
# obj1.method4()




# Hirarchial Inheritance

# class Parent():
#     def parent_method(self):
#         print("Iam Parent Class")


# class Child1(Parent):
#     def child1_method(self):
#         print("Iam Child 1 class")


# class Child2(Parent):
#     def child2_method(self):
#         print("Iam Child 2 class")


# print("--------- Child 1 Class ---------")
# obj1= Child1()
# obj1.parent_method()

# print("--------- Child 2 Class ---------")
# obj2= Child2()
# obj2.parent_method()




