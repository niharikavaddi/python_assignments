class Student:
    __student_list = []

    def __init__(self, student_id=None, student_name=None, student_year=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_year = student_year
        self.student_grade = None
        self.course_list = list()

    def check_if_student_exists(self, student_id):
        if student_id in [student.student_id for student in self.__student_list if
                          student.student_id == student_id]:
            return True
        else:
            return False

    def get_student_by_id(self, student_id):
        return filter(lambda student: student.student_id == student_id,
                      self.__student_list).__next__()

    def get_all_students(self):
        return self.__student_list

    def __repr__(self):
        return f" Student ID: {self.student_id}, Student Name: {self.student_name}, Student Year: {self.student_year}, Student Grade: {self.student_grade}, Courses: {self.course_list}"


class Course:
    __course_list = []

    def __init__(self, course_id=None, course_name=None, professor_name=None):
        self.course_id = course_id
        self.course_name = course_name
        self.professor_name = professor_name

    def check_if_course_exists(self, course_id):
        if course_id in [course.course_id for course in self.__course_list if
                         course.course_id == course_id]:
            return True
        else:
            return False

    def get_course_by_id(self, course_id):
        return filter(lambda course: course.course_id == course_id,
                      self.__course_list).__next__()

    def get_all_courses(self):
        return self.__course_list

    def __repr__(self):
        return f" Course ID: {self.course_id}, Course Name: {self.course_name}, Professor Name: {self.professor_name}"


class Admin(Course, Student):
    admin_id = "1234"
    admin_password = "password"
    admin_name = "Lakshmi"

    def add_courses(self):
        course_id, course_name, professor_name = [str(x) for x in
                                                  input("Course ID, Course Name, Professor Name : ").split(",")]
        if not self.check_if_course_exists(course_id):
            self.get_all_courses().append(Course(course_id, course_name, professor_name))
            print("Course added")
        else:
            print("Course already exists")

    def modify_courses(self):
        course_id = input("Enter Course ID: ")
        if self.check_if_course_exists(course_id):
            course = self.get_course_by_id(course_id)
            course.course_name = input("Enter Updated Course Name: ")
            course.professor_name = input("Enter Updated Professor Name: ")
            print("Course details updated")
        else:
            print("Course doesn't exist")

    def delete_courses(self):
        course_id = input("Enter Course ID: ")
        if self.check_if_course_exists(course_id):
            self.get_all_courses().remove(
                self.get_course_by_id(course_id))
            print("Course details deleted")
        else:
            print("Course doesn't exist")

    def add_student(self):
        student_id, student_name, student_year = [str(x) for x in
                                                  input("Student ID, Student Name, Student Year: ").split(",")]
        if not self.check_if_student_exists(student_id):
            self.get_all_students().append(Student(student_id, student_name, student_year))
            print("Student added")
        else:
            print("Student already exists")

    def modify_student(self):
        student_id = input("Enter Student ID: ")
        if self.check_if_student_exists(student_id):
            student = self.get_student_by_id(student_id)
            student.student_name = input("Enter Updated Student Name: ")
            student.student_year = input("Enter Updated Student Year: ")
            print("Student details updated")
        else:
            print("Student doesn't exist")

    def delete_student(self):
        student_id = input("Enter Student ID: ")
        if self.check_if_student_exists(student_id):
            self.get_all_students().remove(
                self.get_student_by_id(student_id))
            print("Student details deleted")
        else:
            print("Student doesn't exist")

    def enroll_student(self):
        student_id = input("Enter Student ID: ")
        if self.check_if_student_exists(student_id):
            course_id = input("Course ID: ")
            if self.check_if_course_exists(course_id):
                student = self.get_student_by_id(student_id)
                if course_id not in student.course_list:
                    student.course_list.append(course_id)
                    print(student_id + " enrolled in " + course_id)
                else:
                    print("Already enrolled")
            else:
                print("Course doesn't exist")
        else:
            print("Student doesn't exist")

    def disenroll_student(self):
        student_id = input("Enter Student ID: ")
        if self.check_if_student_exists(student_id):
            course_id = input("Course ID: ")
            if self.check_if_course_exists(course_id):
                student = self.get_student_by_id(student_id)
                if course_id in student.course_list:
                    student.course_list.remove(course_id)
                    print(student_id + " dropped " + course_id)
                else:
                    print("No enrollment registered")
            else:
                print("Course doesn't exist")
        else:
            print("Student doesn't exist")

    def submit_grade(self):
        student_id = input("Enter Student ID: ")
        if self.check_if_student_exists(student_id):
            grade = input("Enter Overall Grade: ")
            self.get_student_by_id(student_id).student_grade = grade
            print("Grade Updated")
        else:
            print("Student doesn't exist")

    def show_courses(self):
        print(*self.get_all_courses(), sep='\n')

    def show_students(self):
        print(*self.get_all_students(), sep='\n')


# START

print("Student and Course Management System")
admin_id = input("Enter Admin ID: ")
admin_password = input("Enter Admin Password: ")
if admin_id == Admin.admin_id and Admin.admin_password == admin_password:
    admin = Admin()
    choices = {
        1: admin.add_courses,
        2: admin.modify_courses,
        3: admin.delete_courses,
        4: admin.add_student,
        5: admin.modify_student,
        6: admin.delete_student,
        7: admin.enroll_student,
        8: admin.disenroll_student,
        9: admin.submit_grade,
        10: admin.show_courses,
        11: admin.show_students
    }
    print(f"Welcome {Admin.admin_name}!" + """
                0. Exit
                1. Add courses
                2. Modify courses
                3. Delete courses
                4. Add students
                5. Modify students
                6. Delete students
                7. Enroll students
                8. Disenroll students
                9. Enter grades
                10. Show courses
                11. Show students

                """)
    while True:
        choice = int(input("Task: "))
        if choice != 0:
            choices.get(choice)()
        else:
            print("Thank you")
            break

else:
    print("Wrong admin credentials")
