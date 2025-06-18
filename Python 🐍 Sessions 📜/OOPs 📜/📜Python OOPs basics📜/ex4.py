class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)

    def sub(self):
        return(self.a-self.b)

    def mul(self):
        return(self.a*self.b)

    def div(self):
        return(self.a/self.b)

obj=Calculator(100,200)
ADD=obj.add()
SUB=obj.sub()
MUL=obj.mul()
DIV=obj.div()
print(ADD,SUB,MUL,DIV)


ADD=Calculator(100,200).add()
SUB=Calculator(300,400).sub()
MUL=Calculator(600,2).mul()
DIV=Calculator(100,200).div()
print(ADD,SUB,MUL,DIV)