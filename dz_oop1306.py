class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def arithmetic_mean(self):
        list_values = []
        for grade in self.grades.values():
            for grade_0 in grade:
                list_values.append(grade_0)
                arithmetic_result = sum(list_values) / len(list_values)
            return arithmetic_result

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        elif self.arithmetic_mean() < other.arithmetic_mean():
            return print(f'{self.arithmetic_mean()} меньше {other.arithmetic_mean()}')
        else:
            return print(f'{self.arithmetic_mean()} больше {other.arithmetic_mean()}')

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{self.arithmetic_mean()}' \
              f'\nКурсы в процессе изучения:{",".join(self.courses_in_progress)}\nЗавершенные курсы:' \
              f'{" ".join(self.finished_courses)}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {Student.arithmetic_mean(self)}'\
              f'\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        elif Student.arithmetic_mean(self) < Student.arithmetic_mean(other):
            return print(f'{Student.arithmetic_mean(self)} меньше {Student.arithmetic_mean(other)}')
        else:
            return print(f'{Student.arithmetic_mean(self)} больше {Student.arithmetic_mean(other)}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n '
        return res


some_lecturer = Lecturer('Some', 'Lector')
best_lecturer = Lecturer('Best', 'Lektor')

some_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']

some_student = Student('Some', 'Student', 'your_gender')
best_student = Student('Best', 'Student', 'м')

some_student.finished_courses += ['Git']
some_student.courses_in_progress += ['Python', 'English']
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9)


best_student.courses_in_progress += ['Git', 'Python']
best_student.rate_hw(best_lecturer, 'Git', 6)
best_student.rate_hw(best_lecturer, 'Git', 7)

some_reviewer = Reviewer('Some', 'Reviewer')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 8)
some_reviewer.rate_hw(best_student, 'Python', 9)
best_reviewer = Reviewer('Best', 'Reviewer')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Git']
best_reviewer.rate_hw(some_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Git', 9)
print(best_reviewer)
print(best_lecturer)
print(some_student)
print(some_reviewer)
print(some_lecturer)
print(best_student)
print(some_student > best_student)
print(some_lecturer < best_lecturer)
students_list = [best_student, some_student]
lectors_list = [best_lecturer, some_lecturer]


def average_grade_students(student_list, course):
    total = 0
    counter = 0
    for student in student_list:
        if course in student.courses_in_progress:
            student_course_average = sum(student.grades[course]) / len(student.grades[course])
            total += student_course_average
            counter += 1
    if counter == 0:
        return 'Нет студентов изучающих этот курс'
    else:
        return f'Средний бал по курсу {course} у студентов: {total / counter}'


print(average_grade_students(students_list, 'Python'))
print(average_grade_students(students_list, 'Git'))


def average_grade_lectors(lector_list, course):
    total = 0
    counter = 0
    for lector in lector_list:
        if course in lector.courses_attached:
            lector_course_average = sum(lector.grades[course]) / len(lector.grades[course])
            total += lector_course_average
            counter += 1
    if counter == 0:
        return 'Нет студентов изучающих этот курс'
    else:
        return f'Средний бал по курсу {course} у лекторов : {total / counter}'


print(average_grade_lectors(lectors_list, 'Python'))
print(average_grade_lectors(lectors_list, 'Git'))
