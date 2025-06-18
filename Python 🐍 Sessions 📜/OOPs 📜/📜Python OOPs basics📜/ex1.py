"""
change-1: Create a class
change-2: write self in each function inside the brackets
         Note: Self is not a argument
         add and sub has only two arguments a,b

change-3: Call the class first then using class call the fnctions
"""
class Math_Func:
    def add(self,a,b):
        return(a+b)

    def sub(self,a,b):
        return(a-b)

obj=Math_Func()
addition=obj.add(20,30)  # random.randint
subtraction=obj.sub(20,30)
print('The addition is:',addition)
print('The subtraction is:',subtraction)


addition=Math_Func().add(200,300)  # random.randint
subtraction=Math_Func().sub(200,300)
print('The addition is:',addition)
print('The subtraction is:',subtraction)