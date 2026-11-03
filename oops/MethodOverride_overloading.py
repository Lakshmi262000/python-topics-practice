# Method Override

# class Parent():
#     def method(self):
#         print("Iam Parent Class")


# class Child(Parent):
#     def method(self):
#         print("Iam Child Class")


# obj1= Child()
# obj1.method()




# ---------------practice----------------idi method over ride aitadi,, so ila cheyakuddadhu

# class furniture():
#     def chairs(self):
#         print("i am chair method of furniture class")

#  class home():
#     def chairs(self):
#         print("i am chair method of home class")

# obj1 = furniture()
# obj2 = home()
# print(obj1)
# print(obj2)




# class furniture():
#     def chairs(self):
#         print("i am chair method of furniture class")

# class home(furniture):
#     def chairs(self):
#         print("i am chair method of home class")


# obj2 = home()
# obj2.chairs()






# Method Overloading



# class Cal():
#     def add(self,a,b):
#         return a+b 

#     def add(self,a,b,c):
#         return a+b+c 


# obj1=Cal()
# print(obj1.add(1,2))
# print(obj1.add(1,2,3))



# correct way for overloading
# class Cal():
#     def add(self,*args):
#         return sum(args)

# obj1=Cal()
# print(obj1.add(1,2))
# print(obj1.add(1,2,3))
# print(obj1.add(1,2,3,4,5))










# ----------------polymorphism cheyyi nivve

