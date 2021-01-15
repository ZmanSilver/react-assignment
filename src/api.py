import random
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = generateID()
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd)
        # resp.status_code = 200 #optionally, you can always set a response code.
        # 200 is the default code for a normal response
        return resp, 201


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id:
        for i in range(len(users['users_list'])):
            if users['users_list'][i]['id'] == id:
                if request.method == 'GET':
                    return users['user_list'][i], 200
                if request.method == 'DELETE':
                    users['users_list'].pop(i)
                    return {}, 204

    return (users, 200) if request.method == 'GET' else ({}, 404)



def generateID():
    ID = []

    for i in range(6):
        ID.append(str(random.randint(0, 9)))

    return ''.join(ID)


users = {
    'users_list' :
    [
        {
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id' : 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}
