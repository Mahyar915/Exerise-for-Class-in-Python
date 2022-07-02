

'''
class person:
    pass
p1=person()
p2=person()
p1.name='John'
p1.age=10
p2.name='Mary'
p2.age=20
print(p1.name,'is',p1.age,'years old')
print(p2.name,'is',p2.age,'years old')
'''
''' 
class person:
    def set_attribute(self,name,age):
        self.name = name
        self.age = age
p1 = person()
p2 = person()
p1.set_attribute('John',10)
p2.set_attribute('Mary',20)
print(p1.name,'is',p1.age,'years old')
print(p2.name,'is',p2.age,'years old')
'''
class person():
    def set_attribute(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,'is',self.age,'years old')
    def is_underage(self):
        return self.age<18
p1=person()
p2=person()
p1.set_attribute('John',10)
p2.set_attribute('Mary',20)
p1.print()
p2.print()
print(p1.is_underage())
print(p2.is_underage())






