from models.validation.CleanInputs import CleanInputs


class LabResults:
    def __init__(self, test=None, date=None, results=None):
        self.test = CleanInputs.strings(test)
        self.date = CleanInputs.strings(date)
        self.results = CleanInputs.instances(results)