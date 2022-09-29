from flask_marshmallow import Schema
from marshmallow.fields import List, Str


class RequirementsSchema(Schema):
    class Meta:
        fields = ["content"]

    content = List(Str())
