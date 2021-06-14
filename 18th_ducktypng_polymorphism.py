'''class Duck:
    def talk(self):
        print("Duck talking")
class Dog:
    def bark(self):
        print("Dog talking")    
class Cat:
    def talk(self):
        print("Cat talking")

l = [Duck(),Dog(),Cat()]
for obj in l:
    obj.talk()
'''
# output :

# Duck talking
# Dog talking
# Cat talking

class Duck:
    def talk(self):
        print("Duck talking")
class Dog:
    def bark(self):
        print("Dog barking")    
class Cat:
    def talk(self):
        print("Cat talking")

l = [Duck(),Dog(),Cat()]
for obj in l:
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()