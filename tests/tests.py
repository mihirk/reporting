import json
import unittest
from models.Adherence import Adherence
from models.Complaints import Complaints
from models.Diagnosis import Diagnosis
from models.Encounter import Encounter
from models.LabResults import LabResults
from models.Observation import Observation
from models.Patient import Patient
from models.Prescription import Prescription
from models.Vitals import Vitals


class TestObjectSerialization(unittest.TestCase):
    def setUp(self):
        test_date = "22/01/1922"
        test_adherence = Adherence(medicine="Test Medicine", start_date= test_date, stop_date=test_date,
                                   stop_reason="Test Reason")
        test_complaints = Complaints(name="Test Name", date=test_date, duration="Test Duration")
        test_diagnosis = Diagnosis(name="Test Diagnosis", date=test_date)
        test_lab_results = LabResults(test="Test Test Name", date=test_date, results="Test Results")
        test_observation = Observation(name="Test Obs", value="Test Value")
        test_prescription = Prescription(name="Test_name", start_date=test_date, duration="Test Duration",
                                              dosage_code="Test Code")
        test_vitals = Vitals(test_observation, test_observation, test_observation,
                                  test_observation, test_observation, test_observation)
        test_encounter = Encounter(2195, 1, "TEST_TYPE", [test_diagnosis, test_diagnosis], [test_prescription], [test_complaints],
                                   test_vitals, [test_observation], [test_lab_results], "Test Location")
        self.test_patient_with_encounters = Patient("Test Patient", 2195, "Test Address", "Test Relatives", 12,
                               "Female", encounters=[test_encounter, test_encounter], adherences=[test_adherence])


    def is_valid_json(self, json_object):
        try:
            json.loads(json_object)
        except ValueError:
            return False
        return True

    def test_patient_serialization(self):
        serialized_patient = self.test_patient_with_encounters.get_json()
        self.assertTrue(self.is_valid_json(serialized_patient))

if __name__ == '__main__':
    unittest.main()
