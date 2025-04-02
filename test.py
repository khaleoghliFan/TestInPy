print("hello world")
class Calculator:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        result=self.x + self.y
        return result
    def subtract(self):
        result=self.x - self.y
        return result
    def multiply(self):
        result=self.x * self.y
        return result
    def divide(self):
        if self.y==0:
            raise ValueError("divided by zero not allowed")
        result = self.x / self.y
        return result
    def __repr__(self):
        return f'cal({self.x!r},{self.y!r})'
