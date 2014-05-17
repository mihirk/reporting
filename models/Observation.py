from models.serialization_helper.serialization_helper import to_json
from models.validation.CleanInputs import CleanInputs


class Observation:
    def __init__(self, name=None, value=None):
        self.name = CleanInputs.strings(name)
        self.value = CleanInputs.strings(value)

    def get_json(self):
        return to_json(self)