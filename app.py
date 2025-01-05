from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1> I am Dk </h1> <p>learn more be smart </p>'



@app.route('/about')

def about():
    return '<h1> this is the info page </h1>'

@app.route('/contact')

def contact():
    return '<h1> The contact page </h1>'


if __name__ == '__main__' :
    app.run(debug = True)