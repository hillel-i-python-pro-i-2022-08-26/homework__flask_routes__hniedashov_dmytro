from flask_marshmallow import Schema
from marshmallow.fields import Str


class UserSchema(Schema):
    class Meta:
        fields = ["name", "last_name", "email"]

    name = Str()
    last_name = Str()
    email = Str()
