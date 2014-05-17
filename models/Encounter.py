import json
from models.serialization_helper.serialization_helper import instance_json, to_json
from models.validation.CleanInputs import CleanInputs


class Encounter:
    def __init__(self, identifier=None, visit_identifier=None, visit_type=None, diagnoses=None, prescriptions=None,
                 complaints=None, vitals=None, other_obs=None, lab_results=None, location=None):
        self.identifier = CleanInputs.strings(identifier)
        self.visit_identifier = CleanInputs.strings(visit_identifier)
        self.visit_identifier = CleanInputs.strings(visit_type)
        self.diagnoses = CleanInputs.instances(diagnoses)
        self.prescriptions = CleanInputs.instances(prescriptions)
        self.complaints = CleanInputs.instances(complaints)
        self.vitals = CleanInputs.instance(vitals)
        self.other_obs = CleanInputs.instances(other_obs)
        self.lab_results = CleanInputs.instances(lab_results)
        self.location = CleanInputs.strings(location)

    def get_json(self):
        return to_json(self)

    def jsonify(self):
        json_object = self
        json_object.diagnoses = map(instance_json, json_object.diagnoses)
        json_object.prescriptions = map(instance_json, json_object.prescriptions)
        json_object.complaints = map(instance_json, json_object.complaints)
        json_object.vitals = instance_json(json_object.vitals)
        json_object.other_obs = map(instance_json, json_object.other_obs)
        json_object.lab_results = map(instance_json, json_object.lab_results)
        return json_object