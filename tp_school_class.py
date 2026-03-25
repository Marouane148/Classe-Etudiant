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
                f"matter_3={self.matter_3})")


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print(school_class.students)
