from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/hello')
# def hello1():
#     return 'hello'

# @app.route('/user/<username>')
# def hello(username):
#     return f'Hello, {username}'

# @app.route('/user/<int:user_id>')
# def get_user_by_id(user_id):
#     return f'User id is: {user_id}'

# @app.route('/path/<path:subpath>')
# def get_subpath(subpath):
#     return f'Subpath is : {subpath}'

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# def show_hello():
#     return "hello"

# @app.get('/hello')
# def hello():
#     return show_hello()

@app.route('/login', methods=['POST', 'PUT'])
def login():
    if request.method == 'POST':
        return 'this is post request'
    elif request.method == 'GET':
        return 'this is get request'
    elif request.method == 'PUT':
        return 'this is put request'
    