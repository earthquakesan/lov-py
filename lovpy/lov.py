import requests

class Lov(object):
    searchUri = "http://lov.okfn.org/dataset/lov/api/v1/search"

    def __init__(self):
        pass

    def search(self, string):
        termType = {
                "property": "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property",
                "class": ""
                }
        params = {
                'q': string,
                #'type': '',
                #'vocSpace': '', #filter query results on a Vocabulary Space an element/vocabulary belongs to. e.g. "http://lov.okfn.org/dataset/lov/lov#WORLD"
                #'voc': '', #filter query results on a Vocabulary an element belongs to. e.g. "http://www.w3.org/2003/01/geo/wgs84_pos"
                #'offset': 0,
                #'limit': 0
                }
        r = requests.get(self.searchUri, params=params)
        result = r.json()
        print r.url
        import ipdb; ipdb.set_trace()

if __name__ == "__main__":
    lov = Lov()
    lov.search('Latitude')
    print "hi"
    http://lov.okfn.org/dataset/lov/api/v1/search?q=Latitude
    http://lov.okfn.org/dataset/lov/api/v1/search?q=Latitude
