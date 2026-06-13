# lists

student_names = ["Sachin", "Akshay", "Nishant"]
print(student_names)

# Printing type
print(type(student_names))

# Appending elements to list
student_names.append("Bibtya")
print(student_names)

# Removing elements from list
student_names.remove("Bibtya")
print(student_names)

# Printing specific elements -> List of 0. Brackets are also called as "of"
print(student_names[0])

# Printing specific elements -> List of 1
print(student_names[1])

# Printing length of the list
print(len(student_names))

# Sorting the list
numbers_list = [1, 5, 4, 3, 2, 5, 8]
numbers_list.sort()
print(f"Sorted list is: {numbers_list}")