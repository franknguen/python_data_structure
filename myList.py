# create an empty list
my_list = []

print("MY list is created and updating:")
# add elements into list
my_list.append(00)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# access elements in list
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

# modify element in list
my_list[2] = 22
print(my_list[2])

# remove element from list
my_list.remove(30)

# check if 40 in my_list
if 40 in my_list:
    print("40 exists in my_list.")

# get the length of list
length = len(my_list)
print("Length of my list is: ", length)

# iteration the list
print("current my list:")
for item in my_list:
    print(item)

# sort my list
my_list.sort()
print("after sort:")
# iteration the list
for item in my_list:
    print(item)

# reverse my list
my_list.reverse()
print("after reverse:")
# iteration the list
for item in my_list:
    print(item)

# Clear all elements from the list
my_list.clear()

print("after clear:")
# Check if the list is empty
if not my_list:
    print("The list is empty")


