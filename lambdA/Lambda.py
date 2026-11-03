from functools import reduce


# nums = [2,3,4,5,6,7,8,9,10]
# evens = list(filter(lambda n : n%2 == 0 , nums))
# print(evens)

# # odds = list(filter(lambda n :n%2 != 0,nums))
# # print(odds)
# doubles = list(map(lambda n :n*2 ,evens))
# print(doubles)

# sum = reduce(lambda a,b :a+b ,doubles)
# print(sum)










# numbers = [1, 2, 3, 4, 5]

# def square(x):
#     return x * x

# result = list(map(square, numbers))

# print(result)


# numbs = [1,2,3,4,5,6,7,8,9,10]
# result = reduce(lambda x,y : x + y ,map(lambda x:x*10,filter(lambda x :x%2 == 0 ,numbs)))
# print(result)













# prime 2,3,5,7,11

# a=100

# b=[]
# for i in range(2,a+1):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False 

#     if is_prime:
#         b.append(i)
# print(b)






