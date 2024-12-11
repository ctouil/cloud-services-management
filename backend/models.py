import mongoengine as me

class User(me.Document):
    username = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)

class Service(me.Document):
    name = me.StringField(required=True, unique=True)
    description = me.StringField()

def to_json(self):
    return {"id": str(self.id), "name": self.name, "description": self.description}