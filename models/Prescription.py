from models.serialization_helper.serialization_helper import to_json
from models.validation.CleanInputs import CleanInputs


class Prescription:
    def __init__(self, name=None, start_date=None, duration=None, dosage_code=None):
        self.name = CleanInputs.strings(name)
        self.start_date = CleanInputs.strings(start_date)
        self.duration = CleanInputs.strings(duration)
        self.dosage_code = CleanInputs.strings(dosage_code)

    def get_json(self):
        return to_json(self)