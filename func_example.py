def func(a, b, c):
    """
    print a, b, c, in order
    """

    print(a, b, c)

func(1, 'hello', 66.66)

def func2(a):
    return a

def func3(a):
    print(a) # return None

print(func2(1))
print(func3(1))

class Student:

    def __init__(self, name = "") -> None:
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def speak(self):
        print(f'Hello, World! I am {self.name}')

    def __private(self): # private
        print("NO")
    
    def public(self):
        print("YES")
        self.__private()

stu = Student()
stu.set_name("Simon")
stu.speak()
# stu.__private()
stu.public()

class GoodStudent(Student):
    def speak(self):
        print(f'Good student name: {self.name}')

helen = GoodStudent("Helen")
helen.speak()

print(issubclass(GoodStudent, Student))
print(GoodStudent.__bases__)
print(isinstance(helen, Student))

# Always use self for the first argument to instance methods.
# Always use cls for the first argument to class methods.
# annotation @classmethod == static
class MyClass:
    @classmethod
    def say(cls):
        print("Hey")

    value = 0

    @property   # use method like attribute / flied
    def score(self):
        return self.value
    
    @score.setter
    def score(self, args):
        self.value = args

a = MyClass()
print(a.score)
a.score = 100
print(a.score)

MyClass().say()
MyClass.say()