# Iterator

# numbers = [10, 20, 30]

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# generator 

# def numbers():
#     yield 10
    

# result=numbers()
# print(result)
# print(next(result))




# def numbers():
#     print("Start")
#     yield 10

#     print("Middle")
#     yield 20

#     print("End")
#     yield 30

# g=numbers()
# print(next(g))
# print(next(g))




def numbers():
    for i in range(5):
        yield i


for x in numbers():
    print(x)


