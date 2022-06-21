class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (
                self.courses_in_progress or self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.courses_attached:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        all_avg_grade = []
        for course, grades in self.grades.items():
            avg_grade = sum(grades) / len(grades)
            all_avg_grade += [avg_grade]
        return round(sum(all_avg_grade) / len(all_avg_grade), 1)

    def __str__(self):
        return f'Имя: {self.name}' '\n'  f'Фамилия: {self.surname}' '\n' f'Средняя оценка за домашние задания: {self.avg_grade()}'\
               '\n' f'Курсы в процессе изучения: {self.courses_in_progress}' '\n' f'Завершенные курсы: {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}


    def avg_grade(self):
        all_avg_grade = []
        for course, grades in self.lecturer_grades.items():
            avg_grade = sum(grades) / len(grades)
            all_avg_grade += [avg_grade]
        return round(sum(all_avg_grade) / len(all_avg_grade), 1)

    def __str__(self):
        return f'Имя: {self.name}' '\n'  f'Фамилия: {self.surname}' '\n' f'Средняя оценка за лекции: {self.avg_grade()}'


class Reviewer(Mentor):   # эксперты, проверяющие домашние задания
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}' '\n'  f'Фамилия: {self.surname}'


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# some_reviewer = Reviewer('Some', 'Buddy')
# some_reviewer.courses_attached += ['Python', 'Git']
# print(some_reviewer)
# some_lecturer = Lecturer('Some', 'Buddy')
# some_lecturer.courses_attached += ['Python', 'Git']
# some_lecturer.lecturer_grades = {'Python': [4, 1, 5], 'Git': [2,9,4]}
# print(some_lecturer)

some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python', 'Git']
some_student.grades = {'Python': [4, 1, 5], 'Git': [2,9,4]}
some_student.finished_courses = ['Java']
print(some_student)

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)

# А у студентов так:
#
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# Реализуйте возможность сравнивать (через операторы сравнения)
# между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
