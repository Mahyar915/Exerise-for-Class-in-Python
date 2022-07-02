# Exerise-for-Class-in-Python
# Python example for Class
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
