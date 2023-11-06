
my_dict = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}

# Rekipere kle yo
keys = list(my_dict.keys())

# Rekipere valè yo
values = list(my_dict.values())

# Retounen yon lis valè
print(keys)
print(values)


input_val = input("Tape yon valè: ")
if input_val.startswith('{') and input_val.endswith('}'):
    print("Valè a gen akolad devan ak dèyè.")
else:
    print("Valè a pa gen akolad devan ak dèyè.")




my_dict = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}

# Afiche tout kle yo
for key in my_dict:
    print(key)



my_dict = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}

# Afiche tout valè yo
for value in my_dict.values():
    print(value)



my_dict = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
new_dict = my_dict.copy()
print(new_dict)

my_dict = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
for key, value in my_dict.items():
    if isinstance(value, str):
        my_dict[key] = "_" + value + "_"
print(my_dict)



my_dict = {"a": "12", "b": "abc", "c": "12r", "d": "90"}
new_dict = {key: value for key, value in my_dict.items() if value.isdigit()}
print(new_dict)


my_list = [("a", 1), ("b", 2)]
my_dict = dict(my_list)
print(my_dict)



my_list = [("a", 1), ("b", 2)]
my_dict = dict(my_list)
print(my_dict)



dict1 = {"a": 1, "b": 2, "c": [3, 4]}
dict2 = {"a": 10, "b": 20, "c": [30, 40]}

result_dict = {}

for key in dict1:
    if isinstance(dict1[key], int):
        result_dict[key] = dict1[key] + dict2[key]
    elif isinstance(dict1[key], (str, list, set)):
        result_dict[key] = dict1[key] + dict2[key]

print(result_dict)












