from models.serialization_helper.serialization_helper import to_json
from models.validation.CleanInputs import CleanInputs


class Complaints:
    def __init__(self, name=None, date=None, duration=None):
        self.name = CleanInputs.strings(name)
        self.date = CleanInputs.strings(date)
        self.duration = CleanInputs.strings(duration)

    def get_json(self):
        return to_json(self)
