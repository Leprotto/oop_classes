class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
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

some_student = Student('Ruoy', 'Eman', 'Мale')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student.grades = {'Python': [10, 9.9, 10], 'Git': [10, 10, 9.9], 'Введение в программирование': [9.9, 10, 9.8]}
print(some_student)
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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}'

    def __lt__(self, other):
        return self.lecturer_average_grade() < other.lecturer_average_grade()

    def __gt__(self, other):
        return self.lecturer_average_grade() > other.lecturer_average_grade()

    def __eq__(self, other):
        return self.lecturer_average_grade() == other.lecturer_average_gradede()

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {'Python': [9.9, 10, 9.9]}
print(some_lecturer)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in
                student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)