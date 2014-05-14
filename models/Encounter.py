from models.validation.CleanInputs import CleanInputs


class Encounter:
    def __init__(self, identifier=None, visit_identifier=None, visit_type=None, diagnoses=None, prescriptions=None,
                 complaints=None, vitals=None, other_obs=None, lab_results=None, location=None):
        self.identifier = CleanInputs.strings(identifier)
        self.visit_identifier = CleanInputs.strings(visit_identifier)
        self.visit_identifier = CleanInputs.strings(visit_type)
        self.diagnoses = CleanInputs.instances(diagnoses)
        self.prescriptions = CleanInputs.instances(prescriptions)
        self.complaints = CleanInputs.instances(complaints)
        self.vitals = CleanInputs.instances(vitals)
        self.other_obs = CleanInputs.instances(other_obs)
        self.lab_results = CleanInputs.instances(lab_results)
        self.location = CleanInputs.strings(location)
