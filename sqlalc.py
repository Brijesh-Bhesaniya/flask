from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@192.168.1.105/TEST_DB_21'

db = SQLAlchemy(app)

# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(20), unique=True, nullable=False)
#     last_name = db.Column(db.String(20), unique=True, nullable=False)
#     age = db.Column(db.Integer, nullable=False)

# with app.app_context():
#     db.create_all()

# @app.get('/user')
# def get_all_users():
#     print("hello")
#     users = Profile.query.all()
#     user_list = []
#     for user in users:
#         user_data = {
#             'id': user.id,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'age': user.age
#         }
#         user_list.append(user_data)
#     return jsonify(user_list)

# @app.post('/user')
# def add_user():
#     data = request.json
#     fname = data.get('first_name')
#     lname = data.get('last_name')
#     age = data.get('age')

#     new_user = Profile(first_name=fname, last_name=lname, age=age)

#     db.session.add(new_user)
#     db.session.commit()

#     return 'User created successfully'

# @app.put('/user/<int:user_id>')
# def update_user(user_id):
#     user = Profile.query.get(user_id)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     data = request.json
#     user.first_name = data.get('first_name', user.first_name)
#     user.last_name = data.get('last_name', user.last_name)
#     user.age = data.get('age', user.age)

#     db.session.commit()

#     return 'User updated successfully'

# @app.delete('/user/<int:user_id>')
# def delete_user(user_id):
#     user = Profile.query.get(user_id)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     db.session.delete(user)
#     db.session.commit()

#     return 'User deleted successfully'

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


with app.app_context():
    db.create_all()

# Create author
@app.route('/authors', methods=['POST'])
def create_author():
    data = request.json
    name = data.get('name')
    if name:
        new_author = Author(name=name)
        db.session.add(new_author)
        db.session.commit()
        return jsonify({'message': 'Author created successfully'}), 201
    else:
        return jsonify({'error': 'Name is required'}), 400

#get all authors
@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    result = []
    for author in authors:
        author_data = {
            'id': author.id,
            'name': author.name,
            'books': [book.title for book in author.books]
        }
        result.append(author_data)
    return jsonify({'authors': result})

# create a new book for a specific author
@app.route('/authors/<int:author_id>/books', methods=['POST'])
def create_book(author_id):
    author = Author.query.get(author_id)
    if author:
        data = request.json
        title = data.get('title')
        if title:
            new_book = Book(title=title, author_id=author_id)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({'message': 'Book created successfully'}), 201
        else:
            return jsonify({'error': 'Title is required'}), 400
    else:
        return jsonify({'error': 'Author not found'}), 404


if __name__ == '__main__':
    app.run()
