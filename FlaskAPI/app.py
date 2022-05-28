from flask import Flask, jsonify, request
from all_variables import TeamName, Port
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#common variables
team_name = TeamName()
port_ = Port()

list_members = ['Prathmesh', 'Keshav', 'Ankit']

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def Home():
    return jsonify({'Status': 'Running'})

@app.route('/detail', methods=['GET'])
def Detail():
    return jsonify({'Stack': 'Flask Backend API'})

@app.route('/members', methods=['GET'])
def Members():
    return jsonify({'Team': team_name, 'Members': list_members})

@app.route('/addmember', methods=['POST'])
def AddMember():
    if request.method == 'POST':
        list_members.append(request.json['newmember'])
    return jsonify({'Team': team_name, 'Members': list_members})

if __name__ == '__main__':
    app.run(port=port_)