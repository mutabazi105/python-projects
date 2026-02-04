'''student_count = 100
course_code = 4.50
course_name = 'Mathematics'
decision = True

print(type(student_count))
print(type(decision))

student_id = input('please give the students id:')

print(student_id)

message = """

Hi Ben 

I want to say something to you 
do you remember that yesterday was 
the daye we supposed to go home!!!!

"""

print(message)'''


'''course_name = 'Paython Programing'

print(len(course_name))

print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])'''

'''course_name2 = "Python \"Programing\""
print(course_name2)

first_name = 'Python Programming'
second_name = 'Mutabazi'

# full = first_name+" "+second_name

full = f'{first_name} {second_name}'

print(full)

print(first_name.upper())
print(first_name.lower())
print(first_name.capitalize())
print(first_name.title())
print(first_name.strip())
print(first_name.rstrip())
print(first_name.lstrip())

print(first_name.replace('P', 'N')) '''


# print(10**2)

# print(round(2.9))
# print(abs(-2.9))

# print(bool("False"))
'''
temperature = 12

if temperature > 30:
    print('it is warm')
    print('Please drink enought water')

elif temperature < 30:
    print('The weather is good')

else:
    print('it is very cold')

print('Done')
'''

# age = 17
# message = 'Eligible' if age >= 18 else 'Not eligible'
# print(message)

import numpy as np
beispiel_array = np.array([10, 20, 30, 40, 50])

print("Beispiel element", beispiel_array)
print("Drittes Eelement", beispiel_array[2])
print("Jedes Element", beispiel_array[-2])
print("Slice von index 1 bis4:", beispiel_array[1:4])
print("Jedes Element", beispiel_array[::2])
print("Slice von index 1 bis4:", beispiel_array[-2:])

bool_array = np.array([True, False, True, False, True])

print('Array mit boolean Element', beispiel_array[bool_array])
