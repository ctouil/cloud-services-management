from flask import Flask, request, jsonify
from models import db, User, Service

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mongodb://localhost:27017/cloud_services'
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([service.to_dict() for service in services])

if __name__ == '__main__':
    app.run(debug=True)