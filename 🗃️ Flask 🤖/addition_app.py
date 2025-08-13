from flask import Flask , request

# we need to create an app instance
app=Flask(__name__)

@app.route('/')   
def greet():
    return('welcome')

@app.route('/addition')
def addition():
    num1=request.args.get('num1',type=int)
    num2=request.args.get('num2',type=int)
    result=num1+num2
    return(f"the addition of {num1} and {num2} is:{result}")



if __name__=="__main__":
    app.run(debug=True)