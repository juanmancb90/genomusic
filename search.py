#!/usr/bin/python3

# Python Modules
import requests
import xmltodict


def get_genome(id):
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=genome&db=nuccore&id='
    request = requests.get('{0}{1}'.format(url, id))
    return request.text


def search(search_term):
    db = 'protein'
    term = 'canis familiaris'
    terms = '?db={0}&term={1}&retmax=1&usehistory=y'.format(db, term)
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/{0}'.format(terms)
    request = requests.get('{0}{1}'.format(url, search_term))
    xml = xmltodict.parse(request.text)
    # genome = get_genome(xml['eSearchResult']['IdList']['Id'])
    return xml

if __name__ == '__main__':
    print('Organism Name: \n')
    term = input()
    print(search(term))
