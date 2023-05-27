# create an empty dict
my_dict = {}

print("MY dict is created and updating:")
# add elements into dict
my_dict["name"] = "John"
my_dict["age"]  = 30
my_dict["city"] = "Yongin"

# access elements in dict
print(my_dict["name"])
print(my_dict["age"])

# modify element in dict
my_dict["age"] = 33

# remove element from dict
del my_dict["city"]

# check if name in my_dict
if "name" in my_dict:
    print("Name exists in my_dict.")

# get keys and values of dictionary
keys   = my_dict.keys()
values = my_dict.values()

# iteration the dict
print("current my dict:")
for key in my_dict:
    print(key, my_dict[key])

# get length of my dictionary
length = len(my_dict)
print("Length of my dict: ", length)

# Clear all elements from the dict
my_dict.clear()

print("after clear:")
# Check if the dict is empty
if not my_dict:
    print("The dict is empty")


