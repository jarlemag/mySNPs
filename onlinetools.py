#onlinetools.py

'''
Functions and code for querying databased and websites.

Includes code from:

http://snpedia.com/index.php/Bulk


Links:
ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/database/organism_data/OmimVarLocusIdSNP.bcp.gz

'''

from wikitools import *


def snpedia_getallIDs():
    site = wiki.Wiki("http://bots.snpedia.com/api.php") # open snpedia
    snps = category.Category(site, "Is_a_snp")
    snpedia = []
       
    for article in snps.getAllMembersGen(namespaces=[0]):# get all snp-names as list and print them
        snpedia.append(article.title.lower())
        #print article.title
        print 'List saved.'
    return snpedia

def snpedia_getfulltext(snp):
    site = wiki.Wiki("http://bots.snpedia.com/api.php")
    pagehandle = page.Page(site,snp)
    snp_page = pagehandle.getWikiText()
    return snp_page
