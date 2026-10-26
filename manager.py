import json

FILENAME = "students.json"

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    def show(self):
        print(f"{self.name}: {self.score} -> {self.get_grade()}")

def save_students(students):
    data = []
    for s in students:
        data.append({"name": s.name, "score": s.score})
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def load_students():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    students = []
    for d in data:
        students.append(Student(d["name"], d["score"]))
    return students

def find_student(students, name):
    for s in students:
        if s.name == name:
            return s
    return None

students = load_students()
print(f"មាន {len(students)} នាក់")

print("B sl o")