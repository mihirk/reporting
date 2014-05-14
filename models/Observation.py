from models.validation.CleanInputs import CleanInputs


class Observation:
    def __init__(self, name=None, value=None):
        self.name = CleanInputs.strings(name)
        self.value = CleanInputs.strings(value)
