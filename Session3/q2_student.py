# تمرین ۲: کلاس Student (همراه با بخش امتیازی Classroom)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}  # دیکشنری نمرات: درس به عنوان کلید، نمره به عنوان مقدار

    def add_grade(self, course, grade):
        """ثبت نمره یک درس با بررسی معتبر بودن بازه ۰ تا ۲۰"""
        if 0 <= grade <= 20:
            self.grades[course] = grade
        else:
            print("Invalid grade")

    def average(self):
        """محاسبه میانگین نمرات دانشجو"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def best_course(self):
        """یافتن درسی که دانشجو در آن بالاترین نمره را گرفته است"""
        if not self.grades:
            return None
        return max(self.grades, key=lambda c: self.grades[c])

    def failed_courses(self):
        """لیست درس‌هایی که نمره کمتر از ۱۰ دارند"""
        failed = []
        for course, grade in self.grades.items():
            if grade < 10:
                failed.append(course)
        return failed

    def status(self):
        """تعیین وضعیت تحصیلی بر اساس میانگین"""
        avg = self.average()
        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"

    def report(self):
        """چاپ کامل کارنامه دانشجو طبق فرمت خواسته شده"""
        print(f"Student: {self.name} (ID: {self.student_id})")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
        print(f"Average: {self.average():.1f}")
        print(f"Best course: {self.best_course()}")
        print(f"Failed courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")
        print("-" * 35)


# --- بخش امتیازی: کلاس Classroom ---
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        """اضافه کردن دانشجو به کلاس"""
        self.students.append(student)

    def top_student(self):
        """پیدا کردن دانشجویی با بالاترین معدل"""
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())

    def class_average(self):
        """محاسبه میانگین کل کلاس"""
        if not self.students:
            return 0
        total_avg = sum(s.average() for s in self.students)
        return total_avg / len(self.students)


# --- بخش تست و اجرای خواسته شده در صورت سوال ---
if __name__ == "__main__":
    print("=== تست تمرین ۲ (Student) ===\n")
    
    # ساخت دو دانشجو با حداقل ۴ درس
    s1 = Student("Sara Ahmadi", "40312345")
    s1.add_grade("Math", 18)
    s1.add_grade("Physics", 9)
    s1.add_grade("Programming", 20)
    s1.add_grade("English", 15)

    s2 = Student("Ali Rezaei", "40312346")
    s2.add_grade("Math", 12)
    s2.add_grade("Physics", 10.5)
    s2.add_grade("Programming", 14)
    s2.add_grade("English", 8)

    # چاپ کارنامه هر دو دانشجو
    print("--- کارنامه دانشجو اول ---")
    s1.report()

    print("--- کارنامه دانشجو دوم ---")
    s2.report()

    # تست نمره نامعتبر
    print("--- تست ثبت نمره نامعتبر (۲۵) ---")
    s1.add_grade("Chemistry", 25)

    # تست بخش امتیازی کلاس درس
    print("\n--- تست بخش امتیازی (Classroom) ---")
    cls = Classroom()
    cls.add_student(s1)
    cls.add_student(s2)

    top = cls.top_student()
    print(f"دانشجوی برتر کلاس: {top.name} با معدل {top.average():.2f}")
    print(f"میانگین کل کلاس: {cls.class_average():.2f}")
