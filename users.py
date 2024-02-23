from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/customers'
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    return jsonify({'users': user_list})

@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.json
    if user_data:
        result = mongo.db.users.insert_one(user_data)
        inserted_id = str(result.inserted_id)
        return jsonify({'message': 'User added successfully', 'user_id': inserted_id}), 201
    else:
        return jsonify({'error': 'User data is required'}), 400


@app.route('/users/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    print(user_id)
    user = mongo.db.users.find_one_or_404({'_id': ObjectId(user_id)})
    if user:
        user['_id'] = str(user['_id'])
        return {'user': user}
    else:
        return {'error': 'User not found'}, 404

@app.route('/users/bulk_insert', methods=['POST'])
def bulk_insert():
    try:
        data = request.json
        if isinstance(data, list):
            result = mongo.db.users.insert_many(data)
            return {'message': f'{len(result.inserted_ids)} documents inserted successfully'}, 201
        else:
            return {'error': 'Data must be a list of documents'}, 400
    except Exception as e:
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
