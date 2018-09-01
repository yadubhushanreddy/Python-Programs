import time
class Sample_Class:

    def fun1():
        print("fun1")

    def fun2(self):
        print("fun2")

    def fun3(self):
        print("fun3")

class_obj = Sample_Class()
function_name = "class_obj.fun3()" #For time being, lets think that this is a function name that comes from excel sheet
time.sleep(5)
eval(function_name)
