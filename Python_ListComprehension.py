# I am using list comprehenion to add a value of 1 to each integer in the old list, and storing the result in a new list. #
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [list + 1 for list in old_list]

print(f"This is the old list: {old_list}")

print(f"This is the new list: {new_list}")

