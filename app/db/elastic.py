from elasticsearch import Elasticsearch

class ElasticDB:

    es = Elasticsearch(
        ['https://msb-elk.de050.corpintra.net/elasticsearch/050'],
        api_key=("ce02a0c3-2c29-4b4c-8b5d-a1c72ba1ca2a","a23a6fe6-d592-45f2-85d3-cf27a8822711"),
    )

    def getData(self):
        res = self.es.get(index="it-ocs_msb_prd-sps-s7-300-trend-v1-000023", id="HsfBEXwBHKoj1FjK0XGc")
        print(res['_source'])