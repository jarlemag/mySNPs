#read23andme.py

import string
filename = 'Snippet.txt'

referencesequence = 'CRCh36'


#Open dataset

def createlist(filename): #Extract SNP data from a 23andme file.

    with open(filename) as dataset:
        listoflines = dataset.readlines()

    SNPlist = []

    for line in listoflines:
        if line[0] != '#': #Unless the line has been commented out.
            linesplit = string.split(line)
            currentSNP = {'rsID':linesplit[0],'Chromosome':linesplit[1],
                      'Position':linesplit[2],'Genotype':linesplit[3],'Reference':referencesequence}
            SNPlist.append(currentSNP)
    return SNPlist

def printfile():
    with open(filename) as f:
        for line in f.readlines():
            print line

mylist = createlist(filename)

        
#printfile()

#print SNPlist


def returnSNP(rsID,SNPlist):
    if type(rsID) == int:
        rsID = str(rsID)
    snpfound = False
    for SNP in SNPlist:
        if SNP['rsID'] == rsID:
            snpfound = True
            return SNP
    if snpfound == False:
        print 'Could not find entry for rsID %s' % rsID

def showinfo(SNP):
    print 'Selected SNP:'
    print 'rsID:',SNP['rsID']
    print 'Chromosome:',SNP['Chromosome']
    print 'Position:',SNP['Position']
    print 'Genotype:',SNP['Genotype']
    print 'Reference sequence:',SNP['Reference']

anSNP = returnSNP('rs3934834',mylist)

returnSNP('kake',mylist)

def listrs(SNPlist):
    rslist = [entry['rsID'] for entry in SNPlist]
    return rslist

small_list = mylist[0:5]

tiny_list = mylist[0:3]

def find_union(SNPlist1,SNPlist2):
    #Find SNPs which are in both of two lists
    rslist1 = listrs(SNPlist1)
    rslist2 = listrs(SNPlist2)
    list1set = set(rslist1)
    unionset = list1set.intersection(rslist2)
    return unionset

def comparefiles(file1,file2):
    #Compare two genotypefiles. Return SNPs which are in both files.
    list1 = createlist(file1)
    list2 = createlist(file2)
    inboth = find_union(list1,list2)
    return inboth

showinfo(anSNP)

print 'Comparing files:'
print comparefiles('snippet.txt','snippet2.txt')

theunion = find_union(mylist,small_list)
print 'Union:',theunion

def findhomozygotesrs(SNPlist):
    #Find all homozygous loci
    homozygotes = []
    for element in SNPlist:
        if element['Genotype'][0] == element['Genotype'][1]:
            homozygotes.append(element['rsID'])
    return homozygotes

homozygotes = findhomozygotesrs(small_list)

print 'Homozygotes:',homozygotes

def getposinlist(rsID,SNPlist): #Get the position, in an SNP list, of a dictionary entry with a given rsID
    for i in range(len(SNPlist)):
        if SNPlist[i]['rsID']== rsID:
            index = i
    return index

print 'tinylist:',tiny_list

position = getposinlist('rs3094315',tiny_list)
print 'position:',position
print 'rs:','rs3094315'

def findheterozygotesrs(SNPlist):
    #Find all heterozygous loci
    heterozygotes = []
    for element in SNPlist:
        if element['Genotype'][0] != element['Genotype'][1]:
            heterozygotes.append(element['rsID'])
    return heterozygotes


def sanitycheck(SNPlist):
    #Run a sanity check on a list of SNP genotypes
    sane = True
    N = len(SNPlist)
    if (len(findhomozygotesrs(SNPlist)) + len(findheterozygotesrs(SNPlist)) ) != N:
        sane = False
    return sane

print 'Sanitycheck:',sanitycheck(mylist)

def findnoncalled(SNPlist):
    #Find all loci with at least one uncalled base
    noncalled = []
    for SNP in SNPlist:
        if ('N' in SNP['Genotype']) or ('n' in SNP['Genotype']):
            noncalled.append(SNP['rsID'])
    return noncalled

noncalled = findnoncalled(mylist)
print 'noncalled:',noncalled
            

def findgenotype(genotype,SNPlist):
    matching = []
    for SNP in SNPlist:
        if SNP['Genotype'] == genotype:
            matching.append(SNP['rsID'])
    return matching

print findgenotype('GG',tiny_list)
