class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)

    def sub(self):
        values=self.add()
        print('addition:',values)  # 100+200=300
        return(self.a-self.b)     # 100-200=-100

SUB=Calculator(100,200).sub()
print('Sub:',SUB)