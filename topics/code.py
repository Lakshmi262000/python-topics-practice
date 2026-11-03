# # counter 
# counter = 0

# for i in range(1, 6):
#     counter += 1

# print(counter)




# acumulators


# counter = 0

# for i in range(1, 6):
#     counter += i

# print(counter)


# numbers = [10, 20, 30, 40, 50]

# total = 0

# for num in numbers:
#     total += num

# print(total)








salaries = [25000, 30000, 40000, 50000]

total = 0
count = 0

for salary in salaries:
    total += salary
    count += 1
print(f"total: {total}, count: {count}")
average = total / count

print(average)