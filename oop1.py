# std1 = {'name':'Michael','score':98}
# std2 = {'name':'Bob','score':81}
#
# def print_score(std):
#     print("%s:%s"%(std['name'],std['score']))
#
# print_score(std2)

# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s'%(self.name,self.score))
#
# bart = Student('Bart Simpson',59)
# lisa = Student('Lisa Simpson',87)
#
# bart.print_score()
# lisa.print_score()

# class Student(object):
#     pass
#
# bart = Student()
# print(bart)
# print(Student)
#
# bart.name = 'Bart Simpson'
#
# print(bart.name)

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(std):
        print("%s: %s"%(std.__name,std.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')

    # def get_grade(self):
    #     if self.score >=90:
    #         return 'A'
    #     elif self.score >=80:
    #         return 'B'
    #     else:
    #         return 'C'
# bart = Student('Bart Simpson',101)
# print(bart._Student__name)
# bart.set_score(55)
# print(bart.get_name(),bart.get_score())
# bart = Student('Bart',99)
# print(bart.name)
# print(bart.score)
# bart.print_score()
# print(bart.get_grade())
bart = Student('Bart',99)
print(bart.get_name())
bart.__name = 'New Name'
print(bart.__name)
print(bart.get_name())

def externalfunc(obj,truth):
    print("im out of the scope",truth*truth)

setattr(bart,'test',lambda x:x*x)

print(bart.test(5))























