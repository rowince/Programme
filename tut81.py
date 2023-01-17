# Convert List to List of dictionaries
# input- [‘Gfg’, 3, ‘is’, 8, ‘Best’, 10, ‘for’, 18, ‘Geeks’, 33]
# key_list = ["name", "number"]
# [{‘name’: ‘Gfg’, ‘number’: 3}, {‘name’: ‘is’, ‘number’: 8}, {‘name’: ‘Best’, ‘number’: 10}, {‘name’: ‘for’, ‘number’: 18}, {‘name’: ‘Geeks’, ‘number’: 33}]

arr = ['Gfg', 3, 'is', 8, 'Best', 10, 'for', 18, 'Geeks', 33]
key_list = ["name", "number"]

def convert_list_dict(arr, key):
    temp = []
    for i in range(len(arr)):
        temp_dict = {}
        if i % 2 == 0:
            temp_dict[key[i%2]] = arr[i]
            temp_dict[key[i%2+1]] = arr[i+1]
        if len(temp_dict) > 0:
            temp.append(temp_dict)
    print(temp)
convert_list_dict(arr, key_list)

        
