from collections.abc import Iterable, Iterator


def add_matter_4(cls):
    original_init = cls.__init__

    def new_init(self, name, matter_1, matter_2, matter_3, matter_4=0):
        original_init(self, name, matter_1, matter_2, matter_3)
        self.matter_4 = matter_4

    cls.__init__ = new_init
    return cls


@add_matter_4
class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3

    def __repr__(self):
        return (f"Student({self.name}, "
                f"matter_1={self.matter_1}, "
                f"matter_2={self.matter_2}, "
                f"matter_3={self.matter_3}, "
                f"matter_4={self.matter_4})")


class Matter1Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda student: student.matter_1, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class Matter2Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda student: student.matter_2, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class Matter3Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda student: student.matter_3, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


def add_matter_4_iterator(cls):
    class Matter4Iterator(Iterator):
        def __init__(self, students):
            self.students = sorted(students, key=lambda student: student.matter_4, reverse=True)
            self.index = 0

        def __next__(self):
            if self.index >= len(self.students):
                raise StopIteration
            student = self.students[self.index]
            self.index += 1
            return student

    def get_matter_4_iterator(self):
        return Matter4Iterator(self.students)

    cls.get_matter_4_iterator = get_matter_4_iterator
    return cls


@add_matter_4_iterator
class SchoolClass(Iterable):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls)
            cls._instance.students = []
        return cls._instance

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        return sorted(self.students, key=lambda student: student.matter_1, reverse=True)

    def rank_matter_2(self):
        return sorted(self.students, key=lambda student: student.matter_2, reverse=True)

    def rank_matter_3(self):
        return sorted(self.students, key=lambda student: student.matter_3, reverse=True)

    def __iter__(self):
        return Matter1Iterator(self.students)

    def get_matter_2_iterator(self):
        return Matter2Iterator(self.students)

    def get_matter_3_iterator(self):
        return Matter3Iterator(self.students)


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13, 11))
    school_class.add_student(Student('A', 8, 2, 17, 15))
    school_class.add_student(Student('V', 9, 14, 14, 16))

    print("Classement matière 1 :")
    print(school_class.rank_matter_1())

    print("Classement matière 2 :")
    print(school_class.rank_matter_2())

    print("Classement matière 3 :")
    print(school_class.rank_matter_3())

    print("Itération sur matière 1 :")
    for student in school_class:
        print(student)

    print("Itération sur matière 2 :")
    for student in school_class.get_matter_2_iterator():
        print(student)

    print("Itération sur matière 3 :")
    for student in school_class.get_matter_3_iterator():
        print(student)

    print("Itération sur matière 4 :")
    for student in school_class.get_matter_4_iterator():
        print(student)

    another_class = SchoolClass()

    print("Singleton test :", school_class is another_class)
