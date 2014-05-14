from models.validation.CleanInputs import CleanInputs


class Adherence:
    def __init__(self, medicine=None, start_date=None, stop_date=None, stop_reason=None):
        self.medicine = CleanInputs.strings(medicine)
        self.start_date = CleanInputs.strings(start_date)
        self.stop_date = CleanInputs.strings(stop_date)
        self.stop_reason = CleanInputs.strings(stop_reason)