#Part A

#1
x = 10  #int : whole numbers 
pi = 3.14  #float : decimal numbers
name = "Wania"  #str : text
is_ready = True  #bool : logical values
nums = [1,2,3]  #list : ordered collection
coords = (10,20)  #tuple : immutable collection
student = {"name":"Ali","age":18}  #dict : key-value pairs

#2
def greet(name):
    return f"Hello, {name}!"

print(greet("Wania"))

#3
# List comprehension
squares = [x**2 for x in range(5)]

# Dictionary comprehension
student_marks = {name: len(name)*10 for name in ["Ali","Sara","Wania"]}

#4
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s1 = Student("Wania", "A")
print(s1.name, s1.grade)

#Part B

#1
# Write
with open("data.txt","w") as f:
    f.write("Hello World")

# Append
with open("data.txt","a") as f:
    f.write("\nNew Line")

# Read
with open("data.txt","r") as f:
    print(f.read())

#2
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion!")

#3
import csv, json

# CSV
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# JSON
with open("data.json") as f:
    data = json.load(f)
    print(data)

