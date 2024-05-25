grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Hendrik', 'Aaron'}
print(students)
sorted_students = (sorted(students))
print(sorted_students)
gpa_0 = (float(sum(grades[0]) / len(grades[0])))
gpa_1 = (float(sum(grades[1]) / len(grades[1])))
gpa_2 = (float(sum(grades[2]) / len(grades[2])))
gpa_3 = (float(sum(grades[3]) / len(grades[3])))
gpa_4 = (float(sum(grades[4]) / len(grades[4])))
gpa_all = [(f'{gpa_0:.2f}'), (f'{gpa_1:.2f}'), (f'{gpa_2:.2f}'), (f'{gpa_3:.2f}'), (f'{gpa_4:.2f}')]
print(gpa_all)
my_list = [[sorted_students[0], gpa_all[0]], [sorted_students[1], gpa_all[1]], [sorted_students[2], gpa_all[2]], [sorted_students[3], gpa_all[3]], [sorted_students[4], gpa_all[4]]]
print(my_list)
GPA = dict(my_list)
print(GPA)
