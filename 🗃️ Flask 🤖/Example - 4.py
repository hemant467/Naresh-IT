from flask import Flask , request

# we need to create an app instance
app=Flask(__name__)

@app.route('/')    # http://127.0.0.1:5000
def greet():
    return('welcome')

@app.route('/info/<name>/<int:age>')    # http://127.0.0.1:5000/info/python/10
def info(name,age):
    return(f'hello my name is {name}, age is {age}')

@app.route('/profile')    # http://127.0.0.1:5000/profile?name='python'&age=25
def profile():
    name=request.args.get('name','unknown',type=str)
    age=request.args.get('age','unknown',type=int)
    return(f'hello my name is {name}, age is {age}')



if __name__=="__main__":
    app.run(debug=True)

