#!/usr/bin/python3

# Python Modules
import requests
import xmltodict


def get_genome(id):
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=genome&db=nuccore&id='
    request = requests.get('{0}{1}'.format(url, id))
    return request.text


def search(search_term):
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=genome&term='
    request = requests.get('{0}{1}'.format(url, search_term))
    xml = xmltodict.parse(request.text)
    genome = get_genome(xml['eSearchResult']['IdList']['Id'])
    return genome

if __name__ == '__main__':
    print('Organism Name: \n')
    term = input()
    print(search(term))
