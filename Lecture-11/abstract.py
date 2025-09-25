from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

class exam_calss(Absclass):
    def task(self):
        print("We are inside exam_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)

exam_obj = exam_calss()
exam_obj.task()
exam_obj.print(100)

print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("exam_obj is instance of Absclass? ", isinstance(exam_obj, Absclass))