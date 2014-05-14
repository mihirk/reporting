from models.validation.CleanInputs import CleanInputs


class Diagnosis:
    def __init__(self, name=None, date=None):
        self.name = CleanInputs.strings(name)
        self.date = CleanInputs.strings(date)