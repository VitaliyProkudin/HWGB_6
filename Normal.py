# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.


# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
#
from collections import namedtuple

class Student:

    def __init__(self):
        self.student = ["Egor Petrov", "Vasya Pupochkin", "Vladimir Petushkov", "Lamila Kostileva", "Lena Glubokova"]
        self.parents_father = ["Timur Petrov", "Gosha Pupochkin", "Vladislav Petushkov", "Kolya Kostilev",
                               "Sergei Glubokov"]
        self.parents_mather = ["Olga Petrova", "Elena Pupochkina", "Sveta Petushkova", "Katerina Kostileva",
                               "Nina Glubokova"]
        # self.student_id = student_id

    """Ученики , # У каждого ученика есть два Родителя(мама и папа).
    Родители"""  # 4. Узнать ФИО родителей указанного ученика

    def get_student_all(self):
        return self.student

    def get_parents_father(self):
        return self.parents_father

    def get_parents_mather(self):
        return self.parents_mather

    def get_student_parents_FIO(self, student_id):
        # print(type(self.parents_father))
        # x = [y.split(" ")[1] for y in self.parents_father]
        # print(x)
        mom = 0
        pop = 0
        if student_id in self.student:
            if student_id.split(" ")[1] in [x.split(" ")[1] for x in self.parents_father] or student_id.split(" ")[1][0: -1] in [l.split(" ")[1] for l in self.parents_father] or student_id.split(" ")[1][0: -2] in [s.split(" ")[1] for s in self.parents_father] and student_id.split(" ")[1] in [y.split(" ")[1][0:-1] for y in self.parents_mather] or student_id.split(" ")[1] in [n.split(" ")[1][0:-2] for n in self.parents_mather]:
                for i in range(len(self.parents_father)):
                    if self.parents_father[i].split(" ")[1] == student_id.split(" ")[1] or self.parents_father[i].split(" ")[1] == student_id.split(" ")[1][0:-1] or self.parents_father[i].split(" ")[1] == student_id.split(" ")[1][0:-2]:
                        pop = self.parents_father[i]

                for i in range(len(self.parents_mather)):
                    if self.parents_mather[i].split(" ")[1][0:-1] == student_id.split(" ")[1] or self.parents_mather[i].split(" ")[1][0:-1] == student_id.split(" ")[1][0:-2] or self.parents_mather[i].split(" ")[1][0:-1] == student_id.split(" ")[1] or self.parents_mather[i].split(" ")[1] == student_id.split(" ")[1]:
                        mom = self.parents_mather[i]

                return (f"Родители студента {student_id} Папа:{pop} Мама:{mom}")
        return False

class School(Student):

    def __init__(self): # student, parents_father, parents_mather
        # self.classtype = classtype
        # "Классы"  В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
        # self.class_5A = list()
        # self.class_5B = list()
        # self.class_5C = list()
        # self.class_6A = list()
        # self.class_6B = list()

        self.class_of_school = ["5A", "5B", "5C", "6A", "6B"]
        # "Учителя"
        self.teacher = ["Anrdey Kolesnikov", "Vladimir Gorelov", "Vitaliy Putin", "Kentavr Kolbasinov"]
        # "Занятия"
        self.lesson = ["Math", "Physics", "Madhouse"]
        # 'Описание"
        Student.__init__(self)
        # 1. Получить полный список всех классов школы
        self.dict_klass_in_student = {self.student[0]: self.class_of_school[0],
                                      self.student[1]: self.class_of_school[1],
                                      self.student[2]: self.class_of_school[2],
                                      self.student[3]: self.class_of_school[3],
                                      self.student[4]: self.class_of_school[4],
                                      }
        # Массивы для записи уроков в классы



        # Словари для связок. Пример учитель(key) > урок(value)
        self.dict_teacher_lesson = dict()
        self.dict_klass_on_teacher = dict()
        self.dict_klass_in_lesson = dict()

        # 2. Получить список всех учеников в указанном классе



    def get_all_class_of_school(self):
        return self.dict_klass_in_student
        # Получить все классы школы
    def get_class_of_school(self):
        return self.class_of_school

    def get_teacher_all(self):
        return self.teacher

    def del_class_of_school(self, classtype):
        return self.class_of_school.remove(classtype)

    def add_class_of_school(self, classtype):
        return self.class_of_school.append(classtype)

    def add_teacher_lesson(self, teacher_usr, lesson_usr):
        if teacher_usr in self.teacher and lesson_usr in self.lesson:
            #Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не может преподавать никто друго
            if not teacher_usr in self.dict_teacher_lesson:
                self.dict_teacher_lesson[teacher_usr] = lesson_usr
                return True
        return False

    def add_klass_teacher(self, teacher_usr, klass_usr):
        if teacher_usr in self.teacher and klass_usr in self.class_of_school:
            if not self.dict_klass_on_teacher.get(teacher_usr) == klass_usr:

                self.dict_klass_on_teacher[klass_usr] = teacher_usr
                return True
        return False

    def add_klass_in_lesson(self, klass_usr, lesson_usr):
        if klass_usr in self.class_of_school and lesson_usr in self.lesson:
            if not self.dict_klass_in_lesson.get(klass_usr) == lesson_usr:
                tmp = list()
                if self.dict_klass_in_lesson.get(klass_usr) != None:
                    for item in self.dict_klass_in_lesson.get(klass_usr):
                        tmp.append(item)
                    tmp.append(lesson_usr)
                else:
                    tmp.append(lesson_usr)
                self.dict_klass_in_lesson[klass_usr] = tmp
                return self.dict_klass_in_lesson
            return False

    def schooll_grid(self, student_id):  # (Ученик --> Класс --> Учителя --> Предметы)
            a = list()
            a.append(student_id)
            a.append(self.dict_klass_in_student.get(student_id))
            a.append(self.dict_klass_on_teacher.get(self.dict_klass_in_student.get(student_id)))
            a.append(self.dict_klass_in_lesson.get(self.dict_klass_in_student.get(student_id)))
            return a

# -------Main------
# 5. Получить список всех Учителей, преподающих в указанном классе
a = "Lamila Kostileva"
stud = Student()
x = School()

# add add_teacher_lesson
x.add_teacher_lesson("Anrdey Kolesnikov", "Madhouse")
x.add_teacher_lesson("Vladimir Gorelov", "Math")
x.add_teacher_lesson("Vitaliy Putin", "Physics")

# add_klass_in_lesson
x.add_klass_in_lesson("5A", "Math")
x.add_klass_in_lesson("5A", "Physics")
x.add_klass_in_lesson("5A", "Madhouse")
x.add_klass_teacher("Anrdey Kolesnikov", "5A")

# add_klass_in_lesson
x.add_klass_in_lesson("5B", "Math")
x.add_klass_in_lesson("5B", "Madhouse")
x.add_klass_teacher("Kentavr Kolbasinov", "5B")


# Tod
print(x.schooll_grid('Vasya Pupochkin'))