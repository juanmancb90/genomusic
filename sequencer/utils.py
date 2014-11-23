# Python Modules
import requests
import xmltodict
import urllib
import json

# App Modules
from music.generator import sampler


def get_sequence(db, query_key, web_env):
    terms = '?db={0}&query_key={1}&WebEnv={2}&rettype=fasta&retmode=text&retmax=1'.format(db, query_key, web_env)
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/{0}'.format(terms)
    response = urllib.request.urlopen(url)
    return json.dumps([x.decode("utf-8") for x in response.readlines()])


def search(term, db):
    terms = '?db={0}&term={1}&retmax=1&usehistory=y'.format(db, term)
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/{0}'.format(terms)
    response = requests.get(url)
    xml = xmltodict.parse(response.text)
    query_key = xml['eSearchResult']['QueryKey']
    web_env = xml['eSearchResult']['WebEnv']
    genome = get_sequence(db, query_key, web_env)
    data = sampler(genome)
    return genome

if __name__ == '__main__':
    print('Organism Name: \n')
    term = input()
    db = 'nucleotid'
    print(search(term, db))
