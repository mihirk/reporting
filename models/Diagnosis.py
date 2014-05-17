from models.serialization_helper.serialization_helper import to_json
from models.validation.CleanInputs import CleanInputs


class Diagnosis:
    def __init__(self, name=None, date=None):
        self.name = CleanInputs.strings(name)
        self.date = CleanInputs.strings(date)

    def get_json(self):
        return to_json(self)