# with open('student.txt','r') as file:
#     data=file.read()
# print(data)

# =============================================================

# try      → Try this code
# except   → If error happens, handle it
# else     → If no error, do this
# finally  → Do this no matter what
# raise    → Create an error yourself

# =============================================================




# try:
#     with open('student.txt','r') as file:
#         data=file.read()
#     print(data)

# except FileNotFoundError:
#     print("File Does not Exists")



# try:
#     a = 10
#     b = 0
#     print(a / b)

# except:
#     print("Something went wrong")



# Catching a Specific Exception
# try:
#     result = 10 / 0
#     print(result)

# except ZeroDivisionError:
#     print("Cannot divide by zero")




# try:
#     a = int(input("Enter number: "))
#     result = 10 / a


# except ValueError:
#     print("Please enter a number")

# except ZeroDivisionError:
#     print("Number cannot be zero")





# as e — See the Error Message
# result = 10 / 0
# print(result)
# print('-'*50)

# try:
#     result = 10 / 0

# except ZeroDivisionError as e:
#     print(e)





# try:
#     # risky code

# except SomeException:
#     # handle error

# else:
#     # runs if no error

# finally:
#     # always runs









# try:
#     number = int(input("Enter number: "))
#     result = 100 / number

# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)

# finally:
#     print("Program finished")














# raise Sometimes we want to create an exception ourselves.


# age = 15

# if age < 18:
#     raise ValueError("Age must be 18 or above")





# Exception Handling with Files
# try:
#     with open("employees.csv", "r") as file:
#         data = file.read()

# except FileNotFoundError:
#     print("employees.csv does not exist")