#Program to build custom range function with start,step and end values containing iterable and next function 
class MyRange:
    def __init__(self,start,end,steps = 1):
        self.value = start
        self.end = end
        self.steps = steps
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        else:
            current = self.value
            self.value += self.steps
            return current

nums = MyRange(2,10)
print(next(nums))
print(next(nums))
print(next(nums))
