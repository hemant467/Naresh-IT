from flask import Flask, redirect , url_for

# we need to create an app instance
app=Flask(__name__)

@app.route('/')    
def greet():
    return('welcome')

@app.route('/greet1')   
def greet1():
    return('good morning')

@app.route('/go_amazon')
def go_amazon():
    return(redirect("https://www.amazon.in/"))

@app.route('/greet2')   
def greet2():
    return(redirect(url_for('greet1')))

if __name__=="__main__":
    app.run(debug=True)

