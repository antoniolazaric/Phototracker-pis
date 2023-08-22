from flask import Flask, request, jsonify, render_template
from pony.orm import Database, Required, PrimaryKey, db_session, select
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

class Photographer(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    experience = Required(str)
    equipment = Required(str)
    phone = Required(str)
    email = Required(str)

    

db.generate_mapping(create_tables=True)

@app.route('/photographer', methods=['POST'])
@db_session
def add_photographer():
    data = request.get_json()
    photographer = Photographer(
        first_name=data['first_name'],
        last_name=data['last_name'],
        experience=data['experience'],
        equipment=data['equipment'],
        phone=data['phone'],
        email=data['email']
    )
    return jsonify(success=True, id=photographer.id)


@app.route('/photographers', methods=['GET'])
@db_session
def get_photographers():
    photographers = select(p for p in Photographer)[:]
    photographers_list = [p.to_dict() for p in photographers]
    return jsonify(photographers_list)

@app.route('/photographer/<int:photographer_id>', methods=['PUT'])
@db_session
def update_photographer(photographer_id):
    photographer = Photographer.get(id=photographer_id)
    if photographer is None:
        return {"error": "Photographer not found"}, 404
    data = request.get_json()
    photographer.first_name = data.get('first_name', photographer.first_name)
    photographer.last_name = data.get('last_name', photographer.last_name)
    photographer.experience = data.get('experience', photographer.experience)
    photographer.equipment = data.get('equipment', photographer.equipment)
    photographer.phone = data.get('phone', photographer.phone)
    photographer.email = data.get('email', photographer.email)
    return jsonify(success=True)

@app.route('/photographer/<int:photographer_id>', methods=['DELETE'])
@db_session
def delete_photographer(photographer_id):
    photographer = Photographer.get(id=photographer_id)
    if photographer is None:
        return {"error": "Photographer not found"}, 404
    photographer.delete()
    return jsonify(success=True)




if __name__ == '__main__':
    app.run(debug=True)