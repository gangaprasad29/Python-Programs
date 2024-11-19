# 1) Create a list of students attending STW-PDW

# i) Using initializer variable
list_1 = ['Gangaprasad', 'Anshul', 'Rushi']

# ii) Using a constructor
list_2 = list(('Gangaprasad', 'Anshul', 'Rushi'))

# 2) Add name of one lecturer in the list using:
# i) .insert() method in the middle of the list
list_1.insert(len(list_1)//2, 'Professor Sanjay')

# ii) .append() method
list_2.append('Professor Rathod')

# iii) Initializing the name to 3rd index
list_1[2] = 'Professor Kamble'

# 3) Convert the list in Q1. to tuple and perform operations:

# Convert list to tuple
students_tuple = tuple(list_1)

# i) Add a student’s name.
students_tuple += ('Prasad',)

# ii) Unpack the tuple using 2 variables.
student1, student2, *other_students = students_tuple

# 4) Use the same tuple as a set and:

# Convert tuple to set
students_set = set(students_tuple)

# i) Discard 1 item.
students_set.pop()

# ii) Empty the set and print it.
students_set.clear()
print(students_set)

# 5) Create 2 integer sets and perform:

# Create integer sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# i) Union of the sets.
union_set = set1.union(set2)

# ii) Intersection update of the sets.
set1.intersection_update(set2)

# iii) Symmetric difference of the sets.
symmetric_difference_set = set1.symmetric_difference(set2)

# iv) Check for subsets and supersets.
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)

# v) Check for disjointness of the sets.
is_disjoint = set1.isdisjoint(set2)

# 6) Create a dataset of students for a college.

# Define dataset of students
students_dataset = [
    {"S_Id": 1, "E_Num": "001", "Branch": "CSE", "S_Name": "Gangaprasad"},
    {"S_Id": 2, "E_Num": "002", "Branch": "IT", "S_Name": "Omkar"},
    {"S_Id": 3, "E_Num": "003", "Branch": "Mech", "S_Name": "Bhavesh"},
]

# 7) Extract at least 3 students’ names and branches.

# Extract data
extracted_data = students_dataset[:3]

# Create lists for names and branches
names = [student["S_Name"] for student in extracted_data]
branches = [student["Branch"] for student in extracted_data]

# 8) Create a similar type of dataset for college library.

# Define dataset for library
library_dataset = [
    {"Book_Id": 1, "Title": "Book1", "Author": "Author1", "Issued": False},
    {"Book_Id": 2, "Title": "Book2", "Author": "Author2", "Issued": False},
    {"Book_Id": 3, "Title": "Book3", "Author": "Author3", "Issued": True},
]

# 9) Add a Boolean key in the dataset which is true if a book is issued and false if a book is yet to be issued by the student.

# Add 'Issued' key with boolean value
for book in library_dataset:
    book["Issued"] = True  

# 10) Add students with given lists in the dataset of Q6.

# Update students dataset with given lists
name = ['ABC', 'XYZ', 'CDE', 'SLP']
branch = ['CSE', 'IT', 'Mech', 'ECE']

for i in range(len(name)):
    students_dataset.append({
        "S_Id": i + 4,  
        "E_Num": f"{i+1}",  
        "Branch": branch[i],
        "S_Name": name[i]
    })

# Print the datasets
print(list_1)
print(list_2)
print(students_tuple)
print(student1, student2, other_students)
print(union_set)
print(set1)
print(symmetric_difference_set)
print(is_subset)
print(is_superset)
print(is_disjoint)
print(students_dataset)
print(names)
print(branches)
print(library_dataset)
