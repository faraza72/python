def secondlow(students):
    grades = []
    for student in students:
        grades.append(student[1])
    sort_grades = sorted(grades)
    seclow_grade = sort_grades[0]
    for grade in sort_grades:
        if grade != seclow_grade:
            seclow_grade = grade
            break
    seclow_stud = []
    for student in students:
        if student[1] == seclow_grade:
            seclow_stud.append(student[0])
    for name in sorted(seclow_stud):
        print(name)

l = []
for i in range(int(raw_input())):
    d = []
    name = raw_input()
    score = float(raw_input())
    d.append(name)
    d.append(score)
    l.append(d)
secondlow(l)

