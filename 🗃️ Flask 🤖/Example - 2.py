from flask import Flask

# we need to create an app instance
app=Flask(__name__)

@app.route('/')    # http://127.0.0.1:8080
def greet():
    return('welcome')

@app.route('/greet1')    # http://127.0.0.1:8080/greet1
def greet1():
    return('good morning')

@app.route('/greet2/go')    # http://127.0.0.1:8080/greet2/go
def greet2():
    return('good eve')

if __name__=="__main__":
    app.run(debug=True,port=8080,host='0.0.0.0')

