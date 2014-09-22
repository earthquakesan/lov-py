import requests

class Lov(object):
    searchUri = "http://lov.okfn.org/dataset/lov/api/v2/search"

    def __init__(self):
        pass

    def searchClass(self, string):
        """
            {u'highlight': {u'http://purl.org/dc/terms/description@en': [u'<b>Latitude</b> is a geographic coordinate which refers'],
                            u'http://www.w3.org/2000/01/rdf-schema#label@en': [u'<b>latitude</b>']},
             u'metrics.occurrencesInDatasets': [0],
             u'metrics.reusedByDatasets': [0],
             u'prefixedName': [u'sio:SIO_000319'],
             u'score': 0.5555556,
             u'type': u'class',
             u'uri': [u'http://semanticscience.org/resource/SIO_000319'],
             u'vocabulary.prefix': [u'sio']}
        """
        return self.search(string, 'class')

    def searchProperty(self, string):
        """
            Results[0] example
            {u'highlight': {u'http://www.w3.org/2000/01/rdf-schema#comment': [u'The WGS84 <b>latitude</b> of a SpatialThing (decimal degrees).'],
                            u'http://www.w3.org/2000/01/rdf-schema#label': [u'<b>latitude</b>'],
                            u'vocabulary.http://purl.org/dc/terms/description@en': [u'A vocabulary for representing <b>latitude</b>, longitude']},
             u'metrics.occurrencesInDatasets': [344715],
             u'metrics.reusedByDatasets': [44],
             u'prefixedName': [u'geo:lat'],
             u'score': 1,
             u'type': u'property',
             u'uri': [u'http://www.w3.org/2003/01/geo/wgs84_pos#lat'],
             u'vocabulary.prefix': [u'geo']}
        """
        return self.search(string, 'property')

    def searchDatatype(self, string):
        """
            Results[0] example
            {u'highlight': {u'http://www.w3.org/2000/01/rdf-schema#comment@en-au': [u'Geographic coordinates expressed as <b>latitude</b> and longitude.']},
             u'metrics.occurrencesInDatasets': [0],
             u'metrics.reusedByDatasets': [0],
             u'prefixedName': [u'agls:Geocode'],
             u'score': 1,
             u'type': u'datatype',
             u'uri': [u'http://www.agls.gov.au/agls/terms/Geocode'],
             u'vocabulary.prefix': [u'agls']}
        """
        return self.search(string, 'datatype')

    def searchInstance(self, string):
        """
            Results[0] example
            {u'highlight': {u'http://www.w3.org/2000/01/rdf-schema#comment@en-au': [u'Geographic coordinates expressed as <b>latitude</b> and longitude.']},
             u'metrics.occurrencesInDatasets': [0],
             u'metrics.reusedByDatasets': [0],
             u'prefixedName': [u'agls:Geocode'],
             u'score': 1,
             u'type': u'instance',
             u'uri': [u'http://www.agls.gov.au/agls/terms/Geocode'],
             u'vocabulary.prefix': [u'agls']}
        """
        return self.search(string, 'instance')

    def search(self, string, type):
        #spec is located here: http://lov.okfn.org/dataset/lov/apidoc/
        params = {
                'q': string,
                'page_size': '10',
                'page': '1',
                'type': type,
                #'vocab': '',
                #'vocab_limit': '',
                #'tag': '',
                #'tag_limit': '10'
                }
        r = requests.get(self.searchUri, params=params)
        result = r.json()
        results = result['results']
        return results

if __name__ == "__main__":
    lov = Lov()
    import pprint
    pprinter = pprint.PrettyPrinter()
    lat = lov.searchInstance('Latitude')
    pprinter.pprint(lat[0])
    print "hi"
