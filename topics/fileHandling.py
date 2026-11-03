# w overwrite with new data
# with open("data.txt", "w") as file:
#     file.write("Hello Python ")




# with open("data.txt", "w") as file:
#     file.write("Hello Python hi hello")



# a append data to file

# with open("data.txt", "a") as file:
#     file.write("\n Append data")



# x create a new file


# with open("newfile.txt", "x") as file:
#     file.write("Hello")



# r read file

# with open("newfile.txt", "r") as file:
#     data=file.read()
# print(data)


# readline()  Reads one line.

# with open("data.txt", "r") as file:
#     line1 = file.readline()
#     line2 = file.readline()

#     print(line1)
#     print(line2)




# readlines() Reads all lines and returns a list.

# with open("data.txt", "r") as file:
#     lines = file.readlines()

# print(lines)




# writelines() Used to write multiple strings.


# data = [
#     "Python\n",
#     "SQL\n",
#     "Spark\n"
# ]

# with open('data1.txt','w') as file:
#     file.writelines(data)



# File Pointer
# tell() tells you the current file-pointer position.
# seek() moves the file pointer.



# with open('employee.csv','r') as file:
#     print(file.read(7))
#     file.seek(1) # start from first index 
#     print(file.read(5)) # end index




# csv fomart
import csv

with open("employee.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)