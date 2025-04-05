from flask import Blueprint, render_template, request
main = Blueprint('main', __name__)

@main.route('/')
def index(user_input=""):
    return render_template('index.html', user_input=user_input)

@main.route('/submit', methods=['POST'])
def handle_form():
    user_input = request.form.get('user_input')
    # Do something with user_input (e.g., render it in a response)
    print(user_input)
    return index(user_input)