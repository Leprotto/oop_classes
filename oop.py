class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress or
                course in self.finished_courses and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def student_average_grade(self):
        total_grades = sum(len(grades) for grades in self.grades.values())
        if total_grades == 0:
            return 0.0
        else:
            total_score = sum(grade for grades in self.grades.values() for grade in grades)
            return round(total_score / total_grades, 1)

    def __str__(self):
        average_grade = self.student_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}')

    def __lt__(self, other):
        return self.student_average_grade() < other.gstudent_average_grade()

    def __gt__(self, other):
        return self.student_average_grade() > other.student_average_grade()

    def __eq__(self, other):
        return self.student_average_grade() == other.student_average_grade()

# some_student = Student('Ruoy', 'Eman', 'Мale')
# some_student.courses_in_progress = ['Python', 'Git']
# some_student.finished_courses = ['Введение в программирование']
# some_student.grades = {'Python': [10, 9.9, 10], 'Git': [10, 10, 9.9], 'Введение в программирование': [9.9, 10, 9.8]}
# print(some_student)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lecturer_average_grade(self):
        total_grades = sum(len(grades) for grades in self.grades.values())
        if total_grades == 0:
            return 0.0
        else:
            total_score = sum(grade for grades in self.grades.values() for grade in grades)
            return round(total_score / total_grades, 1)

    def __str__(self):
        average_grade = self.lecturer_average_grade()
        courses_attached = ', '.join(self.courses_attached)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nПреподает на курсах: {courses_attached}\n'
                f'Средняя оценка за лекции: {average_grade}')

    def __lt__(self, other):
        return self.lecturer_average_grade() < other.lecturer_average_grade()

    def __gt__(self, other):
        return self.lecturer_average_grade() > other.lecturer_average_grade()

    def __eq__(self, other):
        return self.lecturer_average_grade() == other.lecturer_average_gradede()

# some_lecturer = Lecturer('Some', 'Buddy')
# some_lecturer.grades = {'Python': [9.9, 10, 9.9]}
# print(some_lecturer)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in
                student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

# some_reviewer = Reviewer('Some', 'Buddy')
# print(some_reviewer)

student_1 = Student('Петр', 'Иванов', 'Мужской')
student_1.courses_in_progress = ['Python', 'C++']
student_1.finished_courses = ['Git']

student_2 = Student('Андрей', 'Сидоров', 'Мужской')
student_2.courses_in_progress = ['Python', 'Java']
student_2.finished_courses = ['Git']
students = [student_1, student_2]

lecturer_1 = Lecturer('Николай', 'Миронов')
lecturer_1.courses_attached = ['Python', 'Java']

lecturer_2 = Lecturer('Сергей', 'Свиридов')
lecturer_2.courses_attached = ['Git', 'C++']
lecturers = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Олег', 'Соколов')
reviewer_1.courses_attached = ['Python', 'Git']

reviewer_2 = Reviewer('Алексей', 'Волков')
reviewer_2.courses_attached = ['C++', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'C++', 8)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_1.rate_hw(student_2, 'Git', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'C++', 9)
student_1.rate_lecturer(lecturer_2, 'Git', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Java', 9)
student_2.rate_lecturer(lecturer_2, 'Git', 10)

print(student_1)
print(student_2)
if student_1 > student_2:
    print(f'{student_1.name} имеет более высокий средний балл, чем {student_2.name}')
else:
    print(f'{student_2.name} имеет более высокий средний балл, чем {student_1.name}')

print(lecturer_1)
print(lecturer_2)
if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name} преподает лучше, чем {lecturer_2.name}')
else:
    print(f'{lecturer_2.name} преподает лучше, чем {lecturer_1.name}')

print(reviewer_1)
print(reviewer_2)

def calc_avg_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            for grade in student.grades[course]:
                total_grades += grade
                total_students += 1
    if total_students == 0:
        return 0.0
    return round(total_grades / total_students, 1)

print(f"Средний балл студентов по курсу Git: {calc_avg_grade(students, 'Git')}")
print(f"Средний балл студентов по курсу Python: {calc_avg_grade(students, 'Python')}")
print(f"Средний балл студентов по курсу Java: {calc_avg_grade(students, 'Java')}")
print(f"Средний балл студентов по курсу C++: {calc_avg_grade(students, 'C++')}")

def calc_avg_lecture_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if hasattr(lecturer, 'courses_attached') and course in lecturer.courses_attached:
            if hasattr(lecturer, 'grades') and course in lecturer.grades:
                for grade in lecturer.grades[course]:
                    total_grades += grade
                    total_lecturers += 1
    if total_lecturers == 0:
        return 0.0
    return round(total_grades / total_lecturers, 1)

print(f"Средняя оценка лекторов по курсу Git: {calc_avg_lecture_grade(lecturers, 'Git')}")
print(f"Средняя оценка лекторов по курсу Python: {calc_avg_lecture_grade(lecturers, 'Python')}")
print(f"Средняя оценка лекторов по курсу C++: {calc_avg_lecture_grade(lecturers, 'C++')}")
print(f"Средняя оценка лекторов по курсу Java: {calc_avg_lecture_grade(lecturers, 'Java')}")