from flask import Flask,render_template




app = Flask(__name__)

@app.route('/')
@app.route('/index/<name>')
def index(name):
    skills = ['python','Flask','Django']
    courses = ['Python','C++','C#','JAVA']
    info = {'father' : 'Rajkumar', 'age' : 23, 'city' : 'Chennai'}
    is_logged_in = True;
    return render_template( 'index.html',user_name = name, skills = skills , info = info, courses = courses, logged_in = is_logged_in )



# @app.route('/about')

# def about():
#     return '<h1> this is the info page </h1>'

# @app.route('/contact')




@app.route('/path/<username>')
def show_user(username):
    return f'<h1> hello iam {username} </h1>'


if __name__ == '__main__' :
    app.run(debug = True)