from elasticsearch import Elasticsearch
import os


class ElasticSearchHandler:
    def __init__(self, host=None):
        if not host:
            host = os.getenv("ES_HOST")
        self.es_handle = Elasticsearch(hosts=host)

    def check_index(self, index):
        return self.es_handle.indices.exists(index)

    def create_index(self, index):
        if not self.check_index(index):
            self.es_handle.indices.create(index)

    def add_to_es(self, index, document_type, body):
        return self.es_handle.create(index=index, doc_type=document_type, body=body)

    def get_from_es(self, index, id):
        return self.es_handle.get(index, id=id)


    def delete_by_id(self, index, document_type, id):
        self.es_handle.delete(index, document_type, id)


