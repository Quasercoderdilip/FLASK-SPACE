from flask import Flask, request, render_template

app = Flask(__name__)

# Function to handle the calculation
def calculate_expression(expression):
    try:
        # Use eval to calculate the result of the expression
        result = eval(expression)
        return result
    except:
        return 'ERROR'

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the expression from the POST request
    expression = request.form.get('expression')
    
    # Calculate the result
    result = calculate_expression(expression)
    
    return render_template('calculator.html', expression=expression, result=result)


@app.route('/reset', methods=['POST'])
def reset():
    return render_template('calculator.html', expression = '', result = '')



if __name__ == '__main__':
    app.run(debug=True)
