from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'web/index.html', context)

def get_protein(request):
    """
    tomar query_key y webenv:

    http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/?db=<PROTEIN o NUCLEOTIDE>&term=<NOMBRE DE LA PROTEINA>&retmax=1&usehistory=y
    eutils.ncbi.nlm.nih.gov
    eutils.ncbi.nlm.nih.gov



    http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=<PROTEIN o NUCLEOTIDE>&query_key=<QUERY_KEY>&WebEnv=<WEBENV>&rettype=
fasta&retmode=text&retmax=1
    """
