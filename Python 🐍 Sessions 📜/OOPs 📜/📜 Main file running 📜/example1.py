"""
create a class called a Math func
apply init
attr1: add
attr2: sub
run those
"""

class Math_Func:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)
    def sub(self):
        return(self.a-self.b)


if __name__=="__main__":
    ADD=Math_Func(100,200).add()
    SUB=Math_Func(10,20).sub()
    print(ADD,SUB)