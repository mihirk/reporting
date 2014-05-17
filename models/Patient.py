import json
from models.serialization_helper.serialization_helper import to_json, instance_json
from models.validation.CleanInputs import CleanInputs


class Patient:
    def __init__(self, name=None, identifier=None, address=None, relatives=None, age=None,
                 gender=None, encounters=None, adherences=None):
        self.name = CleanInputs.strings(name)
        self.identifier = CleanInputs.strings(identifier)
        self.address = CleanInputs.strings(address)
        self.relatives = CleanInputs.strings(relatives)
        self.age = CleanInputs.strings(age)
        self.gender = CleanInputs.strings(gender)
        self.encounters = CleanInputs.instances(encounters)
        self.adherences = CleanInputs.instances(adherences)

    def get_json(self):
        return to_json(self)

    def jsonify(self):
        json_object = self
        json_object.encounters = map(instance_json, json_object.encounters)
        json_object.adherences = map(instance_json, json_object.adherences)
        return json_object