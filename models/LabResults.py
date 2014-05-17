from models.serialization_helper.serialization_helper import to_json
from models.validation.CleanInputs import CleanInputs


class LabResults:
    def __init__(self, test=None, date=None, results=None):
        self.test = CleanInputs.strings(test)
        self.date = CleanInputs.strings(date)
        self.results = CleanInputs.instances(results)

    def get_json(self):
        return to_json(self)