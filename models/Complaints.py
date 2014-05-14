from models.validation.CleanInputs import CleanInputs


class Complaints:
    def __init__(self, name=None, date=None, duration=None):
        self.name = CleanInputs.strings(name)
        self.date = CleanInputs.strings(date)
        self.duration = CleanInputs.strings(duration)
