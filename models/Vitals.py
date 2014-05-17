from models.serialization_helper.serialization_helper import to_json, instance_json
from models.validation.CleanInputs import CleanInputs


class Vitals:
    def __init__(self, weight=None, height=None, bmi=None, bp_systolic=None, bp_diastolic=None, pulse=None):
        self.weight = CleanInputs.instance(weight)
        self.height = CleanInputs.instance(height)
        self.bmi = CleanInputs.instance(bmi)
        self.bp_systolic = CleanInputs.instance(bp_systolic)
        self.bp_diastolic = CleanInputs.instance(bp_diastolic)
        self.pulse = CleanInputs.instance(pulse)

    def jsonify(self):
        json_object = self
        json_object.weight = instance_json(self.weight)
        json_object.height = instance_json(self.height)
        json_object.bmi = instance_json(self.bmi)
        json_object.bp_diastolic = instance_json(self.bp_diastolic)
        json_object.bp_systolic = instance_json(self.bp_systolic)
        json_object.pulse = instance_json(self.pulse)
        return json_object

    def get_json(self):
        return to_json(self)