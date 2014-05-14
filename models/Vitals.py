from models.validation.CleanInputs import CleanInputs


class Vitals:
    def __init__(self, weight=None, height=None, bmi=None, bp_systolic=None, bp_diastolic=None, pulse=None):
        self.weight = CleanInputs.instance(weight)
        self.height = CleanInputs.instance(height)
        self.bmi = CleanInputs.instance(bmi)
        self.bp_systolic = CleanInputs.instance(bp_systolic)
        self.bp_diastolic = CleanInputs.instance(bp_diastolic)
        self.pulse = CleanInputs.instance(pulse)