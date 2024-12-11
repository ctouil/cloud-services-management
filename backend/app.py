from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Service
import mongoengine as me

app = Flask(__name__)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'cloud_services',
    'host': 'localhost',
    'port': 27017
}
me.connect('cloud_services')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], password=data['password'])
    user.save()
    return jsonify({'message': 'User registered successfully'})

@app.route('/services', methods=['GET', 'POST'])
def manage_services():
    if request.method == 'GET':
        services = Service.objects()
        return jsonify([service.to_json() for service in services])
    elif request.method == 'POST':
        data = request.json
        service = Service(name=data['name'], description=data['description'])
        service.save()
        return jsonify({'message': 'Service added successfully'})

@app.route('/services/<id>', methods=['PUT', 'DELETE'])
def modify_service(id):
    service = Service.objects(id=id).first()
    if not service:
        return jsonify({'error': 'Service not found'}), 404

    if request.method == 'PUT':
        data = request.json
        service.update(name=data['name'], description=data['description'])
        return jsonify({'message': 'Service updated successfully'})
    elif request.method == 'DELETE':
        service.delete()
        return jsonify({'message': 'Service deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)