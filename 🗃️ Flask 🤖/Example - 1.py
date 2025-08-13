from flask import Flask

# we need to create an app instance
app=Flask(__name__)

@app.route('/')    # Decorator
def greet():
    return('welcome')

@app.route('/greet1')    # Decorator
def greet1():
    return('good morning')

if __name__=="__main__":
    app.run(debug=True)

