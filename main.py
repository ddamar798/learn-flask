from flask import Flask

app = Flask(__name__) #instant flask

@app.route('/') #define a route
def index():
    return 'Hello, World!' #return a string

app.run(debug=True)