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
            print(course, round(avg_grade, 1))
            all_avg_grade += [avg_grade]
        return round(sum(all_avg_grade) / len(all_avg_grade), 1)

    def __str__(self):
        finished_courses = self.finished_courses
        return f'Имя: {self.name}' '\n' f'Фамилия: {self.surname}' '\n' f'Средняя оценка за домашние задания: {self.avg_grade()}'\
               '\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}' '\n' f'Завершенные курсы: {", ".join(self.finished_courses)}'
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            #print(f'Средняя оценка студента: {self.avg_grade()}')
            #print(f'Средняя оценка лектора: {other.avg_grade()}')
            return self.avg_grade() < other.avg_grade()
        else:
            return 'Указан не верный класс, ожидается класс Лекторы'


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
            print(course, round(avg_grade, 1))
            all_avg_grade += [avg_grade]
        return round(sum(all_avg_grade) / len(all_avg_grade), 1)

    def __str__(self):
        return f'Имя: {self.name}' '\n'  f'Фамилия: {self.surname}' '\n' f'Средняя оценка за лекции: {self.avg_grade()}'

    def __lt__(self, other):
        if isinstance(other, Student):
            #print(f'Средняя оценка лектора: {self.avg_grade()}')
            #print(f'Средняя оценка студента: {other.avg_grade()}')
            return self.avg_grade() < other.avg_grade()
        else:
            return 'Указан не верный класс'

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



# Reviewers
rackham, graff = Reviewer('Mazer', 'Rackham'), Reviewer('Hayram', 'Graff')
rackham.courses_attached += ['Тактика', 'Стратегия', 'Выживание']
graff.courses_attached += ['Тактика', 'Стратегия']

# Lecturers
sergeant = Lecturer('Sergeant', 'Dap')
sergeant.courses_attached += ['Тактика', 'Выживание']
sergeant.lecturer_grades = {'Тактика': [4, 1, 5, 5], 'Выживание': [4, 9, 3]}

major = Lecturer('Gwen', 'Anderson')
major.courses_attached += ['Стратегия', 'Тактика']
major.lecturer_grades = {'Тактика': [4, 6, 8, 5], 'Стратегия': [2, 1, 4]}


# Students
wiggin = Student('Ender', 'Wiggin', 'male')
wiggin.courses_in_progress += ['Тактика', 'Стратегия']
wiggin.grades = {'Тактика': [4, 1, 5, 8], 'Стратегия': [2, 9, 4]}
wiggin.finished_courses = ['Выживание']

madrid = Student('Bonzo', 'Madrid', 'male')
madrid.courses_in_progress += ['Тактика', 'Выживание']
madrid.grades = {'Тактика': [4, 6, 5], 'Выживание': [2, 4, 1]}
madrid.finished_courses = ['Лидерство']

# Methods
wiggin.rate_lecturer(sergeant, 'Тактика', 10)
madrid.rate_lecturer(major, 'Cтратегия', 4)

rackham.rate_hw(wiggin, 'Cтратегия', 6)
graff.rate_hw(madrid, 'Тактика', 5)



print('Reviewers:', rackham, graff, 'Lecturers:', sergeant, major, 'Students:', wiggin, madrid, sep='\n'*2, end='\n'*2)

print(wiggin < sergeant)
print(major < madrid)

print(wiggin < madrid) # вывод с ошибкой

students = [wiggin, madrid]
lecturers = [sergeant, major]
def student_avg_per_course(students, course):
    all_avg_grade = []
    for student in students:
        for k, v in student.grades.items():
            if course == k:
                avg_grade = sum(v) / len(v)
                #print(lecturer.name, course, round(avg_grade, 1))
                all_avg_grade += [avg_grade]
    return print(f"Средняя оценки за домашние задания по всем студентам в рамках конкретного курса '{course}':", round(sum(all_avg_grade) / len(all_avg_grade), 1))

def lecturer_avg_per_course(lecturers, course):
    all_avg_grade = []
    for lecturer in lecturers:
        for k, v in lecturer.lecturer_grades.items():
            if course == k:
                avg_grade = sum(v) / len(v)
                #print(lecturer.name, course, round(avg_grade, 1))
                all_avg_grade += [avg_grade]
    return print(f"Средняя оценка за лекции всех лекторов в рамках курса '{course}':", round(sum(all_avg_grade) / len(all_avg_grade), 1))

#print(wiggin.grades, madrid.grades, sep='\n')
student_avg_per_course(students,'Стратегия')
student_avg_per_course(students,'Тактика')
# print(sergeant.lecturer_grades)
# print(sergeant.avg_grade())
#
# print(major.lecturer_grades)
# print(major.avg_grade())
lecturer_avg_per_course(lecturers,'Выживание')
lecturer_avg_per_course(lecturers,'Тактика')

