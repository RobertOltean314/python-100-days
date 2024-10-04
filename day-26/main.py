numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [number + 1 for number in numbers]
print(new_list)

names = ["Angela," "Robert", "Aurel"]
letter_from_names = [letter for name in names if len(name) > 5 for letter in name]
print(letter_from_names)
