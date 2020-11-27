# class student:
#     school = "Annamalai"

#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.laptop()
#     def show(self):
#         print(self.name, self.rollno)
#         self.lap.show()
#     class laptop:
#         def __init__(self):
#             self.brand = 'Lenovo'
#             self.ram = 8
#             self.cpu = 'i3'
#         def show(self):
#             print(self.brand, self.ram, self.cpu)

# s1 = student('Farheen', 1)
# s2 = student('Minni', 2)

# s1.show()
# s2.show()

# lap = student.laptop()

class student:          #outer class
    school = "Annamalai-Ubivarsity"
    def __init__(self, name, rollno, std):
        self.name = name
        self.rollno = rollno
        self.std = std
        self.lap = self.laptop()
    def show(self):
        print(self.name, self.rollno, self.std)
        self.lap.show()
    class laptop:  #inner class
        def __init__(self):
            self.brand = 'Lenovo'
            self.ram = 8
            self.cpu = 'i5'
        def show(self):
            print(self.brand, self.ram, self.cpu)

s1 = student("Farheen", 1, 15)
s2 = student("Minni", 2, 16)

s1.show()
s2.show()
lap = student.laptop()