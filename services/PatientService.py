from services.ElasticSearchConnection import ElasticSearchHandler
from ast import literal_eval



class PatientService:
    def __init__(self, host=None, index=None):
        self.es_handler = ElasticSearchHandler(host)
        if index:
            self.es_handler.create_index(index)
        else:
            self.es_handler.create_index("reporting")

    def push_to_elastic_search(self, patient, index):
        return self.es_handler.add_to_es(index, "Patient", patient)
