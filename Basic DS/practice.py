class Arr:
    def __init__(self,x):
        self.arr = [0] * x
        self.len = 0
    def length(self):
        print(self.len)
    def append(self, x):
        if self.arr[-1] == 0:
            self.arr[self.len] = x
            self.len += 1
        else:
            print("Array is full. Do something else.")
    def pop(self):
        if self.arr[0] == 0:
            print("Array is empty. Do something else.")
        else:
            self.arr[self.len - 1] = 0
            self.len -= 1
            
    def print(self):
        print(self.arr[:self.len])

x = Arr(2)
x.append(5)
x.append(8)
x.print()
x.append(9)
x.pop()
x.print()