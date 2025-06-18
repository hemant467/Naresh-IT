class Calculator1:
    def add(self,a,b):
        return(a+b)

    def sub(self,a,b):
        return(a-b)

class Calculator2:
    def mul(self,a,b):
        return(a*b)

    def div(self,a,b):
        return(a/b)


ADD=Calculator1().add(100,200)
SUB=Calculator1().sub(100,200)
MUL=Calculator2().mul(300,400)
DIV=Calculator2().div(400,500)
print(ADD,SUB,MUL,DIV)