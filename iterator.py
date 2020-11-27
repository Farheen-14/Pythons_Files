# nums = [2,5,7,3,5]

# it = iter(nums)
# print(it.__next__())  #next will provide the next value..
# print(it.__next__())
# print(next(it))

class Topten:
    def __init__(self):
        self.num = 6
    def __iter__(self):  # iter() : it is a iter method and it will give you the object of iterator
        return self
    def __next__(self):
        if self.num <= 12:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration("Message")
value = Topten()

for i in value:
    print(i)

