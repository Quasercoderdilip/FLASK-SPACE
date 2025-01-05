from flask import Flask,render_template




app = Flask(__name__)

@app.route('/')
@app.route('/index/<name>')
def index(name):
    skills = ['python','Flask','Django']
    info = {'father' : 'Rajkumar', 'age' : 23, 'city' : 'Chennai'}
    return render_template('index.html',user_name = name, skills = skills , info = info)



# @app.route('/about')

# def about():
#     return '<h1> this is the info page </h1>'

# @app.route('/contact')

# def contact():
#     return '<h1> The contact page </h1>'


@app.route('/path/<username>')
def show_user(username):
    return f'<h1> hello iam {username} </h1>'


if __name__ == '__main__' :
    app.run(debug = True)