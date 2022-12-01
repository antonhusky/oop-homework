class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        grade_sum = 0
        count = 0
        for grade in self.grades.values():
            grade_sum += sum(grade)
            count += len(grade)
        return grade_sum / count

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


student1 = Student('Anton', 'Ivanov', 'Gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Ivan', 'Antonov', 'Gender')
student2.courses_in_progress += ['JavaScript']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

lecturer1 = Lecturer('Ivan', 'Ivanov')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']
lecturer1.grades.update({'Python': [10, 10, 10, 10, 10]})
lecturer1.grades.update({'Git': [10, 10, 10, 10, 10]})

lecturer2 = Lecturer('Anton', 'Antonov')
lecturer2.courses_attached += ['JavaScript']
lecturer2.courses_attached += ['Git']
lecturer2.grades.update({'JavaScript': [10, 10, 10, 10, 10]})
lecturer2.grades.update({'Git': [10, 10, 10, 10, 10]})

reviewer1 = Reviewer('Voktor', 'Sineglazov')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Sergey', 'Goluboglazov')
reviewer2.courses_attached += ['Git']
reviewer2.courses_attached += ['JavaScript']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'JavaScript', 9)
reviewer2.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student2, 'Git', 10)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Git', 10)
student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Git', 9)


def average_grade_all_students(students, course):
    grade_sum = 0
    count = 0
    for student in students:
        if course in student.grades:
            grade_sum += sum(student.grades[course])
            count += len(student.grades[course])
    return grade_sum / count


def average_grade_all_lecturer(lecturers, course):
    grade_sum = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            grade_sum += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return grade_sum / count


print('Студенты:')
print(student1)
print(student2)

print('\nЛекторы:')
print(lecturer1)
print(lecturer2)

print('\nРевьюеры:')
print(reviewer1)
print(reviewer2)

print('\nСредние оценки студентов по курсам')
print('Средняя оценка за домашние задания всех студентов по курсу Python:',
      average_grade_all_students([student1, student2], 'Python'))
print('Средняя оценка за домашние задания всех студентов по курсу Git:',
      average_grade_all_students([student1, student2], 'Git'))
print('Средняя оценка за домашние задания всех студентов по курсу JavaScript:',
      average_grade_all_students([student1, student2], 'JavaScript'))

print('\nСредние оценки лекторов по курсам')
print('Средняя оценка за лекции всех лекторов по курсу Python:',
      average_grade_all_lecturer([lecturer1, lecturer2], 'Python'))
print('Средняя оценка за лекции всех лекторов по курсу Git:',
      average_grade_all_lecturer([lecturer1, lecturer2], 'Git'))
print('Средняя оценка за лекции всех лекторов по курсу JavaScript:',
      average_grade_all_lecturer([lecturer1, lecturer2], 'JavaScript'))
